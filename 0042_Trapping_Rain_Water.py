class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        vol = 0
        h_max = height[0]
        num = len(height)
        pos_max = 0
        for i in range(num):
            if height[i] > h_max:
                pos_max = i
                h_max = height[i]
        if h_max == 0:
            return 0
        start_h = height[0]
        for i in range(pos_max):
            if height[i] <= start_h:
                vol += start_h - height[i]
            else:
                start_h = height[i]
        if pos_max < num-2:
            start_h = height[num-1]
            for i in range(num-2, pos_max, -1):
                if height[i] <= start_h:
                    vol += start_h - height[i]
                else:
                    start_h = height[i]
        return vol
