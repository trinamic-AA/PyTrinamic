from PyTrinamic.features.Feature import Feature

class FeatureProvider(Feature):
    def __init__(self, axis):
        self.__axis = axis
    def getAxis(self):
        return self.__axis
    def setAxis(self, axis):
        self.__axis = axis