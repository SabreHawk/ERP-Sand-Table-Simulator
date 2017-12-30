import pymysql


class ERPSystem(object):
    __local_database_IP = "127.0.0.1"
    __local_user_name = "root"
    __local_user_password = "0000"
    __local_database_name = "ERP_SYSTEM"

    def __init__(self):
        self.__init_database_raw_material_info()

    def __init_database(self):
        pass

    def __init_database_raw_material_info(self):
        erp_db = pymysql.connect(self.__local_database_IP,self.__local_user_name,self.__local_user_password,self.__local_database_name)
        db_cursor = erp_db.cursor()
        sql = """INSERT INTO RAWMATERIAL_INFO(
                  ID, NAME, COST, DELIVERYTIME)
                  VALUES ('1', 'p1', 20, 2)"""
        try:
            db_cursor.execute(sql)
            erp_db.commit()
        except:
            erp_db.rollback()
            erp_db.close()