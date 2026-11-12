class Solution(object):
    def maxSubArray(self, nums):
        current = nums[0]
        best = nums[0]
        for num in nums[1:]:
            if current < 0:
                current = num
            else:
                current = current + num
            best = max(current , best)
        return best            
       
        