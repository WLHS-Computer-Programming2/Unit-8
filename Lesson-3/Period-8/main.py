class Point:

    num_points_created = 0

    def __init__(self):
        self.x = 0
        self.y = 0
        Point.num_points_created += 1
    
p1 = Point() # (3,4)
p2 = Point() # (0,0)
p1.x = 3
p1.y = 4
print(p1.num_points_created)
print(Point.num_points_created)
print(p2.num_points_created)

# we don't have a variable x that
# belongs to the class, only
# to instances
# print(Point.x) causes an error
