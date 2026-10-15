# 1. Two Sum (Easy) | Array, Hash Map
# Brute Force: nested loops -> Time O(n^2) | Space O(1)
# Optimal: hash map (value -> index) -> Time O(n) | Space O(n)
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            partner = target - num
            if partner in seen:
                return [seen[partner], i]
            seen[num] = i
        return []


# 217. Contains Duplicate (Easy) | Array, Hash Set
# Brute Force: nested loops -> Time O(n^2) | Space O(1)
# Optimal: set of seen numbers -> Time O(n) | Space O(n)
class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# 121. Best Time to Buy and Sell Stock (Easy) | Array, Greedy
# Approach: ek pass me min_price track karo, har din ka profit check karo
# Time O(n) | Space O(1)
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            current_profit = price - min_price

            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit