import re
# 面向过程编程，从上至下执行
user1 = {'name': 'tom', 'hp': 100}
user2 = {'name': 'jerry', 'hp': 130}


def print_role(rolename):
    print('name is %s ,hp is %s' % (rolename['name'], rolename['hp']))


print_role(user1)

print('================')
# 使用类进行面向对象编程
# 定义一个类，大写字母开头
# 类是将相同的内容进行归纳总结，更符合人的思维

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，job等属性绑上去：

# 注意：特殊方法“__init__”前后分别有两个下划线！！！
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：


class Player():
    def __init__(self, name, hp, job):
        # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
        # 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__name = name  # 将属性前加上"__"防止实例直接修改属性
        self.hp = hp
        self.job = job

    # 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
    # 但是如果外部代码要获取name和score怎么办？可以给类增加get_name这样的方法：
    def get_name(self):
        return self.__name

    # 在方法中，可以对参数做检查，避免传入无效的参数：
    def set_name(self, newname):
        t = re.findall(r'\W', newname)
        if len(t) == 0:
            self.__name = newname
        else:
            print('newName is : %s , t is: %s ' % (newname, len(t)))

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

    #     父类和子类有同名方法时，引用子类的方法时会覆盖父类的同名方法, 这就是继承的多态
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
print('user1的name是：', user1.get_name())
user1.set_name('brooklyn')
print('user1的新name是：', user1.get_name())
# print('user1 is', user1)
# print('user2 is', user2)

# 判断一个变量是否是某个类型可以用isinstance()判断
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
print('Is user1 Player? ', isinstance(user1, Player))


a1 = Monster(200)
print(a1.hp)
print(a1.run())

a2 = AnimalsMoster(5)
print(a2.hp)
print(a2.run())

a3 = BossMoster()
a3.whoami()

# ==================================== getType ====================================
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 我们来判断对象类型，使用type()函数
print('============getType==============')
print('a1的类型 %s' % type(a1))
print('a2的类型 %s' % type(a2))
print('a3的类型 %s' % type(a3))


# 判断谁是谁的子/父类

print(isinstance(a2, Monster))
print(isinstance(a2, AnimalsMoster))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print('============dir==============')
print(dir('ABC'))# 返回所有str的属性和方法

#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
#在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：

print('Is len(**) == **.__len__ ? ', len('ABC') == 'ABC'.__len__())

print('[1,2,3]的类型是 %s' %type([1,2,3]))
print('{1,2,3}的类型是 %s' %type({1,2,3}))
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
# 能用type()判断的基本类型也可以用isinstance()判断
import types
print(type(lambda x: x)==types.LambdaType)
def fn():
    pass
print('Is fn a function?', type(fn)==types.FunctionType)
print('Is "123" a string?', isinstance('123',str))


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 100
    def square(self):
        return self.x * self.x

objTest = MyObject()
print('有y属性吗？', hasattr(objTest,'x')) # 有x属性吗？
print(objTest.x)

print('有y属性吗？', hasattr(objTest,'y')) # 有y属性吗？
setattr(objTest,'y',999)
print(objTest.y)
print(getattr(objTest, 'y'))

# 如果没有这个属性，会返回一个'AttributeError'的错误, 可以传入一个默认值，如果属性不存在就返回默认值
print('有z属性吗？', getattr(objTest,'z', 404))



# 一个正确的用法的例子如下：
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None



# 参考链接：
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017495723838528
# https://docs.python.org/3/library/types.html    about types
