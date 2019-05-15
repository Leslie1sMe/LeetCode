#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (43.12%)
# Total Accepted:    7.2K
# Total Submissions: 16.6K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 
# 示例:
# 
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
# 
#
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)>12:
            return False
        
        

