class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
#        def rec(l: int, r: int) -> int:
#            if l > r:
#                return 0
#            m_h, m_i = heights[l], l
#            for i in range(l, r + 1):
#                if heights[i] < m_h:
#                    m_h = heights[i]
#                    m_i = i
#            m_a = m_h * (r - l + 1)
#            return max(m_a, rec(l, m_i - 1), rec(m_i + 1, r))
#        return rec(0, l-1)

#Stack
        m_a = 0
        s = [-1]
        for i in range(l):
            while s[-1] != -1 and heights[i] <= heights[s[-1]]:
                h_i = s.pop()
                m_a = max(m_a, heights[h_i] * ((i - 1) - (s[-1] + 1) + 1))
            s.append(i)
        while s[-1] != -1:
            h_i = s.pop()
            m_a = max(m_a, heights[h_i] * ((l - 1) - (s[-1] + 1) + 1))
        return m_a
