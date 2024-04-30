x=input('请输入一个18位身份证号码：')
if len(x)>18 or len(x)<18:
    print('不对，请从新输入')
else:
    y=x[6:10]#切出代表出生年份字符
    z=x[10:12]#切出代表出生月份字符
    d=x[12:14]#切出代表出生日期字符
    s=x[-2]
    print('出生年份：',y,sep='')
    print('出生月份：',z,sep='')
    print('出生日期：',d,sep='')
    if int(s)%2==1:
       print('性别是男')
    else:
       print('性别是女')
       
    
