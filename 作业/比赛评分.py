a1=[86,90,95,97,98,89,96,92,89,94]  #10个评委给a1打的分数
a2=[88,91,94,96,91,90,93,91,90,85]  #10个评委给a2打的分数

a1.remove(max(a1))
a1.sort()    #进行升序排序
#b=a1[1:-1]   #进行切片（去掉最高和最低）
a1.pop(0)
a1.pop()
print(a1)
print((1,23,3))
b=a1
x1=sum(b)/len(b)
a2.sort()

c=a2[1:-1]

x2=sum(c)/len(c)
if x1>x2:
    print('选手a1胜出')
elif x1==x2:
    print('平手')
else:
    print('选手a2胜出')
