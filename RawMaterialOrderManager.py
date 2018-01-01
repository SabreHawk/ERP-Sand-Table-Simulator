import ERPDate
import RawMaterialOrder


class RawMaterialOrderManager(object):
    def __init(self):
        self.__raw_material_order_list = []

    def add_raw_material_order(self, in_raw_material_order):
        if isinstance(in_raw_material_order, RawMaterialOrder.RawMaterialOrder):
            self.__raw_material_order_list.append(in_raw_material_order)

