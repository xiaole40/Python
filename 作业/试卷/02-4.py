s=int(input("任意输入任意一个年龄："))
if  s>100 or s<0:
    print('非法输入，请重新输入！')
elif s>=79:
    print('老年')
elif s>=46:
    print('中年')
elif s>=18:
    print('青年')
elif s>=13:
    print('青少年')
else:
    print('婴幼儿')
