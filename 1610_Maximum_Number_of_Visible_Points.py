class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        vrange = angle
        output, same = 0, 0
        X, Y = location[0], location[1]
        for i, point in enumerate(points):
            x, y = point[0], point[1]
            if x == X:
                if y == Y:
                    same += 1
                elif y > Y:
                    angles.append(90)
                else:
                    angles.append(270)
            else:
                slope = (y-Y)/(x-X)
                angle = atan(slope) * 180 / pi
                if angle >= 0:
                    if x < X:
                        angle += 180
                else:
                    if x > X:
                        angle += 360
                    else:
                        angle += 180
                angles.append(angle)
        angles.sort()
        alen, i, j, visible = len(angles), 0, 1, 1
        while i < alen:
            angle = angles[i]
            vision = (angle + vrange)
            while visible < alen:
                if angle <= angles[j] <= vision:
                    visible += 1
                    j = (j + 1) % alen
                elif j < i and angle <= (angles[j] + 360) <= vision:
                    visible += 1
                    j = (j + 1) % alen
                else:
                    break
            output  = max(output, visible)
            if j == i:
                break
            while i < alen:
                if angles[i] <= angles[j] <= angles[i]+vrange or (j < i and angles[i] <= (angles[j] + 360) <= angles[i]+vrange):
                    break
                else:
                    i += 1
                    visible -= 1
        return output + same
