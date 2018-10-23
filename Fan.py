class Fan:
    fan = 0

    """""
    Function
    To return the light value the light
    """
    @staticmethod
    def isOpen():
        if(fan == 1):
            return true
        else:
            return false


    """""
    Function
    To toggle the light
    """
    @staticmethod
    def toggle():
        if(fan == 1):
            fan = 0
        else:
            fan = 1

