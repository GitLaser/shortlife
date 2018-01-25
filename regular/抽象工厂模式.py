# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/24 23:40"

from abc import ABCMeta,abstractmethod

# 工长模式 简单的说有两大好处
# 1：增加代码通用性，灵活性
# 2：松耦合
# 抽象工厂模式的主要目的是提供一个接口来创建一系列相关对象，而无需指定具体类。

# 简单的说就是，父类不能创建实例，得用子类创建实例。
# 这章内容挺难的，边看书边敲


# 我要开办披萨店，供应印式披萨和美式披萨。
class PizzaFactory(metaclass=ABCMeta):
    '''
    这是父类，由于指明了metaclass=ABCMeta和用了@abstractmethod
    所以它不能创建实例，试一下,报错：TypeError: Can't instantiate abstract class PizzaFactory with abstract methods createNonVegPizza, createVegPizza
    '''
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndiaPizzaFactory(PizzaFactory):
    '''
    之前说了店里有两种披萨，这是印度披萨，它分为蔬菜和非蔬菜两种
    '''
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()

class USPizzaFactory(PizzaFactory):
    #veg 蔬菜
    '''
     这是美国披萨，它分为蔬菜和非蔬菜两种,可以看出，印、美的荤素披萨，可以自定义为不相同的。
    '''
    def createVegPizza(self):
        return MexicanVegPizza()
    def createNonVegPizza(self):
        return HamPizza()

# 先定义蔬菜和非蔬菜两大类披萨
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self,VegPizza):
        pass

class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self,VegPizza):
        pass

# 这里定义细分的4种披萨
class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare ",type(self).__name__)

class ChickenPizza(NonVegPizza):
    '''
    太难了，我都看不下去了
    '''
    def serve(self,VegPizza):
        print(type(self).__name__,"is served with Chicken on ",type(VegPizza).__name__)

class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)

class HamPizza(NonVegPizza):
    '''
    太难了，我都看不下去了
    '''

    def serve(self, VegPizza):
        print(type(self).__name__, "is served with Chicken on ", type(VegPizza).__name__)


# 用户来了！！！该做shi物了
class PizzaStore:
    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndiaPizzaFactory(),USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)

pizza = PizzaStore()
pizza.makePizzas()
# 头疼















