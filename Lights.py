class Lights:
    lights = 0

    """""
    Function
    To return the light value the light
    """
    @staticmethod
    def isOpen():
        if(lights == 1):
            return true
        else:
            return false


    """""
    Function
    To toggle the light
    """
    @staticmethod
    def toggle():
        if(lights == 1):
            lights = 0
        else:
            lights = 1


    #Getters and setters
    def getLight(self):
        return light

    def setLights(self, x):
        light = x


