class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        result = []
        result.append(intervals[0])
        for num in intervals:
            if result[-1][1] >= num[0]:
                result[-1][1] = max(result[-1][1], num[1])
            else:
                result.append(num)

        return result