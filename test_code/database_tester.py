import pymysql
db = pymysql.connect("127.0.0.1", "root", "0000", "test_database")
cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE)
         VALUES ('aaa', 'bbb', 20)"""
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()
db.close()

#WSL TEST



