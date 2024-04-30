stu={"num":"201801","name":"张三","credit":0,"course":[]} #定义一个学生
cours1={'num':'01','name':'Python语言','credit':3}  #定义一个课程1
cours2={'num':'02','name':'C语言','credit':4}   #定义一个课程2   
def choose(c):                               #定义实现选课功能的函数
    stu["credit"]=stu["credit"]+c["credit"] #将课程的学分累加到学生的总学分中
    stu["course"].append(c["name"])         #将课程名加入到学生的所选课程中
choose(cours1)                              #学生选课1
choose(cours2)                              #学生选课2
print(stu)                                  #输出学生信息
