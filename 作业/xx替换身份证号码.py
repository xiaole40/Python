x=input('请输入18位身份证号码：')
while len(x)!=18:
    print('错误，请重新输入')
    x=input()
    if len(x)==18:
        break
b=x[6:14]
x1=x.replace(b,'*'*8)
print(x1)
