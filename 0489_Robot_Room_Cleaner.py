# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def __init__(self):
        self.visited = set()
        self.d = 'up'

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        dirs = {'up': (-1, 0), 'left': (0, -1), 'down': (1, 0), 'right': (0, 1)}
        n = {'up': 'left', 'left': 'down', 'down': 'right', 'right': 'up'}
        def rec(i: int, j: int):
            robot.clean()
            self.visited.add((i, j))
            direction = self.d
            for k in range(4):
                di, dj = dirs[self.d]
                ni, nj = i + di, j + dj
                t_d = self.d
                if (ni, nj) not in self.visited and robot.move():
                    rec(ni, nj)
                    while self.d != n[t_d]:
                        robot.turnLeft()
                        self.d = n[self.d]
                else:
                    robot.turnLeft()
                    self.d = n[self.d]
            while self.d != n[n[direction]]:
                robot.turnLeft()
                self.d = n[self.d]
            robot.move()
            return
        rec(0, 0)
        return
                    
