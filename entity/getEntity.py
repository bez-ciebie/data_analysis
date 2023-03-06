import sqlite3
# 以list形式返回userinfo

def getUserInfo():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化userinfo表
    userinfo = c.execute("SELECT U_ID,U_NAME,AGE,SEX,PROVINCE,REGIS_TIME  from USERINFO")
    get = list(userinfo)
    conn.close()

    return get

# 以list形式返回meetings
def getMeetings():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化meetings表
    meetings = c.execute("SELECT M_ID,C_ID,LOGIN_TIME,LOGOUT_TIME from MEETINGS")
    get = list(meetings)
    conn.close()

    return get

# 以list形式返回会议members信息
def getMembers():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    members = c.execute("SELECT ID,M_ID,U_ID  from MEMBERS")
    get = list(members)
    conn.close()

    return get

# 查找召开的会议数
def getOnlineMeetings():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    onlinemeetings = c.execute("SELECT M_ID FROM MEETINGS WHERE LOGIN_TIME == LOGOUT_TIME")
    get = list(onlinemeetings)
    conn.close()

    return get

# 查找在线用户数量
def getOnlineUser():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    onlineuser = c.execute("SELECT U_ID from MEMBERS WHERE M_ID IN (SELECT M_ID FROM MEETINGS WHERE LOGIN_TIME == LOGOUT_TIME)")
    get = list(onlineuser)
    conn.close()

    return get

# 查找所有的会议
def getAllMeetings():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    allmeetings = c.execute("SELECT M_ID FROM MEETINGS")
    get = list(allmeetings)
    conn.close()

    return get

# 查找所有省份
def getProvince():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    province = c.execute("SELECT PROVINCE FROM USERINFO")
    get = list(province)
    conn.close()

    return get

# 查找所有性别
def getGender():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    gender = c.execute("SELECT GENDER FROM USERINFO")
    get = list(gender)
    conn.close()

    return get

# 查找所有AGE
def getAge():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    age = c.execute("SELECT AGE FROM USERINFO")
    get = list(age)
    conn.close()

    return get

# 查找所有regisTime
def getRegistime():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print ("数据库打开成功")

    # 列表化members表
    registime = c.execute("SELECT REGIS_TIME FROM USERINFO")
    get = list(registime)
    conn.close()

    return get

print(getRegistime())