#-*-coding:utf-8-*-
class Car:
    def __init__(self, name='CARRRR',age=13):
        self.name=name
        self.age=age

    def __str__(self):
        msg = "大家好，这个类是用来描述车子的"
        return msg

    def getCarInfo(self):
        # print('车轮子个数:%d, 颜色%s' % (self.wheelNum, self.color))
        print("%s是一辆%d岁的汽车"%(self.name,self.age))

    def move(self):
        print("%s在移动……"%self.name)

BMW=Car('BMW')
AUDI=Car('Audi')

BMW.getCarInfo()
AUDI.move()
print(AUDI)
