class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        def possible(x):
            l = 0
            c = 1
            s = 0
            while l < n:
                if s + nums[l] <= x:
                    s += nums[l]
                else:
                    if nums[l] > x:
                        return False
                    s = nums[l]
                    c += 1
                l += 1
            return c <= m
        l, r = min(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        return l
