import win32.win32api as win32api
from textinput import volup_home
from textinput import voldown_home
from textinput import plug_on
from textinput import plug_off

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


# Google Home
# Functions have a tendancy to forcefully exit when called
# I don't know why but this makes it non ideal as it will close the program
# Wasn't able to pass input to the main function so opted on creating a function for each
# Only was able to get the volume control working, there is device control the specific device needs to be mentioned
# Volume control = volup_home and voldown_home
# Plug control controls device named "plug" can be renamed to control any device plug_on plug_off


class caller:

    #use toggle 'modes' to have 3 working gestures, 2 mapped to a command and 1 to switch to a next series of commands
    def call(self, label): #gibrish text is a placeholder
        if self.mode == 0:
           if label=="ok_gesture":
               self.mode += 1

           elif label == "point_up":
               win32api.keybd_event(VolUp, 48)

           elif label == "rock_and_roll":
               win32api.keybd_event(VolDown, 49)

        elif self.mode == 1:
            if label == "ok_gesture":
                self.mode += 1

            elif label == "point_up":
                win32api.keybd_event(NextTrack, 25)

            elif label == "rock_and_roll":
                win32api.keybd_event(PrevTrack, 16)

        elif self.mode == 2:
            if label == "ok_gesture":
                self.mode = 0
            elif label == "point_up":
                win32api.keybd_event(PlayPauseMedia, 34)

            elif label == "rock_and_roll":
                print("")

        #elif self.mode == 3:
        #    if label == "ok_gesture":
        #        self.mode =
        #    elif label == "point_up":
        #        volup_home()
        #
        #    elif label == "rock_and_roll":
        #        volup_home()



