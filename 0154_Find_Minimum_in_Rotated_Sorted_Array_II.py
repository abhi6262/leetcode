class Solution:
    def findMin(self, nums: List[int]) -> int:
        INF = float('inf')
        def rec(l: int, r: int) -> int:
            if l > r:
                return INF
            if l == r:
                return nums[l]
            m = (l + r) // 2
            if nums[m] < nums[r]:
                return rec(l, m)
            elif nums[m] > nums[r]:
                return rec(m + 1, r)
            else:
                return min(rec(l, m - 1), rec(m + 1, r))
        return rec(0, len(nums) - 1)
