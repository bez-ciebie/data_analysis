from entity import getEntity as get

userinfo=get.getUserInfo()
meetings=get.getMeetings()
members=get.getMembers()

for user_row in userinfo:
   print ("U_ID = ", user_row[0])
   print ("U_NAME = ", user_row[1])
   print ("AGE = ", user_row[2])
   print ("GENDER = ", user_row[3])
   print ("PROVINCE = ", user_row[4])
   print ("REGIS_TIME = ", user_row[5],"\n")


for meetings_row in meetings:
   print ("M_ID = ", meetings_row[0])
   print ("C_ID = ", meetings_row[1])
   print ("LOGIN_TIME = ", meetings_row[2])
   print ("LOGOUT_TIME = ", meetings_row[3],"\n")

for members_row in members:
   print("ID = ", members_row[0])
   print ("M_ID = ", members_row[1])
   print ("U_ID = ", members_row[2],"\n" )