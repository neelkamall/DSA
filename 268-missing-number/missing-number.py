class Solution(object):
    def missingNumber(self, nums):
        seen = set(nums)
        for num in range(len(nums)+ 1):
            if num not in seen:
                return num
        