# -*-coding:utf8 -*-
import operator

__author__ = "陈子昂"
__datetime__ = "2018/1/23 15:12"

class Solution:
    def reverse(self, x):
        f = 1 if x>0 else -1
        n = f * int(str(abs(x))[::-1])
        return n if n.bit_length() < 32 else 0

if __name__ == "__main__":
    A=Solution()
    print(A.reverse(-1534))
    print(int(True))

