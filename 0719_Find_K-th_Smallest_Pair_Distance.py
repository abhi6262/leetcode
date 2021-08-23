class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            l, c = 0, 0
            for i, v in enumerate(nums):
                while v - nums[l] > guess:
                    l += 1
                c += i - l
            return c >= k
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = (l + r) // 2
            if possible(m):
                r = m
            else:
                l = m + 1
        return l
