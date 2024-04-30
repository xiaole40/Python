# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()
# j=1
# s=0
# for i in range(1,11):
#     j*=i
#     s+=j
# print(s)
# n = int(input("请输入任意一个正整数："))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print("sum=%d"%sum)
# sum1=0
# for num in range(2,21,2):
#     sum1=sum1+num*num
# print("2的平方+4的平方+6的平方+。。。20的平方=",sum1)
# n=int(input("请输入任意一个整数："))
# if n%7==0 and n%8==0:
#     print("YES")
# else:
#     print("NO")
# sum = 0
# for i in range(10,51):
#     sum+=i
#     i+=1
# print(sum)
# year = int(input("请输入一个年份："))
#
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(year, "是闰年")
# else:
#     print(year, "不是闰年")

# str1 = int(input("需要输入几个同学数据："))
# str2 = 1
# while str1>0:
#    print("\n第",str2,"个同学")
#    list_name=["姓名","年龄","性别","学号","体重","身高"]
#    姓名=input("请输入姓名:")
#    年龄=int(input("请输入年龄:"))
#    性别=input("请输入性别:")
#    学号=input("请输入学号:")
#    体重=float(input("请输入体重:"))
#    身高=float(input("请输入身高:"))
#    list_data=[姓名,年龄,性别,学号,体重,身高]
#    for i in range(0,len(list_name)):
#       print("%s:%s"%(list_name[i],list_data[i]))
#    str1 -= 1
#    str2 += 1

# list_name=["姓名","年龄","性别","学号","体重","身高"]
# 姓名=input("请输入姓名:")
# 年龄=int(input("请输入年龄:"))
# 性别=input("请输入性别:")
# 学号=input("请输入学号:")
# 体重=float(input("请输入体重:"))
# 身高=float(input("请输入身高:"))
# list_data=[姓名,年龄,性别,学号,体重,身高]
# i=0
# for i in range(6):
#     print("%s:%s"%(list_name[i],list_data[i]))
#     i+=1


id=input("请输入你的身份证号：")
birth_date = id[6:14]
birth_year = birth_date[0:4]
birth_month = birth_date[4:6]
birth_day = birth_date[6:8]
birthday=input(f"出生日： {birth_year}-{birth_month}-{birth_day}")
sex = id[16]
sex1=int(sex)
if sex1 % 2 == 0:
    print("性别：女")
else:
    print("性别：男")

# 编程题
#1：方法一
# list_a=[1,2,3,4,5,6]
# list_a.reverse()
# print(list_a)
#1：方法二
# list_a=[1,2,3,4,5,6]
# list_a=list_a[::-1]
# print(list_a)

#3；
# X=input("请输入字符串：")
# result_str = X[-1] + X[:-1]
# print("新的字符串:", result_str)

#4:
# a=[1,3,4,5,6,7,8,9]
# for b in a:
#     for c in range(2,b):
#         if b%c==0:
#             d=[b]
#             print(d)
#             break
























