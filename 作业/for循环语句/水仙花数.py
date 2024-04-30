s=0
for i in range(100,1000):
    b=i%10
    c=i//10%10
    d=i//100
    if i ==b*b*b+c*c*c+d*d*d:
        print ('水仙花数为%d'%i)
