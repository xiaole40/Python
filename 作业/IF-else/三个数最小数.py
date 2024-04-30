a=int(input('请输入第一个数：'))
b=int(input('请输入第二个数：'))
c=int(input('请输入第三个数：'))
if a<b:
    if a<c:
        min=a
    else:
        min=c
else:
    if b<c:
        min=b
    else:
        min=c
print("最小的数是：",min)
