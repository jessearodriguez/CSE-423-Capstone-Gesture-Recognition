import win32api
#Was confused because win32api needs to be downloaded as pypiwin32
#use pip install pypiwin32
#Scan Code                  Hardware Code
NextTrack = 0xB0            #25
PrevTrack = 0xB1            #16
PlayPauseMedia = 0xB3       #34

#For getting the Hardware Code
#hwcode = win32api.MapVirtualKey(StopMedia,0)
#print(f'Hardware Code: {hwcode}')


#Just simple interface
def controlMedia(a):
    if a == 'a':
        win32api.keybd_event(PlayPauseMedia, 34)
    if a == 'b':
        win32api.keybd_event(NextTrack,25)
    if a == 'c':
        win32api.keybd_event(PrevTrack,16)


while True:
    b = input("a:Play/Pause Media\nb:Next Track\nc:Prev Track\n\n")
    controlMedia(b)