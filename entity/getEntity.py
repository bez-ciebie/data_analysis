import sqlite3


# 以list形式返回userinfo
def getuserinfo():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化userinfo表
    userinfo = c.execute("SELECT U_ID,U_NAME,AGE,GENDER,PROVINCE,REGIS_TIME  from USERINFO")
    get = list(userinfo)
    conn.close()

    return get

# 以list形式返回meetings
def getmeetings():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化meetings表
    meetings = c.execute("SELECT M_ID,C_ID,LOGIN_TIME,LOGOUT_TIME from MEETINGS")
    get = list(meetings)
    conn.close()

    return get

# 以list形式返回会议members信息
def getmembers():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    members = c.execute("SELECT ID,M_ID,U_ID  from MEMBERS")
    get = list(members)
    conn.close()

    return get

# 查找召开的会议数
def getonlinemeetings():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    onlinemeetings = c.execute("SELECT M_ID FROM MEETINGS WHERE LOGIN_TIME == LOGOUT_TIME")
    get = list(onlinemeetings)
    conn.close()

    return get

# 查找在线用户数量
def getonlineuser():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    onlineuser = c.execute("SELECT U_ID from MEMBERS WHERE M_ID IN (SELECT M_ID FROM MEETINGS WHERE LOGIN_TIME == LOGOUT_TIME)")
    get = list(onlineuser)
    conn.close()

    return get

# 查找所有的会议
def getallmeetings():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    allmeetings = c.execute("SELECT M_ID FROM MEETINGS")
    get = list(allmeetings)
    conn.close()

    return get

# 查找所有省份
def getprovince():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    province = c.execute("SELECT PROVINCE FROM USERINFO")
    get = list(province)
    conn.close()

    return get

# 查找所有性别
def getgender():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    gender = c.execute("SELECT GENDER FROM USERINFO")
    get = list(gender)
    conn.close()

    return get

# 查找所有AGE
def getage():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    age = c.execute("SELECT AGE FROM USERINFO")
    get = list(age)
    conn.close()

    return get

# 查找所有regisTime
def getregistime():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    registime = c.execute("SELECT REGIS_TIME FROM USERINFO")
    get = list(registime)
    conn.close()

    return get

print(getregistime())