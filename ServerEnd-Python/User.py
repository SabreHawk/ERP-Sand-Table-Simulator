class User(object):
    
    def __init__(self, in_name, in_password):
        self.__user_name = in_name
        self.__user_password = in_password
        self.__permission_sheet = {'root': 1, 'purchase': 1, 'order': 1, 'produce': 1}

    def check_permission(self, in_permission_name):
        if in_permission_name in self.__permission_sheet and self.__permission_sheet[in_permission_name] == 1:
            return True
        else:
            return False

    def set_permission(self, in_permission_name, in_bool):
        if in_bool is True:
            self.__permission_sheet[in_permission_name] = in_bool
            return True
        else:
            return False

    def set_new_raw_material_info(self):
        pass

    def place_raw_material_order(self,in_raw_material_type_id,in_num):
        pass
