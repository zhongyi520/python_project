
'''
定义一个学生类，用来形容学生
'''


class Student():
    pass


class PythonStudent():
    name = None
    age = 18
    ke = 'python'

    def doHomework(self):
        print('我在做作业....')
        return None


# 实例化一个叫做白白的学生，是个具体的人
baibai = PythonStudent()
print(baibai.name)
print(baibai.age)
baibai.doHomework()


