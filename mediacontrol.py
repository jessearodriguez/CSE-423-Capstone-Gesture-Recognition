import win32api
#Was confused because win32api needs to be downloaded as pypiwin32
#use pip install pypiwin32
#Scan Code                  Hardware Code
NextTrack = 0xB0            #25
PrevTrack = 0xB1            #16
PlayPauseMedia = 0xB3       #34
VolUp = 0xAF                #48
VolDown = 0xAE              #49
MuteSound = 0xAD            #32

#For getting the Hardware Code
hwcode = win32api.MapVirtualKey(VolDown,0)
print(f'Hardware Code: {hwcode}')


#Just simple interface
def controlMedia(a):
    if a == 'a':
        win32api.keybd_event(PlayPauseMedia, 34)
    if a == 'b':
        win32api.keybd_event(NextTrack,25)
    if a == 'c':
        win32api.keybd_event(PrevTrack,16)
    if a == 'd':
        win32api.keybd_event(VolUp,48)
    if a == 'e':
        win32api.keybd_event(VolDown, 49)
    if a == 'f':
        win32api.keybd_event(MuteSound,32)

while True:
    b = input("a:Play/Pause Media\nb:Next Track\nc:Prev Track\nd:VolUp\ne:VolDown\nf:MuteSound\n")
    controlMedia(b)