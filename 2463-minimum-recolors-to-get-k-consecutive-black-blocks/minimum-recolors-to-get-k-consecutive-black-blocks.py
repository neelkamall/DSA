class Solution(object):
    def minimumRecolors(self, blocks, k):
        current_w = 0
        for i in range(k):
            if blocks[i] == 'W':
                current_w += 1
        min_w = current_w

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                current_w += 1
            if blocks[i - k] == 'W':
                current_w -= 1
            if current_w < min_w:
                min_w = current_w
        return min_w        
                              
        