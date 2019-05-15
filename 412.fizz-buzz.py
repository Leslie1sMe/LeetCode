#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode-cn.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (58.55%)
# Total Accepted:    12.5K
# Total Submissions: 21.2K
# Testcase Example:  '1'
#
# 写一个程序，输出从 1 到 n 数字的字符串表示。
# 
# 1. 如果 n 是3的倍数，输出“Fizz”；
# 
# 2. 如果 n 是5的倍数，输出“Buzz”；
# 
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
# 
# 示例：
# 
# n = 15,
# 
# 返回:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
# 
# 
#
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ls=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:ls.append("FizzBuzz")
            elif i%3==0:ls.append("Fizz")
            elif i%5==0:ls.append("Buzz")
            else:ls.append(str(i))
        return ls

        

