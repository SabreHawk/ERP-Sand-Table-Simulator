import pymysql
import ERPDate
import RawMaterial
import RawMaterialOrder
import RawMaterialOrderManager
import User
import DatabaseManager


class ERPSystem(object):

    def __init__(self):
        self.__active_user_list = []
        self.__sys_data = ERPDate.ERPDate(1, 1)
        self.__raw_material_order_manager = RawMaterialOrderManager.RawMaterialOrderManager()
        self.__database_manager = DatabaseManager.DatabaseManager()
        self.__init_system()

    def __init_system(self):
        self.__init_root_user()
        self.__init_database()

    def __init_root_user(self):
        root_user = User.User('root', '0000')
        self.__active_user_list.append(root_user)

    def __init_database(self):
        pass

    def test_main(self):
        self.sys_add_raw_material_info('4', 'R4', 3, 8)
        self.sys_add_raw_material_order(6, 4, 2)

    def sys_add_raw_material_info(self, in_id, in_name, in_cost, in_delivery_time):
        self.__database_manager.insert__raw_material_info(in_id, in_name, in_cost, in_delivery_time)

    def sys_add_raw_material_order(self, in_order_id, in_raw_material_id, in_num):
        temp_delivery_time = self.__database_manager.query_raw_material_info(in_raw_material_id)[0][3]
        temp_raw_material_order = RawMaterialOrder.RawMaterialOrder(in_order_id, 'testOrder', in_raw_material_id,
                                                                    in_num, temp_delivery_time, self.__sys_data)
        self.__raw_material_order_manager.add_raw_material_order(temp_raw_material_order)
        self.__database_manager.insert_raw_material_order(temp_raw_material_order)

    def sys_add_raw_material_repository(self,id_material,in_num):

