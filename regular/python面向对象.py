# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/24 17:04"

# class Foo:
#     def __init__(self,name):
#         self.name = name
#
#     def get_name(self):
#         print(self.name)
#
#     @staticmethod
#     def bar(arg1):
#         print(arg1)
#
#     @classmethod
#     def get_class(cls):
#         print(cls)
#
# test = Foo('test')
# test.get_name()
# The custom dictionary
class member_table(dict):
    def __init__(self):
        self.member_names = []

    def __setitem__(self, key, value):
        # if the key is not already defined, add to the
        # list of keys.
        if key not in self:
            self.member_names.append(key)

        # Call superclass
        dict.__setitem__(self, key, value)

    def p_self(self):
        print(self)


test=member_table()
test.p_self()
# The metaclass
class OrderedClass(type):
    # The prepare function
    @classmethod
    def __prepare__(metacls, name, bases):  # No keywords in this case
        return member_table()

    # The metaclass invocation
    def __new__(cls, name, bases, classdict):
        # Note that we replace the classdict with a regular
        # dict before passing it to the superclass, so that we
        # don't continue to record member names after the class
        # has been created.
        result = type.__new__(cls, name, bases, dict(classdict))
        result.member_names = classdict.member_names
        return result