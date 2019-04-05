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

    #use toggle 'modes' to have 3 working gestures, 2 mapped to a command and 1 to switch to a next series of commands
    mode = 0
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


