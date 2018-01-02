import pymysql
import ERPDate
import User
import RawMaterial
import RawMaterialOrder
import RawMaterialOrderManager
import DatabaseManager
import RepositoryManager


class ERPSystem(object):

    def __init__(self):
        self.__active_user_list = []
        self.__sys_data = ERPDate.ERPDate(1, 1)
        self.__raw_material_order_manager = RawMaterialOrderManager.RawMaterialOrderManager()
        self.__repository_manager = RepositoryManager.RepositoryManager()

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
        print(self.sys_query_production_repository(2))
        self.sys_produce(2, 2)
        print(self.sys_query_production_repository(2))

    def sys_add_raw_material_info(self, in_id, in_name, in_cost, in_delivery_time):
        self.__database_manager.insert_raw_material_info(in_id, in_name, in_cost, in_delivery_time)

    def sys_add_raw_material_order(self, in_order_id, in_raw_material_id, in_num):

        temp_delivery_time = self.__database_manager.query_raw_material_info(in_raw_material_id)[0][3]

        temp_raw_material_order = RawMaterialOrder.RawMaterialOrder(in_order_id, 'testOrder', in_raw_material_id,
                                                                    in_num, temp_delivery_time, self.__sys_data)
        # self.__raw_material_order_manager.add_raw_material_order(temp_raw_material_order)

        self.__database_manager.insert_raw_material_order(temp_raw_material_order)

    def sys_update_raw_material_repository(self, in_id, in_num):
        self.__database_manager.update_raw_material_repository(in_id, in_num)

    def sys_update_production_repository(self, in_id, in_num):
        self.__database_manager.update_production_repository(in_id, in_num)

    def sys_query_raw_material_info(self, in_id):
        return self.__database_manager.query_raw_material_info(in_id)

    def sys_query_raw_material_order(self, in_id):
        return self.__database_manager.query_raw_material_order(in_id)

    def sys_query_raw_material_repository(self, in_id):
        return self.__database_manager.query_raw_material_repository(in_id)

    def sys_query_production_info(self, in_id):
        return self.__database_manager.query_production_info(in_id)

    def sys_query_production_repository(self, in_id):
        return self.__database_manager.query_production_repository(in_id)

    def sys_get_raw_material_category_total_num(self):
        return int(self.__database_manager.query_raw_material_category_total_num()[0][0])

    def sys_get_raw_material_category_remain_num(self):
        return int(self.__database_manager.query_raw_material_category_remain_num()[0][0])

    def sys_produce(self, in_id, in_num):
        rm_total_num = self.sys_get_raw_material_category_total_num()
        rm_remain_num = self.sys_get_raw_material_category_remain_num()
        rm_required_num = [0] * rm_total_num
        for info in analyze_production_info(self.sys_query_production_info(in_id)[0]):
            rm_required_num[int(info[0])] += (int(info[1]) * in_num)
        rm_stored_num = [0] * rm_total_num

        for i in range(rm_remain_num):
            rm_stored_num[i] = self.sys_query_raw_material_repository(i)[0][1]
        for i in range(rm_total_num):
            if rm_required_num[i] - rm_stored_num[i] > 0:
                return False
        for i in range(rm_total_num):
            self.sys_update_raw_material_repository(i, -1 * rm_required_num[i])
        self.sys_update_production_repository(in_id, in_num)


def analyze_production_info(in_tuple):
    temp_info = in_tuple[2].split('/')
    results = []
    for s in temp_info:
        results.append((s[0], s[2]))
    return results
