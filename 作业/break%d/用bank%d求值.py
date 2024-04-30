s=0
i=1
while True:
    s=s+i
    if s>10000:
        break
    i=i+4
print('此时的累加和为%d,此时的加数为%d,符合题意的加数为%d'%(s,i,i+4))
