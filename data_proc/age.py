import sys,os
sys.path.append(os.getcwd())

from entity import getEntity as get


###   8.	年龄区间的列表age（所有省份以及省份统计）age[‘<20’, ’20_29’, ’30-39’, ‘40_49’, ’50_59’, ’>60’]
def AGE():
   #！类似哈希表
   #! age[‘<20’, ’20_29’, ’30-39’, ‘40_49’, ’50_59’, ’>60’]
   #! [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   # 即：li[4]=1
   age = [0 for _ in range(6)]

   for each in get.getAge():
      age[judgeAge(each[0])]+= 1

   return age

def judgeAge(age):
   if age < 20:
      return 0
   elif age < 30:
      return 1
   elif age < 40:
      return 2
   elif age < 50:
      return 3
   elif age < 60:
      return 4
   else:
      return 5

print(AGE())