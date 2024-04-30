n=int(input("%的因数是: "))
print("%d的因数是:"%n,end="")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
print()
