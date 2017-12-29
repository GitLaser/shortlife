# -*-coding:utf8-*-
__datetime__ = "2017/11/27 22:31"

def is_dcsl(l):
    '''
    Python习题：Python 判读是不是等差数列，要求算法时间复杂度为O(NlogN)
    :param l:
    :return:
    '''
    if not isinstance(l,list):
        print('请输入一个数组')
        return
    for i in range(len(l)-2):
        if l[i+1]-l[i] != l[i+2]-l[i+1]:
            print('不是等差数列')
            return
    print('是等差数列')

is_dcsl([-2,0,2,4,6,8])

if __name__ == "__main__":
    pass