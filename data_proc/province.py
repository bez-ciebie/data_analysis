import sys,os
sys.path.append(os.getcwd())

from entity import getEntity as get


###   6.	省份列表province（所有省份以及省份统计）
def PROVINCE():
   #！类似哈希表，地址是省份编号从1开始，值对应该省的人数
   #{11: 1, 7: 1, 4: 1}
   #[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   # 即：li[4]=1
   province = [0 for _ in range(31)]

   for each in get.getProvince():
      province[each[0]]+=1

   return province

print(PROVINCE())