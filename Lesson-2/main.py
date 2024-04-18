# Point class goes here
class Point:
    # constructor
    def __init__(self,x_value:int,y_value:int):
        self.x = x_value # attribute x takes value of x_value
        self.y = y_value # attrubute y takes value of y_value
    
    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self,point_two):
        return self.x == point_two.x and self.y == point_two.y
    

    # find distance
    def distance(self,point_two:'Point'):
        x_distance_squared = (self.x-point_two.x)**2
        y_distance_squared = (self.y-point_two.y)**2
        return (x_distance_squared+y_distance_squared)**0.5
        
    # find slope
    def slope(self,point_two:'Point'):
        delta_y = point_two.y - self.y
        delta_x = point_two.x - self.x
        return delta_y / delta_x

class Circle:
    pi = 3.1415 # type Circle.pi to use it
    def __init__(self, center:Point,radius:int):
        if isinstance(center,Point) and isinstance(radius,int):
            self.x = center.x
            self.y = center.y
            self.radius = radius
        else:
            raise ValueError("Incorrect types")
    def __str__(self):
        return f"Center: ({self.x},{self.y})\nRadius: {self.radius}"

    def __eq__(self,circle_two):
        return self.radius == circle_two.radius
        
    def area(self):
        return Circle.pi*self.radius**2
    
    def circumference(self):
        return 2*Circle.pi*self.radius
    
def main():
    c = Point(3,4) 
    origin = Point(0,0)
    d = Point(3,4)
    print(c.slope(origin))
    circle_one = Circle(d,5)
    print(circle_one)
    
    

if __name__ == '__main__':
    main()
