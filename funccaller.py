from sound import Sound
import win32.win32api as win32api

NextTrack = 0xB0            #25
PrevTrack = 0xB1            #16
PlayPauseMedia = 0xB3       #34
VolUp = 0xAF                #48
VolDown = 0xAE              #49
MuteSound = 0xAD            #32


# ALL GESTURES ARE FINIKY IN THEIR DETECTIONS, CURRENTLY UNAVOUDABLE DUE TO TINY YOLO, YOLOV3 NEEDS BETTER HARDWARE
# 3 fingers works at some positions
# camera gesture same as above, harder to do
# closed hand contests with point up for some reason
# handgun works with like 60% detection rate
# ok gesture works
# peace gesture contests too much with point up, <10% detection rate
# point up works
# rock and roll works
# stop gesture contends with rock and roll, 15~% detection rate
# thumbs up works at certain angles
# thumbs down not working at all

class caller:

    def call(label): #gibrish text is a placeholder
       if label=="febjafndafeafds":
           win32api.keybd_event(PlayPauseMedia, 34)
       elif label =="feadfafesfed": #point up
           win32api.keybd_event(NextTrack, 25)
       elif label =="fadeaffdaf": #open hand
           win32api.keybd_event(PrevTrack, 16)
       elif label =="point_up": #3 fingers
           win32api.keybd_event(VolUp, 48)
       elif label =="rock_and_roll":#2 fingers
           win32api.keybd_event(VolDown, 49)
