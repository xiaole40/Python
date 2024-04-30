y=int(input('请输入一个年份：'))
if y%12==0:
    print(y,'年是猴年',sep='')
elif y%12==1:
    print(y,'年是鸡年',sep='')
elif y%12==2:
    print(y,'年是狗年',sep='')
elif y%12==3:
    print(y,'年是猪年',sep='')
elif y%12==4:
    print(y,'年是鼠年',sep='')
elif y%12==5:
    print(y,'年是牛年',sep='')
elif y%12==6:
    print(y,'年是虎年',sep='')
elif y%12==7:
    print(y,'年是兔年',sep='')
elif y%12==8:
    print(y,'年是龙年',sep='')
elif y%12==9:
    print(y,'年是蛇年',sep='')
elif y%12==10:
    print(y,'年是马年',sep='')
else:
    print(y,'年是羊年',sep='')
