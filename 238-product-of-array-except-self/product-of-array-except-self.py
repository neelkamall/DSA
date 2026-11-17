class Solution(object):
    def productExceptSelf(self, nums):

        n = len(nums)
        answer = [1] * n

        # Loop 1: left products
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Loop 2: right products multiply
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * right
            right = right * nums[i]

        return answer
        