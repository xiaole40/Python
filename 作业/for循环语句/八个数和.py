a=int(input('请输入第一个数：'))
b=int(input('请输入第二个数：'))
c=int(input('请输入第三个数：'))
d=int(input('请输入第四个数：'))
e=int(input('请输入第五个数：'))
f=int(input('请输入第六个数：'))
g=int(input('请输入第七个数：'))
h=int(input('请输入第八个数：'))
s=0
for i in range(a,h+1):
    s=s+i
print(a,'+',b,'...',h,'=',s,sep='')
