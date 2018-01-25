# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/24 20:51"

from abc import ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print('wang wang!')

class Cat(Animal):
    def do_say(self):
        print("Moew Moew!")

class Factory(object):
    def make_sound(self,obj_type):
        return eval(obj_type)().do_say()

if __name__ == "__main__":
    ff = Factory()
    animal = 'Dog'
    ff.make_sound(animal)
