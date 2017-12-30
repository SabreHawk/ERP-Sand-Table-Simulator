import pymysql


class DatabaseManager(object):
    __local_database_IP = "127.0.0.1"
    __local_user_name = "root"
    __local_user_password = "0000"
    __local_database_name = "ERP_SYSTEM"

    def __init__(self):
        self.__erp_db = pymysql.connect(self.__local_database_IP, self.__local_user_name, self.__local_user_password,
                                 self.__local_database_name)
        self.__db_cursor = self.__erp_db.cursor()
        pass


    def init_database_raw_material_info(self):
        params = []
        sql = """DELETE FROM RAWMATERIAL_INFO """
        try:
            self.__db_cursor.execute(sql)
        except pymysql.connections.err as error:
            print("Error: {}".format(error.msg))
            self.__erp_db.rollback()

        for i in range(4):
            sql = """INSERT INTO RAWMATERIAL_INFO(
                  ID, NAME, COST, DELIVERYTIME)
                  VALUES (%s,%s, %s, %s)"""
            params.append((i, 'p' + str(i), str(i * 10), str(i + 3)))

        try:
            self.__db_cursor.executemany(sql, params)
            self.__erp_db.commit()
        except pymysql.connections.err as error:
            print("Error: {}".format(error.msg))
            self.__erp_db.rollback()

    def testQuery(self):
        sql = """SELECT * FROM RAWMATERIAL_INFO"""
        try:
            self.__db_cursor.execute(sql)
            query_result = self.__db_cursor.fetchall()
            for results in query_result:
                print(results)

        except pymysql.connections.err as error:
            print("Error: {}".format(error.msg))
            self.__erp_db.rollback()

    def close_database(self):
        self.__erp_db.close()


