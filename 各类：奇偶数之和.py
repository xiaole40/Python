i=0                            #此为求终止值为100时的偶数之和
s=0
while i<=100:
        if i%2==0:
           s+=i
        i+=1
print("偶数之和是：%d"%s)


#以下为终止值不确定时，求总数之和及相对应的奇偶数之和

n=int(input("请输入一个数："))  #此为求终止值为N时的奇偶数之和
i=0
s=0
s1=0
s2=0
while i<=n:
        s+=i
        if i%2==0:
            s1+=i
        else:
            s2+=i
        i+=1
print("总数之和是：%d"%s)
print("偶数之和是：%d"%s1)
print("奇数之和是：%d"%s2)


n=int(input("请输入一个数："))  #此为求终止值为N时的奇偶数之和
s=0
s1=0
s2=0
for i in range(0,n+1,1):
    s+=i
    if i%2==0:
        s1+=i
    else:
        s2+=i
print("总数之和是：%d"%s)
print("偶数之和是：%d"%s1)
print("奇数之和是：%d"%s2)

            
