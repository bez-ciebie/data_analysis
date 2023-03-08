import sys,os
sys.path.append(os.getcwd())

from entity import getEntity as get


###   3.	当前活跃会议数nowMeetingNumber（遍历会议列表，统计LOGIN_TIME= LOGOUT_TIME的项个数）
def onlinemeetingnumber():
   #!!! login_time==logout_time筛选出在线会议，然后根据会议号找到会议成员
   return len(get.getonlinemeetings())

print(onlinemeetingnumber())
