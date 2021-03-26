# coding:utf-8

# Python 中的类有一些特殊的方法，方法名前后分别添加了两个下画线“__”，这些方法统称“魔术方法”（Magic Method）


# __new__	 创建类并返回这个类的实例
# __init__ 可理解为“构造函数”，在对象初始化的时候调用，使用传入的参数初始化该实例
# __del__	可理解为“析构函数”，当一个对象进行垃圾回收时调用
# __metaclass__	定义当前类的元类
# __class__	查看对象所属的类
# __base__	获取当前类的父类
# __bases__	获取当前类的所有父类
# __str__	定义当前类的实例的文本显示内容
# __getattribute__	定义属性被访问时的行为
# __getattr__	定义试图访问一个不存在的属性时的行为
# __setattr__	定义对属性进行赋值和修改操作时的行为
# __delattr__	定义删除属性时的行为
# __copy__	定义对类的实例调用 copy.copy() 获得对象的一个浅拷贝时所产生的行为
# __deepcopy__	定义对类的实例调用 copy.deepcopy() 获得对象的一个深拷贝时所产生的行为
# __eq__	定义相等符号“==”的行为
# __ne__	定义不等符号“!=”的行为
# __lt__	定义小于符号“<”的行为
# __gt__	定义大于符号“>”的行为
# __le__	定义小于等于符号“<=”的行为
# __ge__	定义大于等于符号“>=”的行为
# __add__	实现操作符“+”表示的加法
# __sub__	实现操作符“-”表示的减法
# __mul__	实现操作符“*”表示的乘法
# __div__	实现操作符“/”表示的除法
# __mod__	实现操作符“％”表示的取模(求余数)
# __pow__	实现操作符“**”表示的指数操作
# __and__	实现按位与操作
# __or__	实现按位或操作
# __xor__	实现按位异或操作
# __len__	用于自定义容器类型，表示容器的长度
# __getitem__	用于自定义容器类型，定义当某一项被访问时，使用 self[key] 所产生的行为
# __setitem__	用于自定义容器类型，定义执行 self[key]=value 时产生的行为
# __delitem__	用于自定义容器类型，定义一个项目被删除时的行为
# __iter__	用于自定义容器类型，一个容器迭代器
# __reversed__	用于自定义容器类型，定义当 reversed( ) 被调用时的行为
# __contains__	用于自定义容器类型，定义调用 in 和 not in 来测试成员是否存在的时候所产生的行为
# __missing__	用于自定义容器类型，定义在容器中找不到 key 时触发的行为

class A():
    def __init__(self, data=1):
        self.data = data

    def __iter__(self):
        return self

    def f1(self):
        raise StopIteration()

    def __next__(self):
        if self.data > 3:  # 循环的中止
            raise StopIteration()
        else:
            self.data = self.data + 1  # 2,3,4,
            return self.data

a = A()
print(a)
print(type(a))
for i in A():
    print(i)

