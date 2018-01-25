# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/24 21:05"

from abc import ABCMeta,abstractmethod

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class InfoSection(Section):
    def describe(self):
        print('This is InfoSection.')

class AlbumSection(Section):
    def describe(self):
        print('This is AlbumSection.')

class ChatSection(Section):
    def describe(self):
        print('This is ChatSection.')

class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections=[]
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass
    def addSection(self,section):
        self.sections.append(section)
    def getSection(self):
        return self.sections

class Weibo(Profile):
    def createProfile(self):
        self.addSection(AlbumSection)
        self.addSection(InfoSection)

class Weixin(Profile):
    def createProfile(self):
        self.addSection(ChatSection)
        self.addSection(InfoSection)

if __name__ == "__main__":
    profile_type = input("which is your app ")
    profile = eval(profile_type.title())()
    print(profile.getSection())






