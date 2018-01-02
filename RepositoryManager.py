class RepositoryManager(object):

    def __init__(self):
        self.__raw_material_repository = []
        self.__production_repository = []

    def add_raw_material(self, in_id, in_num):
        for i in range(len(self.__raw_material_repository)):
           if self.__raw_material_repository[i][0] == in_id:
                self.__raw_material_repository[i][1] += in_num
                break
        self.__raw_material_repository.append([in_id,in_num])
        return True

    def delete_raw_material_(self,in_id,in_num,):
        for i in range(len(self.__raw_material_repository)):
            if self.__raw_material_repository[i][0] == in_id:
                self.__raw_material_repository[i][1] -= in_num
                if self.__raw_material_repository[i][1] < 0:
                    self.__raw_material_repository[i][1] = 0
                return True
        return False

    def add_production(self,in_id,in_num):
        for i in range(len(self.__production_repository)):
            if (self.__production_repository[i][0] == )

