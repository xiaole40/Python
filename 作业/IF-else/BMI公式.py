h=float(input('请输入你的身高：'))
t=float(input('请输入你的体重：'))
a=t/h**2
print()
if a<18.5:
   print("您的体重过轻")
elif a<25:
      print('正常')
elif a<28:
      print('过重')
elif a<32:
      print('肥胖') 
else:
    print('您的体重严重肥胖！') 
