from Production import *
from RawMaterial import *


class Repository(object):
    __production_list = []
    __raw_material_list = []

    def __init__(self, in_max_production_capacity, in_max_raw_material_capacity):
        self.__max_production_capacity = in_max_production_capacity
        self.__max_raw_material_capacity = in_max_raw_material_capacity
        self.__utilized_production_capacity = 0
        self.__utilized_raw_material_capacity = 0

    def append_production(self, in_production_id):
        if isinstance(in_production, Production) and self.__utilized_production_capacity < self.__max_production_capacity:
            self.__production_list.append(in_production)
            self.__utilized_production_capacity += 1
            return True
        else:
            return False

    def erase_production(self, in_production_id):
    def get_max_production_capacity(self):
        return self.__max_production_capacity

    def get_utilized_production_capacity(self):
        return self.__utilized_production_capacity

    def append_raw_material(self, in_raw_material):
        if isinstance(in_raw_material, RawMaterial) and self.__utilized_raw_material_capacity < self.__max_production_capacity:
            self.__raw_material_list.append(in_raw_material)
            self.__utilized_raw_material_capacity += 1
            return True
        else:
            return False

    def get_max_raw_material_capacity(self):
        return self.__max_raw_material_capacity

    def get_utilized_raw_material_capacity(self):
        return self.__utilized_raw_material_capacity

