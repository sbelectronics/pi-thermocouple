class DummyMax31855:
    def __init__(self):
        pass

    @property
    def externalF(self):
       return 12

    @property
    def internalF(self):
       return 34


Thermocouple = None
def startup(noHardware=False):
    global Thermocouple
    if noHardware:
        Thermocouple = DummyMax31855()
    else:
        from max31855 import Max31855

        Thermocouple = Max31855(0,0)

