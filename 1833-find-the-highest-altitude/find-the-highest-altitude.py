class Solution(object):
    def largestAltitude(self, gain):
        current_num = 0
        max_total = 0

        for num in gain:
            current_num += num
            if max_total < current_num:
                max_total = current_num
        return max_total    

        