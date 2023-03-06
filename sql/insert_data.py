import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
print ("数据库打开成功")

# 插入userinfo表
c.execute("INSERT INTO USERINFO (U_ID,U_NAME,AGE,GENDER,PROVINCE,REGIS_TIME) \
      VALUES (1, '魏子皓', 22, 1, 11, '2023-01-12T11:10:00' )")
c.execute("INSERT INTO USERINFO (U_ID,U_NAME,AGE,GENDER,PROVINCE,REGIS_TIME) \
      VALUES (2, '白杬钊', 20, 1, 7, '2023-01-12T11:13:00' )")
c.execute("INSERT INTO USERINFO (U_ID,U_NAME,AGE,GENDER,PROVINCE,REGIS_TIME) \
      VALUES (3, '小红', 35, 0, 4, '2023-01-12T12:13:00' )")

# 插入meetings表
c.execute("INSERT INTO MEETINGS (M_ID,C_ID,LOGIN_TIME,LOGOUT_TIME) \
      VALUES (14323, 1, '2023-01-12T12:15:00', '2023-01-12T12:16:00' )")
c.execute("INSERT INTO MEETINGS (M_ID,C_ID,LOGIN_TIME,LOGOUT_TIME) \
      VALUES (14324, 2, '2023-01-12T12:17:00', '2023-01-12T12:18:00' )")
c.execute("INSERT INTO MEETINGS (M_ID,C_ID,LOGIN_TIME,LOGOUT_TIME) \
      VALUES (14325, 3, '2023-01-12T19:15:00', '2023-01-12T19:15:00' )")
c.execute("INSERT INTO MEETINGS (M_ID,C_ID,LOGIN_TIME,LOGOUT_TIME) \
      VALUES (14326, 1, '2023-01-12T19:15:30', '2023-01-12T19:15:30' )")

# 插入members表
c.execute("INSERT INTO MEMBERS (ID,M_ID,U_ID) \
      VALUES (1, 14323, 1)")
c.execute("INSERT INTO MEMBERS (ID,M_ID,U_ID) \
      VALUES (2, 14323, 2)")
c.execute("INSERT INTO MEMBERS (ID,M_ID,U_ID) \
      VALUES (3, 14324, 2)")
c.execute("INSERT INTO MEMBERS (ID,M_ID,U_ID) \
      VALUES (4, 14324, 1)")
c.execute("INSERT INTO MEMBERS (ID,M_ID,U_ID) \
      VALUES (5, 14324, 3)")
c.execute("INSERT INTO MEMBERS (ID,M_ID,U_ID) \
      VALUES (6, 14325, 3)")
c.execute("INSERT INTO MEMBERS (ID,M_ID,U_ID) \
      VALUES (7, 14326, 1)")
c.execute("INSERT INTO MEMBERS (ID,M_ID,U_ID) \
      VALUES (8, 14326, 2)")

conn.commit()
print ("数据插入成功")
conn.close()