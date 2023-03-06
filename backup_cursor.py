import sqlite3
#初始化数组
ID_data=[]
USERNAME_data=[]
AGE_data=[]
SEX_data=[]
PROVINCE_data=[]
ACTION_data=[]
CTIME_data=[]

#数据库连接
conn = sqlite3.connect('test.db')
c = conn.cursor()
print ("数据库打开成功")


cursor = c.execute("SELECT ID,USERNAME,AGE,SEX,PROVINCE,ACTION,CTIME  from RECORD")
#遍历cursor中每一条数据，将同种数据其添加到数组中去。
for row in cursor:
    ID_data.append(row[0])  
    USERNAME_data.append(row[1])  
    AGE_data.append(row[2])  
    SEX_data.append(row[3])  
    PROVINCE_data.append(row[4])
    ACTION_data.append(row[5])  
    CTIME_data.append(row[6])   
print ("数据提取成功")
conn.close()
print(ID_data)
print(USERNAME_data)
print(AGE_data)
print(SEX_data)
print(PROVINCE_data)
print(ACTION_data)
print(CTIME_data)

