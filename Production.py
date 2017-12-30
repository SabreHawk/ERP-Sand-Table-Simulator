from RawMaterial import *


class Production(object):
    __raw_material_sheet = [] # Store The ID Of The Raw Material Which Contains Count

    def __init__(self):
        self.ID = 0
        self.__quantity = 0

    def increase_quantity(self, in_num):
        self.__quantity += in_num

    def decrease_quantity(self, in_num):
        self.__quantity -= in_num

    def append_raw_material(self, in_raw_material):
        if isinstance(in_raw_material, RawMaterial) and in_raw_material not in self.__raw_material_sheet:
            self.__raw_material_sheet.append(in_raw_material)
            return True
        else:
            return False

    def erase_raw_material(self, in_raw_material_id):
        if in_raw_material_id < len(self.__raw_material_sheet):
            self.__raw_material_sheet.pop(in_raw_material_id)
            return True
        else:
            return False



