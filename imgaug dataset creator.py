import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import imageio as imgio
import os

import cv2


from sklearn.utils import shuffle as skshuffle


from lxml import etree

import xml.etree.cElementTree as ET

from PIL import Image

from random import randint


ia.seed(100)

imagearray = []
lablearray = []
bg_images=[]
boundingboxes_arr = []


#possible improvement to make would be to incorporate relative paths, but since this code is only intended to be run once, i left it as is during its creation.


for subdir in os.listdir('C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\dtd\\images'): #loads backgrounds for future use
    for image in  os.listdir('C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\dtd\\images\\'+subdir):
        print(subdir)
        print(image)
        filename, type = os.path.splitext(image)
        if type ==".jpg": #specifies specific filetype only
            bg_images.append(imgio.imread('C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\dtd\\images\\' + subdir + '\\'+image))






for filename in os.listdir('C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\resized\\pngs'): #for gesture in images

    temparr = []


    image = imgio.imread('C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\resized\\pngs\\' + filename) #reads in the gesture


    for x in bg_images: #generate images

        randombackground = x #gets a background
        print(filename)
        width, height, channels = randombackground.shape #minimum width, height of 300 needed
        if width > 400 and height > 400:

            tempimage = Image.fromarray(image,'RGBA') #converts it to pil format for manipulation
            tempbg = Image.fromarray(randombackground, 'RGB')

            centerw = int(width/2) #finding the center of the background
            centerh = int(height/2)
            centerw -=150
            centerh -=150

            if centerw <0:
                centerw = 0
            if centerh <0:
                centerh = 0

            tempbg.paste(tempimage,(centerh,centerw),tempimage) #pastes the gesture into the center of the image
            tempbg.save('temp.jpg') #step to reload it into imgaug
            newimage = imgio.imread('temp.jpg')

            boundingbox = ia.BoundingBoxesOnImage([ #defines the bounding boxes for the image
                ia.BoundingBox(x1=centerh,x2=centerh+300,y1=centerw,y2=centerw+300)
            ], shape=newimage.shape)

            seq = iaa.Sequential([
                # simple img aug that is taken from https://imgaug.readthedocs.io/en/latest/source/examples_basics.html#a-simple-and-common-augmentation-sequence
                iaa.Fliplr(0.5),  # flips 50% images left or right for right or left hands
                iaa.Crop(percent=(0, 0.1)),  # random crops
                # Small gaussian blur with random sigma between 0 and 0.5.
                # But we only blur about 50% of all images.
                iaa.Sometimes(0.5,
                              iaa.GaussianBlur(sigma=(0, 0.5))
                              ),
                # Strengthen or weaken the contrast in each image.
                iaa.ContrastNormalization((0.75, 1.5)),
                # Add gaussian noise.
                # For 50% of all images, we sample the noise once per pixel.
                # For the other 50% of all images, we sample the noise per pixel AND
                # channel. This can change the color (not only brightness) of the
                # pixels.
                iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05 * 255), per_channel=0.5),
                # Make some images brighter and some darker.
                # In 20% of all cases, we sample the multiplier once per channel,
                # which can end up changing the color of the images.
                iaa.Multiply((0.6, 1.4), per_channel=0.2),
                # Apply affine transformations to each image.
                # Scale/zoom them, translate/move them, rotate them and shear them.
                iaa.Affine(
                    scale={"x": (0.5, 1.1), "y": (0.5, 1.2)},
                    translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)},
                    rotate=(-35, 35),
                    shear=(-8, 8)
                )
            ], random_order=True)  # apply augmenters in random order

            seq_deterministic = seq.to_deterministic()
            augimage = seq_deterministic.augment_images([newimage])[0] #augments the image and its bounding box
            boundingaug = seq_deterministic.augment_bounding_boxes([boundingbox])[0]

            if boundingaug.bounding_boxes[0].x1 < 0: #fixes out of bounds bounding boxes
                boundingaug.bounding_boxes[0].x1 = 10

            if boundingaug.bounding_boxes[0].x1 > height:
                boundingaug.bounding_boxes[0].x1 = height-10

            if boundingaug.bounding_boxes[0].x2 < 0:
                boundingaug.bounding_boxes[0].x2 = 10

            if boundingaug.bounding_boxes[0].x2 > height:
                boundingaug.bounding_boxes[0].x2 = height-10


            if boundingaug.bounding_boxes[0].y1 < 0:
                boundingaug.bounding_boxes[0].y1 = 10

            if boundingaug.bounding_boxes[0].y1 > width:
                boundingaug.bounding_boxes[0].y1 = width-10

            if boundingaug.bounding_boxes[0].y2 < 0:
                boundingaug.bounding_boxes[0].y2 = 10

            if boundingaug.bounding_boxes[0].y2 > width:
                boundingaug.bounding_boxes[0].y2 = width-10

            lable = filename #gets the gesture label
            lable = os.path.splitext(lable)[0]  # splits the filename without its extension

            imagearray.append(augimage) #stores the created data for future use
            lablearray.append(lable)

            boundingboxes_arr.append(boundingaug.bounding_boxes[0])



        else:
            x = x-1




print(np.shape(imagearray))
print(np.shape(lablearray))
print(np.shape(boundingboxes_arr))





#randomizes the data


images, lables, boundingboxes = skshuffle(imagearray,lablearray,boundingboxes_arr)



def write_xml(folder, img, objects, tl, br, savedir, filename):


    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    image = cv2.imread(img)
    height, width, depth = image.shape

    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = folder
    ET.SubElement(annotation, 'filename').text = filename
    ET.SubElement(annotation, 'segmented').text = '0'
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)
    for obj, topl, botr in zip(objects, tl, br):
        ob = ET.SubElement(annotation, 'object')
        ET.SubElement(ob, 'name').text = obj
        ET.SubElement(ob, 'pose').text = 'Unspecified'
        ET.SubElement(ob, 'truncated').text = '0'
        ET.SubElement(ob, 'difficult').text = '0'
        bbox = ET.SubElement(ob, 'bndbox')
        ET.SubElement(bbox, 'xmin').text = str(int(topl[0]))
        ET.SubElement(bbox, 'ymin').text = str(int(topl[1]))
        ET.SubElement(bbox, 'xmax').text = str(int(botr[0]))
        ET.SubElement(bbox, 'ymax').text = str(int(botr[1]))

    xml_str = ET.tostring(annotation)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root, pretty_print=True)
    newfilename,_ = os.path.splitext(filename)

    save_path = os.path.join(savedir, newfilename+'.xml')
    with open(save_path, 'wb') as temp_xml:
        temp_xml.write(xml_str)


for index in range(len(lables)): #generating all the required files
    print(index)
    imagename = "image_%07d.jpg" % index #saves image
    lablename = lables[index]
    boundingregion = boundingboxes[index]
    tl = [(boundingregion.x1, boundingregion.y1)]
    br = [(boundingregion.x2, boundingregion.y2)]


    #probability = rand.uniform(0,1)

    imgio.imsave('C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\training\\images\\' + imagename,
                 images[index])

    write_xml(folder='trainingimages',
              img='C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\training\\images\\' + imagename,
              tl=tl, br=br, objects=[lablename], filename=imagename,
              savedir='C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\training\\annotations\\')


#removed data split since darkflow cannot utilize this like darknet can

#    if probability <.75: #75% training data 25% testing data
 #       imgio.imsave('C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\training\\images\\' + imagename, images[index])

  #      write_xml(folder='trainingimages',
   #               img='C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\training\\images\\' + imagename,
     #             tl=tl, br=br, objects = [lablename], filename = imagename,
    #              savedir='C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\training\\annotations\\')
    #else:
     #   imgio.imsave('C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\testing\\images\\' + imagename, images[index])
      #  write_xml(folder='testingimages',
       #           img='C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\testing\\images\\' + imagename,
        #          tl=tl, br=br, objects = [lablename], filename = imagename,
         #         savedir='C:\\Users\\Jesse\\Desktop\\CSE-423-Capstone-Gesture-Recognition\\testing\\annotations\\')


#for x in range(20):

 #   random = randint(0,2000)
  #  print(random)
   # print(lablearray[random])
    #ia.imshow(imagearray[random])
    #bounded_image = boundingboxes_arr[random].draw_on_image(imagearray[random], thickness=2, color=[0, 0, 255])
    #ia.imshow(bounded_image)


#for x in range(20):

 #   random = randint(0,3000)
  #  print(random)
   # print(lables[random])
    #ia.imshow(images[random])
    #bounded_image = boundingboxes[random].draw_on_image(images[random], thickness=2, color=[0, 0, 255])
    #ia.imshow(bounded_image)