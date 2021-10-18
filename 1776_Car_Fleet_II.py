class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        clen = len(cars)
        output = [-1.0] * clen
        stack = [clen-1]
        for i in range(clen-2, -1, -1):
            while stack and cars[stack[-1]][1] >= cars[i][1]:
                stack.pop()
            while stack:
                t = (cars[stack[-1]][0] - cars[i][0]) / (cars[i][1] - cars[stack[-1]][1])
                if t >= output[stack[-1]] >= 0:
                    stack.pop()
                else:
                    break
            if stack:
                output[i] = (cars[stack[-1]][0] - cars[i][0]) / (cars[i][1] - cars[stack[-1]][1])
            stack.append(i)
        return output
