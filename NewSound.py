from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

i = 1
#Based in Decibels
#Base value of -40 dBs
#Should find a way to set to current value
#Currently set to -30 so it doesnt max like previous
current = -30
#While loop for testing
while i == 1:
    #Change is in + - x dB
    x = int(input("Volume Change: "))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    current = current + x
    volume.SetMasterVolumeLevel(current , None)