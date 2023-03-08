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
from data_proc import allmeeting,age,allmeetingnumber,allusernumber,currentmeetingnumber,gender,onlineusernumber,province, registime

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc("font",family='MicroSoft YaHei')

def drawAge():
   #创建图形对象
   fig1 = plt.figure()
   #添加子图区域，参数值表示[left, bottom, width, height ]
   ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
   #准备数据
   age_number = age.age()
   age_box = ["<20","20_29","30-39","40_49","50_59",">60"]
   ax.set_yticks([2,4,6,8,10])
   #绘制柱状图
   ax.bar(age_box,age_number)
   plt.show()

def drawGender():
   #创建图形对象
   fig1 = plt.figure()
   #添加子图区域，参数值表示[left, bottom, width, height ]
   ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
   #准备数据
   age_number = gender.gender()
   age_box = ["female","male"]
   ax.set_yticks([2,4,6,8,10])
   #绘制柱状图
   ax.bar(age_box,age_number)
   plt.show()

def drawProvince():
   #创建图形对象
   fig1 = plt.figure()
   #添加子图区域，参数值表示[left, bottom, width, height ]
   ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
   #准备数据
   age_number = province.province()
   age_box = [   '四川', '浙江', '福建', '江苏', '山东', '湖南', '安徽', '河北', '广东', '湖北', '吉林',   
                           '山西', '江西', '广西', '贵州', '北京', '云南', '重庆', '河南', '陕西', '上海', '辽宁', '新疆',  
                           '内蒙古', '黑龙江', '天津', '甘肃', '海南', '青海', '宁夏', '西藏']

   ax.set_yticks([2,4,6,8,10])
   #绘制柱状图
   ax.bar(age_box,age_number)
   plt.show()

drawProvince()