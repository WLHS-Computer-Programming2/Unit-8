class Point:
    x = 0
    y = 0

    def __init__(self):
        pass

p1 = Point()
p2 = Point()
print(p1)
print(f"I entered Point.x=4")
Point.x = 4
print(f"p1.x = {p1.x}")
print(f"p2.x is {p2.x}")
print(f"Point.x is {Point.x}")