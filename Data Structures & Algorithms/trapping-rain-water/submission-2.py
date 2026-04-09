class Solution:
    # def trap(self, height: List[int]) -> int:
    #     if len(height) < 3:
    #         return 0
    #     max_r = [0] * len(height)
    #     max_r[-1] = height[-1]
    #     for i in range(len(height) - 2, -1, -1):
    #         max_r[i] = max(max_r[i + 1], height[i])
        
    #     max_l = height[0]
    #     water = 0
    #     for i in range(1, len(height) - 1):
    #         water += max(0, min(max_l, max_r[i + 1]) - height[i])
    #         max_l = max(max_l, height[i])
        
    #     return water

    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        water = 0

        max_l, max_r = height[0], height[-1]
        l, r = 1, len(height) - 2

        while l <= r:
            if max_l < max_r:
                max_l = max(max_l, height[l])
                water += max(0, max_l - height[l])
                l += 1
            else:
                max_r = max(max_r, height[r])
                water += max(0, max_r - height[r])
                r -= 1
        
        return water