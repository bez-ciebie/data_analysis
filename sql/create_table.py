import sqlite3

# 连接test.db数据库
conn = sqlite3.connect('test.db')

# 打开外键约束
conn.execute('PRAGMA foreign_keys = ON')
print ("数据库打开成功")
c = conn.cursor()

# 创建USERINFO表
c.execute('''CREATE TABLE IF NOT EXISTS USERINFO
       (
              U_ID           INT PRIMARY KEY        NOT NULL,
              U_NAME         VARCHAR(20) NOT NULL,
              AGE            INT(4)      NOT NULL,
              GENDER         INT(1)      NOT NULL,
              PROVINCE       INT(4)      NOT NULL,
              REGIS_TIME     VARCHAR(20) NOT NULL
       );
       ''')
print ("USERINFO数据表创建成功")
conn.commit()

# 创建MEETINGS表
c.execute('''CREATE TABLE IF NOT EXISTS MEETINGS
       (
              M_ID           INT PRIMARY KEY NOT NULL  UNIQUE,
              C_ID           INT         NOT NULL,
              LOGIN_TIME     VARCHAR(20) NOT NULL,
              LOGOUT_TIME    VARCHAR(20) NOT NULL,
              FOREIGN KEY(C_ID) REFERENCES USERINFO(U_ID)
       );
       ''')
print ("MEETINGS数据表创建成功")
conn.commit()

# 创建MEMBERS表
c.execute('''CREATE TABLE IF NOT EXISTS MEMBERS
       (
              ID             INT PRIMARY KEY NOT NULL  UNIQUE,
              M_ID           INT NOT NULL,
              U_ID           INT NOT NULL,
              FOREIGN KEY(U_ID) REFERENCES USERINFO(U_ID),
              FOREIGN KEY(M_ID) REFERENCES MEETINGS(M_ID)
       );
       ''')
print ("MEMBERS数据表创建成功")
conn.commit()

conn.close()
