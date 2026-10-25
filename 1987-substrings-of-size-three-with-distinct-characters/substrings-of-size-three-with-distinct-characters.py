class Solution(object):
    def countGoodSubstrings(self, s):
        count = 0
        if len(s) < 3:
            return 0
        k = 3

        for i in range(k, len(s) + 1):
            window = s[i - k : i]
            if len(set(window)) == k:
                count += 1
        return count        

        