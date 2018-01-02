import ERPDate


class RawMaterialOrder(object):

    def __init__(self, in_id, in_name, in_raw_material_id, in_num, in_delivery_time, in_date):
        self.__id = in_id
        self.__name = in_name
        self.__raw_material_id = in_raw_material_id
        self.__number = in_num
        self.__delivery_time = in_delivery_time
        if isinstance(in_date, ERPDate.ERPDate):
            self.__order_date = in_date
        else:
            self.__order_date = ERPDate.ERPDate(in_date[0], in_date[2])
        self.__arrival_date = self.__order_date.add_date(in_delivery_time)

    def get_attributes(self):
        return self.__id, self.__name, self.__raw_material_id, self.__number, self.__delivery_time, self.__order_date.to_string(), self.__arrival_date.to_string()

    def get_id(self):
        return self.__id

    def set_id(self, in_id):
        self.__id = in_id

    def get_name(self):
        return self.__name

    def set_name(self, in_name):
        self.__name = in_name

    def get_raw_material_id(self):
        return self.__raw_material_id

    def set_raw_material_id(self, in_id):
        self.__raw_material_id = in_id

    def get_delivery_time(self):
        return self.__delivery_time

    def set_delivery_time(self, in_time):
        self.__delivery_time = in_time

    def get_order_date(self):
        return self.__order_date

    def set_order_date(self, in_date):
        self.__order_date = in_date

    def get_arrival_date(self):
        return self.__arrival_date

    def display_info(self):
        print("<Object Type : RawMaterialOrder")
        print("Name : %s" % self.__name)
        print("order_date : ")
        self.__order_date.display_info()
        print("raw_material_id : %s" % self.__raw_material_id)
