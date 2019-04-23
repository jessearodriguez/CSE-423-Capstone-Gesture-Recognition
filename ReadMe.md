### Setup instructions:

For setup purposes, I recommend creating two different conda 3.6 environments; one will be for dataset generation and another will be for actually training and running the program.


#### Dataset generator env setup:
The purpose of this environment is to generate the data set that will be used to train the neural net later on. This also required the following external downloads:
- Describable Textures Dataset: [[Link]][1] - Used to fill out backgrounds for more robust training images

The following python modules should be installed inside of the conda environment defined for this task:
- Pre-requisites - `pip install six numpy scipy Pillow matplotlib scikit-image opencv-python imageio Shapely`
-  Imgaug - can be installed via `pip install imgaug`
- scikit-learn - can be installed via `conda install scikit-learn`
- lxml - can be installed via `pip install lxml`

After installing the modules, extract and drop the describable textures dataset into the parent capstone folder alongside modifying the paths used inside the file. Once those are done, the code should be run and it will generate and augment the base included images and output roughly 35k images for training alongside their annotations. 

The dataset can also be pre-downloaded here [[Link]][2]

#### Training/running env setup
In a new conda environemnt, the following moduels and pre-requisites are needed to successfuly train and run the program.
- c++ build tools [[Link]][4]
- darkflow [[Link]][3]
- opencv - can be installed via `conda install opencv`
- tensorflow - should be installed via `conda install tensorflow` or if you have a compatible GPU `conda install tensorflow-gpu`
- cython - can be installed via `conda install cython`
- pywemo - can be installed via `pip install pywemo`
- win32api - can be installed via `pip install pywin32`

Training from scratch information can be found in the darkflow link listed above; the pre-trained weights used for this program can be found here [[Link]][5]. After installing, drop it into the already created ckpt/ folder. 

At this point, the mainv2.py should be able to be run.


[1]: https://www.robots.ox.ac.uk/~vgg/data/dtd/
[2]: https://drive.google.com/open?id=1X55D_BYsIAp7QoyG6ev2i2eJKxtEL7gx
[3]: https://github.com/thtrieu/darkflow
[4]: https://download.microsoft.com/download/5/f/7/5f7acaeb-8363-451f-9425-68a90f98b238/visualcppbuildtools_full.exe?fixForIE=.exe
[5]: http://drive.google.com/file/d/1JICbL_1BevMWTBNLowmjLNYCMND1Fx5n/view?usp=sharing