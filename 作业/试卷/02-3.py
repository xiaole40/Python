y=int(input("请输入任意一个年份："))      
if (y%4==0 and y%100!=0) or y%400==0:    
    print("该年为闰年")
else:
    print("该数不是闰年")
