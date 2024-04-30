s=0
for n in range(1,13):#循环次数
    x=int(input('请输入成绩：'))
    if x>0:
     s=s+x
print('平均数：',s/12)
print('***********************************************************')
s=0
for n in range(1,13):#循环次数
    x=float(input('请输入成绩：'))
    if x<0 or x>100:
        print('输入错误，请重新输入!')
    else:
     s=s+x
print('平均成绩：',s/12)        
print('***********************************************************')
s=0
for n in range(1,13):#循环次数
    x=float(input('请输入成绩：'))
    if x<0 or x>100:
        print('输入错误，请重新输入!')
    else:
     s=s+x
print('这%d个同学的平均成绩为%.2f'%(n,s/12)) 
