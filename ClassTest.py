# 面向过程编程，从上至下执行
user1 = {'name':'tom', 'hp':100}
user2 = {'name':'jerry', 'hp':130}

def print_role(rolename):
    print('name is %s ,hp is %s' %(rolename['name'], rolename['hp']))
print_role(user1)

# 使用类进行面向对象编程
# 定义一个类，大写字母开头
# 类是将相同的内容进行归纳总结，更符合人的思维
class Player():
    def __init__(self,name, hp, job):
        self.__name = name #将属性前加上"__"防止实例直接修改属性
        self.hp= hp
        self.job= job
    def print_role(self): #定义一个方法
        print('name is %s ,hp is %s,job is %s' %(self.__name, self.hp, self.job))
    def modify_name(self, newname):
        self.__name = newname
# 如果需要定义其他类，且暂时先不进行编写
class Monster():
    '定义怪物类'
    pass

# 类的实例化
user1 = Player('tom', 100, 'solder')
user2 = Player('jerry', 130, 'mailman')
user1.print_role()
user2.print_role()

user2.modify_name('bruce')
user2.print_role()
# user1.__name不能改变user1的name值
user1.__name= 'bruno'
user1.print_role()