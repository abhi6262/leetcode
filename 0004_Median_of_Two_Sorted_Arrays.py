class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums2, nums1 = nums1, nums2
            m, n = n, m
        i, j = 0, 0
        l, r = 0, m
        while l <= r:
            i = (l + r) // 2
            j = ((m + n) // 2) - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                r = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                l = i + 1
            else:
                if i == 0:
                    ml = nums2[j - 1]
                elif j == 0:
                    ml = nums1[i - 1]
                else:
                    ml = max(nums1[i - 1], nums2[j - 1])
                if i == m:
                    mr = nums2[j]
                elif j == n:
                    mr = nums1[i]
                else:
                    mr = min(nums1[i], nums2[j])
                if (m + n) % 2 == 0:
                    return (ml + mr) / 2
                return max(ml, mr)
