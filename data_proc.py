ID_data=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
USERNAME_data=['魏子皓', '魏子皓', '魏子皓', '魏子皓', '白杬钊', '白杬钊', '白杬钊', '白杬钊', '小红', '小红', '小红', '小红']
AGE_data=[22, 22, 22, 22, 20, 20, 20, 20, 35, 35, 35, 35]
SEX_data=[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
PROVINCE=['SHANXI', 'SHANXI', 'SHANXI', 'SHANXI', 'HEBEI', 'HEBEI', 'HEBEI', 'HEBEI', 'SHANGHAI', 'SHANGHAI', 'SHANGHAI', 'SHANGHAI']
ACTION_data=['LIKE', 'LIKE', 'FOLLOW', 'FOLLOW', 'LIKE', 'LIKE', 'FOLLOW', 'FOLLOW', 'LIKE', 'LIKE', 'LIKE', 'FOLLOW']
CTIME_data=['2023-01-12T11:10:00', '2023-01-12T11:30:00', '2023-01-12T11:00:00', '2023-01-12T11:33:00', '2023-01-12T11:13:00', '2023-01-12T11:36:00', '2023-01-12T11:03:00', '2023-01-12T11:38:00', '2023-01-12T12:13:00', '2023-01-12T12:36:00', '2023-01-12T12:03:00', '2023-01-12T12:38:00'] 

print (" Numbers of Users: ", len(ID_data))
print('\n')

dict={}
for i in range(len(AGE_data)):
    print(USERNAME_data[i])
    print(AGE_data[i])
    dict[USERNAME_data[i]] = AGE_data[i]
print (dict)
print (list(dict.values()))
print('\n')

dict={}
for i in range(len(SEX_data)):
    print(USERNAME_data[i])
    print(SEX_data[i])
    dict[USERNAME_data[i]] = SEX_data[i]
print (dict)
print (list(dict.values()))
print(" Number of male users：", list(dict.values()).count(1))
print(" Number of female users：", list(dict.values()).count(0))
print('\n')

dict={}
for i in range(len(PROVINCE)):
    print(USERNAME_data[i])
    print(PROVINCE[i])
    dict[USERNAME_data[i]] = PROVINCE[i]
print (dict)
print (list(dict.values()))
print('\n')

print (" Number of LIKEs：", ACTION_data.count("LIKE"))
print (" Number of FOLLOWs：", ACTION_data.count("FOLLOW"))
print('\n')

list = []
for i in range(12):
    list.append(CTIME_data[i])
print(list)
for i in range(len(list)):
    print(list[i][11:19])
