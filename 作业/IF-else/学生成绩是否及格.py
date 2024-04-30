s=float(input('请输入一个分数：'))
if  s>100 or s<0:
    print('非法输入，请重新输入！')
elif s>=90:
    print('优秀！')
elif s>=80:
    print('良好！')
elif s>=70:
    print('中等！')
elif s>=60:
    print('及格！')
else:
    print('不及格，要加油！')
