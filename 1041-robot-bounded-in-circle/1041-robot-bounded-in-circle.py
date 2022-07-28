class Solution(object):
    def isRobotBounded(self, instructions):
        x_dir, y_dir = 0, 1
        x, y = 0, 0 
        
        for i in instructions:
            if i == "G":
                x, y = x + x_dir, y + y_dir
            if i == "L":
                x_dir, y_dir = -1 * y_dir, x_dir
            if i == "R":
                x_dir, y_dir = y_dir, -1 * x_dir
        
        return (x == 0 and y == 0) or (x_dir != 0 or y_dir != 1)
    