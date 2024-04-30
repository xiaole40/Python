#用户从键盘输入一串字符（以回车键结束），统计并输出其中数字、大写字母、小写字母及其他字符的个数
a=b=c=d=0
str=input("Please input a string: ")
for ch in str:
    if ch=='\n':
        break;
    elif '0'<=ch<='9':
        a+=1
    elif 'A'<=ch<='Z':
        b+=1
    elif 'a'<=ch<='z':
        c+=1
    else:
        d+=1
print("数字、大写字母、小写字母小写字母及其他字符的个数是%d、%d、%d、%d\n"%(a,b,c,d))

    
