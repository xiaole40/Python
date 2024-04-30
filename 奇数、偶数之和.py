x_old=0;x_even=0
for i in range(1,101):
    if i%2!=0:
        x_old +=i
    else:
        x_even+=i
print("1-100在所有的奇数之和：",x_old)
print("1-100在所有的偶数之和：",x_even)

    
