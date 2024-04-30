a=float(input("请输入a的值:"))		#输入a的值并转换为整数
b=float(input("请输入b的值:"))		#输入b的值并转换为整数
c=float(input("请输入c的值:"))		#输入c的值并转换为整数
if a>b:								#a>b
    if a>c:							#a>b并且a>c，最大值为a
        max=a						
    else:							#a>b并且c>a，最大值为c
        max=c
else:								#a<b
    if b>c:						#b>a并且b>c，最大值为b
        max=b
    else:						#b>a并且c>b，最大值为c
        max=c
print("max=",max)				#输出最大值max４５
