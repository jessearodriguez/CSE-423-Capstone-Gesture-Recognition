from sound import Sound
import time
#Test file for volume test, using existing Sound Module

#Note first call from the sound module will max out volume
#Compensate by setting volume
#Currently trying to create a new sound module

Sound.volume_down()
Sound.volume_set(20)
time.sleep(2)
Sound.volume_min()
time.sleep(2)
Sound.volume_set(40)
time.sleep(2)
Sound.volume_set(60)
time.sleep(2)
Sound.volume_set(80)
time.sleep(2)
Sound.volume_set(2)


