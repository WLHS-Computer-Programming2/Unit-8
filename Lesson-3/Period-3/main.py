class Point:

    num_points_made = 0 # class variable

    def __init__(self):
        self.x = 0
        self.y = 0
        Point.num_points_made += 1

p1 = Point() # (0,0)
p2 = Point() # (0,0)
p1.x = 3 # x is an instance variable
p1.y = 4 # y is an instance variable
print(Point.num_points_made)
print(p1.num_points_made)
print(p2.num_points_made)

