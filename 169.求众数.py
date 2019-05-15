#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (58.42%)
# Total Accepted:    33.2K
# Total Submissions: 56.8K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2

# 方法1:从第一个数字开始循环，对出现的数字做count得出结果
# 方法2:开一个map或者set，把出现的数字放进去，然后最后取出最大的数字
# 方法3:
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        return sorted(m.items(),key=lambda x:x[1]).pop()[0]
            

        

