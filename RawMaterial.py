class RawMaterial(object):

    def __init__(self, in_cost, in_delivery_time, in_quantity = 0):
        self.__cost = in_cost
        self.__deliveryTime = in_delivery_time
        self.__quantity = in_quantity

    def get_cost(self):
        return self.__cost

    def set_cost(self, in_cost):
        self.__cost = in_cost

    def get_delivery_time(self):
        return self.__deliveryTime

    def set_delivery_time(self, in_delivery_time):
        self.__deliveryTime = in_delivery_time

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, in_quantity):
        self.__quantity = in_quantity

    def increase_quantity(self, in_num):
        self.__quantity += in_num

    def decrease_quantity(self, in_num):
        self.__quantity -= in_num
