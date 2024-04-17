# Point class goes here
class Point():
    # constructor
    def __init__(self,x_val:int,y_val:int):
        self.x = x_val
        self.y = y_val
        
    # distance method
    # two parameters (self, second point)
    # return Euclidean distance (Pythagorean)
    def distance(self,second_point):
        x_dist_squared = (self.x-second_point.x)**2
        y_dist_squared = (self.y-second_point.y)**2
        return (x_dist_squared+y_dist_squared)**0.5
        
    # start class - make a slope method that returns the slope
    # import math at the top



def main():
    c = Point(3,4)
    print(f"The x coordinate of point c is {c.x}")
    print(f"The y coordinate of point c is {c.y}")
    # I have created an instance of the class Point
    # called c with an x value of 3 and a y value 
    # of 4
    origin = Point(0,0)
    print(f"The x coordinate of point origin is {origin.x}")
    print(f"The y coordinate of point origin is {origin.y}")
    # This x is different - it belongs to the instance origin
    # not the instance c
    # In this case, x is the instance variable of origin
    print(f"The distance between the two points is {c.distance(origin)}")
    

if __name__ == '__main__':
    main()