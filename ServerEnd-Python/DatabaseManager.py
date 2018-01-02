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
        self.__erp_db = pymysql.connect(self.__local_database_IP, self.__local_user_name, self.__local_user_password,
                                        self.__local_database_name)
        self.__db_cursor = self.__erp_db.cursor()
        self.__db_sql = ""
        self.__init_raw_material_info_table()
        self.__init_raw_material_order_table()
        self.__init_production_info_table()
        self.__init_raw_material_repository_table()
        self.__init_production_repository_table()
        self.__init_production_order_table()
        self.__init_account_info_table()
        pass

    # Init Database Tables And Data
    def __init_account_info_table(self):
        self.__create_account_info_table()
        self.__insert_root_account_info_data()

    def __init_raw_material_info_table(self):
        self.__create_raw_material_info_table()
        self.__insert_initial_raw_material_info_data()

    def __init_raw_material_order_table(self):
        self.__create_raw_material_order_table()
        self.__insert_initial_raw_material_order_data()

    def __init_production_info_table(self):
        self.__create_production_info_table()
        self.__insert_initial_production_info_data()

    def __init_raw_material_repository_table(self):
        self.__create_raw_material_repository_table()
        self.__insert_initial_raw_material_repository_data()

    def __init_production_repository_table(self):
        self.__create_production_repository_table()
        self.__insert_initial_production_repository_data()

    def __init_production_order_table(self):
        self.__create_production_order_table()
        self.__insert_initial_production_order_data()

    def __create_account_info_table(self):
        self.__db_sql = """CREATE TABLE IF NOT EXISTS ACCOUNT_INFO(
                            NAME VARCHAR(20) PRIMARY  KEY,
                            PASSWORD VARCHAR(20) NOT NULL) """
        self.__db_cursor.execute(self.__db_sql)

    def __create_raw_material_info_table(self):
        self.__db_sql = """CREATE TABLE IF NOT EXISTS RAWMATERIAL_INFO(
                                ID VARCHAR(20) PRIMARY KEY,
                                NAME VARCHAR(20) NOT NULL,
                                COST INT NOT NULL,
                                DELIVERYTIME INT NOT NULL)"""
        self.__db_cursor.execute(self.__db_sql)

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

    def __create_production_info_table(self):
        self.__db_sql = """CREATE TABLE IF NOT EXISTS PRODUCTION_INFO(
                                ID VARCHAR(20) PRIMARY  KEY ,
                                NAME VARCHAR(20) NOT NULL ,
                                RAWMATERIAL_COMPOSITION VARCHAR(20)NOT NULL)"""
        self.__db_cursor.execute(self.__db_sql)

    def __create_raw_material_repository_table(self):
        self.__db_sql = """CREATE TABLE IF NOT EXISTS RAWMATERIAL_REPOSITORY(
                            RAWMATERIAL_ID VARCHAR(2) PRIMARY  KEY,
                            NUM INT NOT NULL)"""
        self.__db_cursor.execute(self.__db_sql)

    def __create_production_repository_table(self):
        self.__db_sql = """CREATE TABLE IF NOT EXISTS PRODUCTION_REPOSITORY(
                                   PRODUCTION_ID VARCHAR(20) PRIMARY KEY,
                                   NUM INT NOT NULL)"""
        self.__db_cursor.execute(self.__db_sql)

    def __create_production_order_table(self):
        self.__db_sql = """CREATE TABLE IF NOT EXISTS PRODUCTION_ORDER(
                            ID VARCHAR(20) PRIMARY  KEY,
                            NAME VARCHAR(20) NOT NULL,
                            PRODUCTION_ID VARCHAR(20) NOT NULL,
                            QUANTITY INT NOT NULL,
                            STATUS INT NOT NULL DEFAULT 0)"""
        self.__db_cursor.execute(self.__db_sql)

    def __insert_root_account_info_data(self):
        params = []
        self.__db_sql = """DELETE FROM ACCOUNT_INFO"""
        try:
            self.__db_cursor.execute(self.__db_sql)
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

        self.__db_sql = """INSERT INTO ACCOUNT_INFO VALUES ('root','root')"""
        self.__execute_sql()

    def __insert_initial_raw_material_order_data(self):
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
        for i in range(4):
            params.append((str(i), 'order' + str(i), '2', int(random.randint(1, i * 3 + 2)), int(2), '1-1', '1-3'))

        try:
            self.__db_cursor.executemany(self.__db_sql, params)
            self.__erp_db.commit()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def __insert_initial_raw_material_info_data(self):
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

    def __insert_initial_production_info_data(self):
        self.__db_sql = """DELETE FROM PRODUCTION_INFO"""
        try:
            self.__db_cursor.execute(self.__db_sql)
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))
        self.__db_sql = """INSERT INTO PRODUCTION_INFO VALUES (%s,%s,%s)"""
        params = []
        for i in range(4):
            params.append((i, 'p' + str(i),
                           str(random.randint(0, 4)) + '-' + str(random.randint(1, 10)) + '/' + str(random.randint(0,
                                                                                                                   4)) + '-' + str(
                               random.randint(1, 10))))
        try:
            self.__db_cursor.executemany(self.__db_sql, params)
            self.__erp_db.commit()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def __insert_initial_raw_material_repository_data(self):
        self.__db_sql = """DELETE FROM RAWMATERIAL_REPOSITORY"""
        try:
            self.__db_cursor.execute(self.__db_sql)
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

        self.__db_sql = """INSERT INTO RAWMATERIAL_REPOSITORY VALUES(%s,%s)"""
        params = []
        for i in range(4):
            params.append((i, random.randint(10, 50)))
        try:
            self.__db_cursor.executemany(self.__db_sql, params)
            self.__erp_db.commit()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def __insert_initial_production_repository_data(self):
        self.__db_sql = """DELETE FROM PRODUCTION_REPOSITORY"""
        try:
            self.__db_cursor.execute(self.__db_sql)
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

        self.__db_sql = """INSERT INTO PRODUCTION_REPOSITORY VALUES(%s,%s)"""
        params = []
        for i in range(4):
            params.append((i, random.randint(1, 10)))
        try:
            self.__db_cursor.executemany(self.__db_sql, params)
            self.__erp_db.commit()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def __insert_initial_production_order_data(self):
        self.__db_sql = """DELETE FROM PRODUCTION_ORDER"""
        try:
            self.__db_cursor.execute(self.__db_sql)
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

        self.__db_sql = """INSERT INTO PRODUCTION_ORDER VALUES (%s,%s,%s,%s,%s)"""
        params = []
        for i in range(4):
            params.append((i, 'po' + str(i), random.randint(0, 4), random.randint(1, 3), 0))
        try:
            self.__db_cursor.executemany(self.__db_sql, params)
            self.__erp_db.commit()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def __test_raw_material_info_query(self):
        self.__db_sql = """SELECT * FROM RAWMATERIAL_INFO"""
        try:
            self.__db_cursor.execute(self.__db_sql)
            query_result = self.__db_cursor.fetchall()
            for results in query_result:
                print(results)

        except pymysql.DatabaseError as error:
            print("Error: {}".format(error.args))
            self.__erp_db.rollback()

    def insert_raw_material_info(self, in_id, in_name, in_cost, in_delivery_time):
        self.__db_sql = """INSERT INTO RAWMATERIAL_INFO VALUES (%s,%s,%s,%s)"""
        params = (in_id, in_name, in_cost, in_delivery_time)
        try:
            self.__db_cursor.execute(self.__db_sql, params)
            self.__erp_db.commit()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def insert_raw_material_order(self, in_raw_material_order):
        self.__db_sql = """INSERT INTO RAWMATERIAL_ORDER VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        params = in_raw_material_order.get_attributes()
        try:
            self.__db_cursor.execute(self.__db_sql, params)
            self.__erp_db.commit()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def query_account_info(self, in_name):
        self.__db_sql = "SELECT * FROM ACCOUNT_INFO WHERE NAME = %s"
        try:
            self.__db_cursor.execute(self.__db_sql, in_name)
            return self.__db_cursor.fetchall()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def query_raw_material_info(self, in_id):
        self.__db_sql = """SELECT * FROM RAWMATERIAL_INFO WHERE ID = %s"""
        try:
            self.__db_cursor.execute(self.__db_sql, str(in_id))
            return self.__db_cursor.fetchall()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def query_raw_material_order(self, in_order_id):
        self.__db_sql = """SELECT * FROM RAWMATERIAL_ORDER WHERE ID = %s"""
        try:
            self.__db_cursor.execute(self.__db_sql, str(in_order_id))
            return self.__db_cursor.fetchall()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def query_production_info(self, in_production_id):
        self.__db_sql = """SELECT * FROM PRODUCTION_INFO WHERE ID = %s"""
        try:
            self.__db_cursor.execute(self.__db_sql, str(in_production_id))
            return self.__db_cursor.fetchall()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def query_raw_material_repository(self, in_raw_material_id):
        self.__db_sql = """SELECT * FROM RAWMATERIAL_REPOSITORY WHERE RAWMATERIAL_ID = %s"""
        try:
            self.__db_cursor.execute(self.__db_sql, str(in_raw_material_id))
            return self.__db_cursor.fetchall()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def query_production_repository(self, in_production_id):
        self.__db_sql = """SELECT * FROM PRODUCTION_REPOSITORY WHERE PRODUCTION_ID = %s"""
        try:
            self.__db_cursor.execute(self.__db_sql, str(in_production_id))
            return self.__db_cursor.fetchall()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def query_production_order(self, in_id):
        self.__db_sql = """SELECT * FROM PRODUCTION_ORDER WHERE ID = %s"""
        try:
            self.__db_cursor.execute(self.__db_sql, in_id)
            return self.__db_cursor.fetchall()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def query_raw_material_category_total_num(self):
        self.__db_sql = """SELECT COUNT(*) FROM RAWMATERIAL_INFO """
        try:
            self.__db_cursor.execute(self.__db_sql)
            return self.__db_cursor.fetchall()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def query_raw_material_category_remain_num(self):
        self.__db_sql = """SELECT COUNT(*) FROM RAWMATERIAL_REPOSITORY """
        try:
            self.__db_cursor.execute(self.__db_sql)
            return self.__db_cursor.fetchall()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def update_raw_material_repository(self, in_id, in_num):
        self.__db_sql = "UPDATE RAWMATERIAL_REPOSITORY SET NUM = NUM + %s WHERE RAWMATERIAL_ID = %s"
        params = (in_num, in_id)
        try:
            self.__db_cursor.execute(self.__db_sql, params)
            self.__erp_db.commit()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def update_production_repository(self, in_id, in_num):
        self.__db_sql = "UPDATE PRODUCTION_REPOSITORY SET NUM = NUM + %s WHERE PRODUCTION_ID = %s"
        params = (in_num, in_id)
        try:
            self.__db_cursor.execute(self.__db_sql, params)
            self.__erp_db.commit()
        except pymysql.DatabaseError as error:
            self.__erp_db.rollback()
            print("Error: {}".format(error.args))

    def update_production_order(self, in_id, in_flag):
        self.__db_sql = """UPDATE PRODUCTION_ORDER SET STATUS = %s WHERE  ID = %s"""
        params = (in_flag, in_id)
        try:
            self.__db_cursor.execute(self.__db_sql, params)
            self.__erp_db.commit()
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
