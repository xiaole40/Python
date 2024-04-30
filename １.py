# 求一个3X3的矩阵的两条对角线元素之和(注意：两条对角线交叉点处的元素只计算一次)

X =[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for i in range(len(X)):
    for j in range(len(X)):
        if i == j:
            sum+=X[i][i]
        if(j ==(len(X)-i-1-j)):
            sum+=X[i][2-i]
print(sum)

#问题解决
tuple=("英语","思政","Python程序设计")
#tuple[0]="英语(1)" #不能修改
list1=[78,69,83]
list2=[89,87,76]
sum1=0
sum2=0
for i,j in zip(list1,list2):
    sum1=sum1+i
    sum2=sum2+j
print("")
print("")