tuple1 = ("学号","姓名","性别","出生年月")
list1 = ["230311371","郑伊龙","男","2001年4月"]
list2 = ["230311372","廖乐乐","男","2001年5月"]
list3 = ["230311373","祝英豪","男","2001年6月"]
list4 = ["230311374","李新安","男","2001年7月"]

# 列表
x = list(zip(tuple1,list1))
print(x)

# 字典
dict1 = dict(zip(tuple1,list1))
print(dict1)

list1.extend(dict1)
print(list1)

dict1 = {"学号":"230311372","姓名":"张三"}
print(dict1)

keys = ["a","b","c"]
values = [1,2,3]
d4 = dict(zip(keys,values))
print(d4)

x2 = dict(学号="230311374",姓名="李新安",性别="男",出生年月="2001年7月")
print(x2)

stu_info1 = {'num':'20180101','name':'Liming','sex':'male'}                 #直接赋值创建字典
stu_info2 = dict(stu_info1)                                                 #通过其他字典创建
stu_info3 = dict([('num','20180101'),('name','Liming'),('sex','name')])     #通过“（键，值）”对的列创建
stu_info4 = dict(num = '20180101',name = 'Liming',sex = 'male')             #通过关键字参数创建
stu_info5 = dict(zip(['num','name','sex'],['20180101','Liming','male']))    #通过dict和zip结合创建
if stu_info1 == stu_info2 == stu_info3 == stu_info4 == stu_info5:           #判断五个变量是否相等
    print("创建字典的5种方式相同")                                              #如果相同输出提示符
else:                                                                       #如果不相同
    print("创建字典的5种方式不相同")                                            #输出提示符
