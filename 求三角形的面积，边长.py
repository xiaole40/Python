print('欢迎使用Python')
a=5
b=4
print(a+b)
a = float(input('输入三角形边长a: '))
b = float(input('输入三角形边长b: '))
c = float(input('输入三角形边长c: '))
d = float(input('输入三角形边长d: '))
e = float(input('输入三角形边长e: '))
f = float(input('输入三角形边长f: '))
g = float(input('输入三角形边长g: '))
# 计算半周长
c1 = (a + b + c) / 2
# 计算面积
s1 = (c1*(c1-a)*(c1-b)*(c1-c)) ** 0.5
# 计算半周长
c2 = (c +d +e) / 2
# 计算面积
s2 = (c2*(c2-c)*(c2-d)*(c2-e)) ** 0.5
# 计算半周长
c3 = (e +f + g)/ 2
# 计算面积
s3 = (c3*(c3-e)*(c3-f)*(c3-g)) ** 0.5
s=s1+s2+s3
print('三角形面积为 %0.2f' %s)
