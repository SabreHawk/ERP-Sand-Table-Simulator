class RawMaterial(object):
    __category = 0

    def __init__(self, in_category, in_cost, in_delivery_period):
        self.__category = in_category
        self.__cost = in_cost
        self.__in_delivery_period = in_delivery_period

    def printInfo(self):
        print(self.__category)