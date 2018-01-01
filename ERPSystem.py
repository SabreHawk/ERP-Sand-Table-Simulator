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
        pass


    def sys_add_raw_material_order(self, in_raw_material_id, in_num, in_date):
        temp_delivery_time = self.__database_manager.query_raw_material_info(in_raw_material_id)[3]
        temp_raw_material_order = RawMaterialOrder.RawMaterialOrder('testOrder', in_raw_material_id, in_num, in_date)
        self.__raw_material_order_manager.add_raw_material_order(temp_raw_material_order)
       # self.__database_manager.add