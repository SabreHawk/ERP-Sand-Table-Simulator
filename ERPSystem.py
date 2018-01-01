import pymysql
import ERPDate
import User
import DatabaseManager


class ERPSystem(object):
    
    def __init__(self):
        self.__active_user_list = []
        self.__sys_data = ERPDate.ERPDate(1,1)
        self.__database_manager = DatabaseManager.DatabaseManager()
        self.__init_system()

    def __init_system(self):
        self.__init_root_user()
        self.__init_database()

    def __init_root_user(self):
        root_user = User.Ueer('root', '0000')
        self.__active_user_list.append(root_user)
        
    def __init_database(self):
        pass


