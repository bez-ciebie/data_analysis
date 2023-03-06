import sys,os
sys.path.append(os.getcwd())

from entity import getEntity as get


###   2.	在线用户人数onlineUserNumber（根据meetings和members中UID统计，嵌套查询LOGIN=LOGOUT）
def ONLINEUSERNUMBER():
   #!!! login_time==logout_time筛选出在线会议，然后根据会议号找到会议成员
   return len(get.getOnlineUser())

print(ONLINEUSERNUMBER())
