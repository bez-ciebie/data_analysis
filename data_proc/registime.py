import sys,os
sys.path.append(os.getcwd())

from entity import getEntity as get


###   9.	用户注册时间列表regisTime；regisTimeNumber[同上计数] （userinfo本项做字符串截取，做判断计数：注意等式两边类型要相同）
def registime():
   #！类似哈希表
   #! [‘202301’, ‘202302’, ‘202303’, ‘202304’, ‘202305’, ‘202306’, ‘202307’, ‘202308’, ‘202309’, ‘202310’, ‘202311’, ‘202312’,]

   return get.getregistime()


print(registime())