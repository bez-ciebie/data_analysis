import sys,os
sys.path.append(os.getcwd())

from entity import getEntity as get


###   7.	性别列表gender
def GENDER():
   #！类似哈希表，存放地址0，1：女，男    值对应人数
   #{0，1：女，男}
   #[0, 0]   
   # 即：li[4]+=1
   gender = [0 for _ in range(2)]

   for each in get.getGender():
      gender[each[0]]+=1

   return gender

print(GENDER())