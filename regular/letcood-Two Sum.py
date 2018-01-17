# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/14 15:50"

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 这种方法可以 但是太慢
        if len(nums) <=1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [i,buff_dict[nums[i]]]
            else:
                buff_dict[target-nums[i]] = i



A=Solution()
print(A.twoSum([0,4,3,0],0))

