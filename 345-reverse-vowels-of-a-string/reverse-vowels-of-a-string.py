class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and s[left] not in "aeiouAEIOU":
                left += 1
            while left < right and s[right] not in "aeiouAEIOU":
                right -= 1

            s[left], s[right] = s[right], s[left] 

            left += 1
            right -=1
        return "".join(s)           
