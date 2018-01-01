import ERPDate


class RawMaterialOrder(object):

    def __init__(self, in_name, in_raw_material_id, in_delivery_time, in_num, in_date):
        self.__order_name = in_name
        self.__raw_material_id = in_raw_material_id
        self.__number = in_num
        self.__delivery_time = in_delivery_time
        self.__order_date = in_date
        self.__arrival_date = self.__order_date.add_date(in_delivery_time)

    def display_info(self):
        print("<Object Type : RawMaterialOrder")
        print("Name : %s" % self.__order_name)
        print("order_date : ")
        self.__order_date.display_info()
        print("raw_material_id : %s" % self.__raw_material_id)
