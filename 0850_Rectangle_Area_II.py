class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        rlen = len(rectangles)
        coordinates = []
        M = 10 ** 9 + 7
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            coordinates.append((x1, y1, y2, False))
            coordinates.append((x2, y1, y2, True))
        coordinates.sort()
        area = 0
        intervalset = defaultdict(int)
        lastx = 0
        
        def currwidth():
            if not intervalset:
                return 0
            interval = []
            for key in intervalset:
                if intervalset[key] > 0:
                    interval.append(key)
            interval.sort()
            width = 0
            start, end, i, n = 0, 0, 0, len(interval)
            while i < n:
                start = interval[i][0]
                end = interval[i][1]
                if interval[i][0] <= end:
                    while i < n and interval[i][0] <= end:
                        end = max(end, interval[i][1])
                        i += 1
                    width += end - start
                else:
                    width += end - start
                    i += 1
            return width
                
        for coordinate in coordinates:
            x, y1, y2, isend = coordinate
            width = currwidth()
            area += ((x - lastx) * width % M)
            lastx = x
            if isend:
                intervalset[(y1, y2)] -= 1
            else:
                intervalset[(y1, y2)] += 1
        return area % M
