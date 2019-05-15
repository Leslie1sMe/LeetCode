#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (39.90%)
# Total Accepted:    20.4K
# Total Submissions: 51K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
# 
# 示例:
# 
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
       pre = ListNode(None)
       pre.next = head
       q = pre
       while q.next:
           if q.next.val == val:
               q.next = q.next.next
           else:
                q = q.next
       return pre.next

