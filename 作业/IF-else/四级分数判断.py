a=float(input('请输入你的分数:'))
if a>=425:
    print('恭喜你通过英语四级！')
    print('你还超出了',a-425,'分')
else:
    print('很遗憾你没有通过英语四级！')
    print('你还要提升',425-a,'分才可以通过！')
