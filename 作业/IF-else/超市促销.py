s=float(input('请输入消费金额：'))
if  s>=500:
    print('实际支付的金额为：',s*0.75)
elif s>=300:
    print('实际支付的金额为：',s*0.85)
elif s>=100:
    print('实际支付的金额为：',s*0.95)
else:
    print('实际支付的金额为：',s*1)
