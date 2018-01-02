import ERPDate
import RawMaterialOrder


class RawMaterialOrderManager(object):

    def __init__(self):
        self.__raw_material_order_list = []

    def add_raw_material_order(self, in_raw_material_order):
        if isinstance(in_raw_material_order, RawMaterialOrder.RawMaterialOrder):
            self.__raw_material_order_list.append(in_raw_material_order)
            return True
        else:
            return False

    def commit_raw_material_order(self, in_id):
        for i in range(len(self.__raw_material_order_list)):
            if self.__raw_material_order_list[i].get_id() == in_id:
                self.__raw_material_order_list.pop(i)
                return True
            else:
                return False

    def display__info(self):
        for order in self.__raw_material_order_list:
            order.display_info()
