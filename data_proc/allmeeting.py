import sys,os
sys.path.append(os.getcwd())

from entity import getEntity as get


###   5.	历史会议列表allMeeting（MID的个数）
def allmeeting():
   return get.getallmeetings()

print(allmeeting())
