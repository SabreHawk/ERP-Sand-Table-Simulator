import pymysql
import random
import ERPDate
import RawMaterialOrder


class DatabaseManager(object):
    __local_database_IP = "127.0.0.1"
    __local_user_name = "root"
    __local_user_password = "0000"
    __local_database_name = "ERP_SYSTEM"

    def __init__(self):
        self.__erp_db = pymysql.connect(self.__local_database_IP, self.__local_user_name, self.__local_user_password, self.__local_database_name)
        self.__db_cursor = self.__erp_db.cursor()
        self.__db_sql = ""

        self.__init_raw_material_info_table()
        self.__init_raw_material_order_table()
        pass

    # Init Database Tables And Data
    def __init_raw_material_info_table(self):
        self.__create_raw_material_info_table()
        self.__insert_raw_material_info_data()

    def __init_raw_material_order_table(self):
        self.__create_raw_material_order_table()
        self.__insert_raw_material_order_data()

    def __create_raw_material_order_table(self):
        self.__db_sql = """CREATE TABLE IF NOT EXISTS RAWMATERIAL_ORDER(
                            ID VARCHAR(20) PRIMARY KEY,
                            NAME VARCHAR(20) NOT NULL,
                            RAWMATERIAL_ID VARCHAR(20) NOT NULL,
                            QUANTITY INT NOT NULL,
                            DELIVERYTIME INT NOT NULL,
                            ORDER_DATE VARCHAR(20) NOT NULL,
                            ARRIVAL_DATE VARCHAR(20) NOT NULL)"""
        self.__db_cursor.execute(self.__db_sql)

    def __insert_raw_material_order_data(self):
        params = []
        self.__db_sql = """DELETE FROM RAWMATERIAL_ORDER"""
        try:
            self.__db_cursor.execute(self.__db_sql)
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

        self.__db_sql = """INSERT INTO RAWMATERIAL_ORDER
                                VALUES (%s,%s,%s,%s,%s,%s,%s)
                                """
        for i in range(5):
            params.append((str(i), 'order'+str(i), '2', int(random.randint(1, i*3+2)), int(2), '1-1', '1-3'))

        try:
            self.__db_cursor.executemany(self.__db_sql, params)
            self.__erp_db.commit()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def __create_raw_material_info_table(self):
        self.__db_sql = """CREATE TABLE IF NOT EXISTS RAWMATERIAL_INFO(
                            ID VARCHAR(20) PRIMARY KEY,
                            NAME VARCHAR(20) NOT NULL,
                            COST FLOAT NOT NULL,
                            DELIVERYTIME INT NOT NULL)"""

        self.__db_cursor.execute(self.__db_sql)

    def __insert_raw_material_info_data(self):
        params = []
        self.__db_sql = """DELETE FROM RAWMATERIAL_INFO """
        try:
            self.__db_cursor.execute(self.__db_sql)
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

        self.__db_sql = """INSERT INTO RAWMATERIAL_INFO
                            VALUES (%s,%s, %s, %s)"""
        for i in range(4):
            params.append((i, 'R' + str(i), str(i * 10), int(random.randint(1, 5))))

        try:
            self.__db_cursor.executemany(self.__db_sql, params)
            self.__erp_db.commit()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))


    def __add_raw_material_info_data(self):
        pass

    def __raw_material_info_query(self):
        self.__db_sql = """SELECT * FROM RAWMATERIAL_INFO"""
        try:
            self.__db_cursor.execute(self.__db_sql)
            query_result = self.__db_cursor.fetchall()
            for results in query_result:
                print(results)

        except pymysql.DatabaseError as error:
            print("Error: {}".format(error.args))
            self.__erp_db.rollback()

    def __init_table_raw_material_order(self):
        pass


    def insert_raw_material_order(self, in_raw_material_order):
        self.__db_sql = """INSERT INTO RAWMATERIAL_INFO"""

    def query_raw_material_info(self, in_raw_material_id):
        self.__db_sql = """SELECT * FROM RAWMATERIAL_INFO WHERE ID = %s"""
        try:
            self.__db_cursor.execute(self.__db_sql, str(in_raw_material_id))
            return self.__db_cursor.fetchall()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def close_database(self):
        self.__erp_db.close()

    def __execute_sql(self):
        try:
            self.__db_cursor.execute(self.__db_sql)
            self.__erp_db.commit()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

