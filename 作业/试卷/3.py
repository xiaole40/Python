#  程序改错题 第一题

y=input("请输入任意一个年份：")          #错误1
if (y%4==0 or y%100!=0) or y%400==0:      #错误2
    print("该年为闰年")
else:
    print("该数不是闰年")


       
