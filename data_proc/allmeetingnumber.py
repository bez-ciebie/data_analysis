import sys,os
sys.path.append(os.getcwd())

from entity import getEntity as get


###   4.	历史总会议数allMeetingNumber（MID的个数）
def allmeetingnumber():
   #!!! login_time==logout_time筛选出在线会议，然后根据会议号找到会议成员
   return len(get.getallmeetings())

print(allmeetingnumber())
