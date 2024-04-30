for x in range(0,20+1):#公鸡个数
    for y in range(0,33+1):#母鸡个数
        z=100-x-y#小鸡个数
        if x*15+y*9+z==300  and z%3==0:
            print(x,y,z)
