#LeetCode 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return None
        d = dict()
        for index, v in enumerate(nums):
            res = target - v
            if res in d:
                return [index, d[res]]
            d[v] = index
        return None
