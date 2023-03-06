'''
Userinfo存储了所有历史用户的信息；
Meetings储存了所有历史会议的信息；
Members存储了所有会议的人员名单；
在创建新会议时，会将LOGIN_TIME= LOGOUT_TIME，会议结束时，重新将LOGOUT_TIME赋予当前时间。
可视化功能如下，请根据括号内容完成程序，以左侧示例参数保存数据：
   1.	总用户人数allUserNumber（userinfo注册人数统计）
   2.	在线用户人数nowUserNumber（根据meetings中UID统计）
   3.	当前活跃会议数nowMeetingNumber（遍历会议列表，统计LOGIN_TIME= LOGOUT_TIME的项个数）
   4.	历史总会议数allMeetingNumber（MID的个数）
   5.	历史总会议列表allMeeting[]（所有MID）
   6.	省份统计e.g.: province[]  类似哈希表，地址是省份编号，值对应该省的人数  数据库中从0开始
   7.	性别统计gender[]：（同上）
   8.	年龄统计age[‘<20’, ’20_29’, ’30-39’, ‘40_49’, ’50_59’, ’>60’] (同上，年龄区间划分如例)
   9.	用户注册时间列表regisTime[‘202301’, ‘202302’, ‘202303’, ‘202304’, ‘202305’, ‘202306’, ‘202307’, ‘202308’, ‘202309’, ‘202310’, ‘202311’, ‘202312’,]；regisTimeNumber[同上计数] （userinfo本项做字符串截取，做判断计数：注意等式两边类型要相同）
'''

from entity import getEntity as get

userinfo=get.getUserInfo()
meetings=get.getMeetings()
members=get.getMembers()

for user_row in userinfo:
   print ("U_ID = ", user_row[0])
   print ("U_NAME = ", user_row[1])
   print ("AGE = ", user_row[2])
   print ("GENDER = ", user_row[3])
   print ("PROVINCE = ", user_row[4])
   print ("REGIS_TIME = ", user_row[5],"\n")


for meetings_row in meetings:
   print ("M_ID = ", meetings_row[0])
   print ("C_ID = ", meetings_row[1])
   print ("LOGIN_TIME = ", meetings_row[2])
   print ("LOGOUT_TIME = ", meetings_row[3],"\n")

for members_row in members:
   print("ID = ", members_row[0])
   print ("M_ID = ", members_row[1])
   print ("U_ID = ", members_row[2],"\n" )



nowusernumber = NOWUSERNUMBER()
print(NOWUSERNUMBER())   

allUserNumber = ALLUSERNUMBER()
print(allUserNumber)