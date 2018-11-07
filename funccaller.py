from sound import Sound

class caller:
    firstrun = True
    @staticmethod
    def volup():
        Sound.volume_up()


    def call(num):
        if caller.firstrun: #for audio stuff
            Sound.volume_up()
            Sound.volume_set(2)
            caller.firstrun = False
        switch={
            7: caller.volup()
        }
        switch.get(num,"")
