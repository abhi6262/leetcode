# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        c = 0
        q = deque([])
        if sea.hasShips(topRight, bottomLeft):
            q.append((topRight, bottomLeft))
        while q:
            r = q.popleft()
            if r[0].x == r[1].x and r[0].y == r[1].y:
                c += 1
                if c == 10:
                    break
                else:
                    continue
            c_x, c_y = (r[0].x+r[1].x)//2, (r[0].y+r[1].y)//2
            p1 = Point(c_x, c_y)
            p2, p3 = Point(r[1].x, c_y+1), Point(c_x, r[0].y)
            p4, p5 = Point(c_x+1, r[1].y), Point(r[0].x, c_y)
            p6 = Point(c_x+1, c_y+1)
            if p1.x >= r[1].x and p1.y >= r[1].y and sea.hasShips(p1, r[1]):
                q.append((p1, r[1]))
            if p3.x >= p2.x and p3.y >= p2.y and sea.hasShips(p3, p2):
                q.append((p3, p2))
            if p5.x >= p4.x and p5.y >= p4.y and sea.hasShips(p5, p4):
                q.append((p5, p4))
            if r[0].x >= p6.x and r[0].y >= p6.y and sea.hasShips(r[0], p6):
                q.append((r[0], p6))
        return c
            
            
            
        
