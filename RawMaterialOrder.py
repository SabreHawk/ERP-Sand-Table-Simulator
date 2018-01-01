import ERPDate


class RawMaterialOrder(object):

    def __init__(self, in_raw_material, in_date):
        self.__raw_material = in_raw_material
        self.__order_date = in_date
        self.__arrival_date = self.__order_date.add_date(self.__raw_material.getDeliveryTime())


