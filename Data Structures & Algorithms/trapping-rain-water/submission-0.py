class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        max_r = [0] * len(height)
        max_r[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            max_r[i] = max(max_r[i + 1], height[i])
        
        max_l = height[0]
        water = 0
        for i in range(1, len(height) - 1):
            water += max(0, min(max_l, max_r[i + 1]) - height[i])
            max_l = max(max_l, height[i])
        
        return water
