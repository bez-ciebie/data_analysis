from entity import getEntity

print(getEntity.getMeetings())


# import sqlite3
# # 以list形式返回userinfo

# conn = sqlite3.connect('sql/test.db')
# c = conn.cursor()
# print ("数据库打开成功")

# # 列表化userinfo表
# userinfo = c.execute("SELECT U_ID,U_NAME,AGE,SEX,PROVINCE,REGIS_TIME  from USERINFO")
# print(list(userinfo))
# print ("数据打印成功")
# conn.close()
