a=int(input('请输入一个三位数：'))                        
print()
if a>500:
   print("数字个位为：",a%10)
   print('数字十位为：',a//10%10)
   print('数字百位为：',a//100)
else:
    print(a,'不是大于500的数') 
