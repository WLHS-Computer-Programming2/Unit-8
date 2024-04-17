# Point class goes here
class Point:
    # constructor
    def __init__(self,x_value:int,y_value:int):
        self.x = x_value # attribute
        self.y = y_value # attrubute
    
    # find distance
    def distance(self,point_two):
        x_distance_squared = (self.x-point_two.x)**2
        y_distance_squared = (self.y-point_two.y)**2
        return (x_distance_squared+y_distance_squared)**0.5
        
    # find slope

def main():
    c = Point(3,4) 
    # you created an instance of the Point class, an object,
    # called c with an x value of 3 and a y value of 4 
    print(c.x) # . is the access operator
    # this prints the x value of the object called c
    print(f"c=({c.x},{c.y})")
    origin = Point(0,0)
    distance = c.distance(origin)
    print(f"The distance between c and origin is {distance}")

if __name__ == '__main__':
    main()
