import sys,os
sys.path.append(os.getcwd())

from entity import getEntity as get


###   1.	总用户人数allUserNumber（userinfo注册人数统计）
def ALLUSERNUMBER():
   #!!! userinfo中Uid按照顺序递增
   return len(get.getUserInfo())

print(ALLUSERNUMBER())