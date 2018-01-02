class RepositoryManager(object):

    def __init__(self):
        self.__raw_material_repository = []
        self.__production_repository = []

    def __find_raw_material_index(self, in_id):
        for i in range(len(self.__raw_material_repository)):
            if self.__raw_material_repository[i][0] == in_id:
                return i
        return -1

    def __find_production_index(self, in_id):
        for i in range(len(self.__production_repository)):
            if self.__production_repository[i][0] == in_id:
                return i
        return -1

    def add_raw_material(self, in_id, in_num):
        temp_index = self.__find_raw_material_index(in_id)
        if temp_index == -1:
            self.__raw_material_repository.append([in_id, in_num])
        else:
            self.__raw_material_repository[temp_index][1] += in_num
        return True

    def delete_raw_material_(self, in_id, in_num):
        temp_index = self.__find_raw_material_index(in_id)
        if temp_index == -1:
            return False
        else:
            self.__raw_material_repository[temp_index][1] -= in_num
            if self.__raw_material_repository[temp_index][1] <= 0:
                self.__raw_material_repository.pop(temp_index)
        return True

    def add_production(self, in_id, in_num):
        temp_index = self.__find_production_index(in_id)
        if temp_index == -1:
            self.__production_repository.append([in_id, in_num])
        else:
            self.__production_repository[temp_index][1] += in_num
        return True

    def delete_production(self, in_id, in_num):
        temp_index = self.__find_production_index(in_id)
        if temp_index == -1:
            return False
        else:
            self.__production_repository[temp_index][1] -= in_num
            if self.__production_repository[temp_index][1] <= 0:
                self.__production_repository.pop(temp_index)
        return True
