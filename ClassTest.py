# 面向过程编程，从上至下执行
user1 = {'name': 'tom', 'hp': 100}
user2 = {'name': 'jerry', 'hp': 130}


def print_role(rolename):
    print('name is %s ,hp is %s' % (rolename['name'], rolename['hp']))


print_role(user1)

# 使用类进行面向对象编程
# 定义一个类，大写字母开头
# 类是将相同的内容进行归纳总结，更符合人的思维


class Player():
    def __init__(self, name, hp, job):
        self.__name = name  # 将属性前加上"__"防止实例直接修改属性
        self.hp = hp
        self.job = job

    def print_role(self):  # 定义一个方法
        print('name is %s ,hp is %s,job is %s' %
              (self.__name, self.hp, self.job))

    def modify_name(self, newname):
        self.__name = newname
# 如果需要定义其他类，且暂时先不进行编写
# class Monster():
#     '定义怪物类'
#     pass
# 先用pass省略具体内容，先把业务逻辑写清


class Monster():
    '定义怪物类'

    def __init__(self, hp=100):  # hp=100是初始化的默认值
        self.hp = hp

    def run(self):
        print('Monster移动到某个位置')

    def whoami(self):
        print('我是Monster类')


# 继承和多态都是面向对象编程的重要特征
# Monster的子类,Monster作为参数传给子类


class AnimalsMoster(Monster):
    '普通的怪物'

    def __init__(self, hp=10):
        # 子类和父类的属性相同，当大量实例引用时会引起内存消耗，所以使用super()代替，避免重复初始化
        # self.hp = hp
        super().__init__(hp)


class BossMoster(Monster):
    'Boss类怪物'

    def __init__(self, hp=1000):
        super().__init__(hp)
    #     父类和子类有同名方法时，引用子类的方法时会覆盖父类的同名方法

    def whoami(self):
        print('我是Monster的子类BossMonster')


# 类的实例化
user1 = Player('tom', 100, 'solder')
user2 = Player('jerry', 130, 'mailman')
user1.print_role()
user2.print_role()

user2.modify_name('bruce')
user2.print_role()
# user1.__name不能改变user1的name值
user1.__name = 'bruno'
user1.print_role()


a1 = Monster(200)
print(a1.hp)
print(a1.run())

a2 = AnimalsMoster(5)
print(a2.hp)
print(a2.run())

a3 = BossMoster()
a3.whoami()


print('a1的类型 %s' % type(a1))
print('a2的类型 %s' % type(a2))
print('a3的类型 %s' % type(a3))
# 判断谁是谁的子/父类
print(isinstance(a2, Monster))
