from sound import Sound
import win32api

NextTrack = 0xB0            #25
PrevTrack = 0xB1            #16
PlayPauseMedia = 0xB3       #34
VolUp = 0xAF                #48
VolDown = 0xAE              #49
MuteSound = 0xAD            #32



class caller:

    def call(num):
       if num==6: #thumbs up
           win32api.keybd_event(PlayPauseMedia, 34)
       elif num ==2: #point up
           win32api.keybd_event(NextTrack, 25)
       elif num ==5: #open hand
           win32api.keybd_event(PrevTrack, 16)
       elif num ==4: #3 fingers
           win32api.keybd_event(VolUp, 48)
       elif num ==3:#2 fingers
           win32api.keybd_event(VolDown, 49)
