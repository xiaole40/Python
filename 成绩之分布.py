score=float(input("请输入百分制成绩："))	#输入分数score的值并将其转化为整数
if score>100 or score<0:				#当分值不合理时显示出错信息
	print("输入数据无意义")
elif score>=90:				#当成绩大于等于90小于等于100时，输出“优”
	print("优")
elif score>=80:					#当成绩大于等于80小于90时，输出“良”
	print("良")
elif score>=70:					#当成绩大于等于70小于80时，输出“中”
	print("中")
elif score>=60:					#当成绩大于等于60小于70时，输出“及格”
	print("及格")
else:								#以上条件都不满足
	print("不及格")				#输出不
