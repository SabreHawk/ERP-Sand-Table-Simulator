import DatabaseManager
import ERPDate
import RawMaterialOrder
import RawMaterialOrderManager
import RepositoryManager
import User
import socket


class ERPSystem(object):

    def __init__(self):
        self.__active_user_list = []
        self.__sys_data = ERPDate.ERPDate(1, 1)
        self.__raw_material_order_manager = RawMaterialOrderManager.RawMaterialOrderManager()
        self.__repository_manager = RepositoryManager.RepositoryManager()
        self.__database_manager = DatabaseManager.DatabaseManager()
        self.__request_msg = []
        self.__fcn_dic = []
        self.__init_system()

    def __init_system(self):
        self.__init_root_user()
        self.__init_function_dic()
        self.__sys_network_monitor()

    def __init_root_user(self):
        root_user = User.User('root', 'root')
        self.__active_user_list.append(root_user)

    def __init_function_dic(self):
        self.__fcn_dic = ['sys_add_raw_material_info', 'sys_add_raw_material_order',
                          'sys_update_raw_material_repository',
                          'sys_update_production_repository', 'sys_query_raw_material_info',
                          'sys_query_raw_material_order'
                          'sys_query_raw_material_repository', 'sys_query_production_info',
                          'sys_query_production_repository'
                          'sys_query_production_order', 'sys_get_raw_material_category_total_num',
                          'sys_get_raw_material_category_remain_num'
                          'sys_produce', 'sys_commit_production_order', 'sys_login']

    def test_main(self):
        print(self.__sys_request_manager('sys_login "root" "root"'))

    def __sys_network_monitor(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host_ip = '45.77.121.117'
        port = 1830
        server_socket.bind((host_ip, port))
        server_socket.listen(5)
        while True:
            (client_socket, address) = server_socket.accept()
            request_msg = client_socket.recv(1024).decode('utf-8')
            return_msg = self.__sys_request_manager(request_msg)
            client_socket.send(return_msg.encode('utf-8'))
            client_socket.close()

    def __sys_request_manager(self, in_msg):
        in_msg = in_msg.split()
        fcn_name = in_msg[0]
        fcn_params = in_msg[1:]
        call_fcn_cmd = 'self.' + fcn_name + '(' + ','.join(fcn_params) + ')'
        try:
            return eval(call_fcn_cmd)
        except Exception:
            return str(False)

    def sys_login(self, in_name, in_passwd):
        return str(self.__database_manager.query_account_info(in_name)[0][1] == in_passwd)

    def sys_add_raw_material_info(self, in_id, in_name, in_cost, in_delivery_time):
        return str(self.__database_manager.insert_raw_material_info(in_id, in_name, in_cost, in_delivery_time))

    def sys_add_raw_material_order(self, in_order_id, in_raw_material_id, in_num):
        temp_delivery_time = self.__database_manager.query_raw_material_info(in_raw_material_id)[0][3]
        temp_raw_material_order = RawMaterialOrder.RawMaterialOrder(in_order_id, 'testOrder', in_raw_material_id,
                                                                    in_num, temp_delivery_time, self.__sys_data)
        return str(self.__database_manager.insert_raw_material_order(temp_raw_material_order))

    def sys_update_raw_material_repository(self, in_id, in_num):
        return str(self.__database_manager.update_raw_material_repository(in_id, in_num))

    def sys_update_production_repository(self, in_id, in_num):
        return str(self.__database_manager.update_production_repository(in_id, in_num))

    def sys_query_raw_material_info(self, in_id):
        result = self.__database_manager.query_raw_material_info(in_id)
        if result is False:
            return str(result)
        else:
            return 'True '+' '.join(map(str, result[0]))

    def sys_query_raw_material_order(self, in_id):
        result = self.__database_manager.query_raw_material_order(in_id)
        if result is False:
            return str(result)
        else:
            return 'True '+' '.join(map(str, result[0]))

    def sys_query_raw_material_repository(self, in_id):
        result = self.__database_manager.query_raw_material_repository(in_id)
        if result is False:
            return str(result)
        else:
            return 'True '+' '.join(map(str, result[0]))

    def sys_query_production_info(self, in_id):
        result = self.__database_manager.query_production_info(in_id)
        if result is False:
            return str(result)
        else:
            return 'True '+' '.join(map(str, result[0]))

    def sys_query_production_repository(self, in_id):
        result = self.__database_manager.query_production_repository(in_id)
        if result is False:
            return str(result)
        else:
            return 'True '+' '.join(map(str, result[0]))

    def sys_query_production_order(self, in_id):
        result = self.__database_manager.query_production_order(in_id)
        if result is False:
            return str(result)
        else:
            return 'True '+' '.join(map(str, result[0]))

    def sys_get_raw_material_category_total_num(self):
        return str(self.__database_manager.query_raw_material_category_total_num()[0][0])

    def sys_get_raw_material_category_remain_num(self):
        return str(self.__database_manager.query_raw_material_category_remain_num()[0][0])

    def sys_produce(self, in_id, in_num):
        rm_total_num = int(self.sys_get_raw_material_category_total_num())
        rm_remain_num = int(self.sys_get_raw_material_category_remain_num())
        rm_required_num = [0] * rm_total_num
        for info in analyze_production_info(self.sys_query_production_info(in_id)[0]):
            rm_required_num[int(info[0])] += (int(info[1]) * in_num)
        rm_stored_num = [0] * rm_total_num

        for i in range(rm_remain_num):
            rm_stored_num[i] = self.sys_query_raw_material_repository(i)[0][1]
        for i in range(rm_total_num):
            if rm_required_num[i] - rm_stored_num[i] > 0:
                return str(False)
        for i in range(rm_total_num):
            self.sys_update_raw_material_repository(i, -1 * rm_required_num[i])
        return self.sys_update_production_repository(in_id, in_num)

    def sys_commit_production_order(self, in_id):
        temp_result = self.__database_manager.query_production_order(in_id)
        p_order_id = temp_result[0][2]
        p_order_quantity = temp_result[0][3]
        p_stored_quantity = self.__database_manager.query_production_repository(p_order_id)[0][1]
        if p_stored_quantity >= p_order_quantity:
            self.__database_manager.update_production_repository(p_order_id, -1 * p_order_quantity)
            self.__database_manager.update_production_order(in_id, 1)
            return str(True)
        else:
            return str(False)


def analyze_production_info(in_tuple):
    temp_info = in_tuple[2].split('/')
    results = []
    for s in temp_info:
        results.append((s[0], s[2]))
    return results


def analyze_request(in_request):
    try:
        return in_request.split()
    except Exception:
        return str(False)
