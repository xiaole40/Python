#定义学生类
class Stu:
    def _init_(self,num,name,credit,course):
        self.num=num
        self.name=name
        self.credit=credit
        self.course=course
    def choose(self,c):
        self.credit+=c.credit
        self.course.append(c.name)

#定义课程类
class Cou:
    def _init_(self,num,name,credit):
        self.num=num
        self.name=name
        self.credit=credit
stu_1=Stu("201801","Jack",0,[""])
stu_2=Stu("201802","Tom",3,["Math"])
cou_1=Cou("01","Python",3)
cou_2=Cou("02","C",4)
stu_1.choose(cou_1)
stu_2.choose(cou_2)

#输出各学生信息
print("学号:",stu_1.num,"姓名：",stu_1.name,"总学分：",stu_1.credit,"所选课程",stu_1.course)
print("学号:",stu_2.num,"姓名：",stu_2.name,"总学分：",stu_2.credit,"所选课程",stu_2.course)

    
