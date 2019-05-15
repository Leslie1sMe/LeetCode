#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (32.20%)
# Total Accepted:    106.7K
# Total Submissions: 331.4K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#
class Solution:
    def reverse(self, x: int) -> int:
       li = list(str(x))
       if li[0] == '-':
            a = li.pop(0)
            li.reverse()
            li.insert(0,a)
            rest = "".join(li)
            answer = int(rest)
            if answer < (-2) ** 31:
                return 0
            return answer
       else:
            li.reverse()
            rest = "".join(li)
            answer = int(rest)
            if answer > (2 ** 31 - 1):
                return 0
            return answer
        

