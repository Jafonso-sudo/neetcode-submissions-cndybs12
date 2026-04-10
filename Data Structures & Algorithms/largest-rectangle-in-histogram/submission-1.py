# Bug
# - Initially, wasn't popping from the stack causing an infinite loop
# - IMPORTANT CONCEPTUAL BUG: When I add to the stack, I should subtract the length in the stack
#   Basically imagine we have [1, 7, 2, 2, 4]
#   Initially I was outputting 7 because I would be storing in the 2 after pos 2 instead of 1
#   So I need to subtract from the number I'm storing the number I'm popping
#   But it's more than that actually, I need to keep track of the width accounting for the previous pops of others

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        tallest = []
        res = 0
        heights.append(0)
        
        for r, h in enumerate(heights):
            cur_w = 0
            while tallest and tallest[-1][1] >= h:
                t_w, t_h = tallest.pop()
                cur_w += t_w
                res = max(res, t_h * cur_w)
            tallest.append([cur_w + 1, h])
        
        return res