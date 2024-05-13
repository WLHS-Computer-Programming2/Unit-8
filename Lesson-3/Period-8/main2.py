class Point:
    x = 0
    y = 0

    def __init__(self):
        pass


p1 = Point()
p2 = Point()
p1.x = 10
print("p1x",p1.x)
print("p2x",p2.x)
Point.x = 3
print("p1x",p1.x)
print("p2x",p2.x)
# p1 = Point() # (0,0)
# p2 = Point() # (0,0)
# print(p1.x) # 0
# Point.x = 10 # 0
# print(Point.x) # 10
# print(p1.x) # 10???

'''
Shadowing in action
https://pythontutor.com/render.html#code=class%20Point%3A%0A%20%20%20%20x%20%3D%200%0A%20%20%20%20y%20%3D%200%0A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20pass%0A%0A%0Ap1%20%3D%20Point%28%29%0Ap2%20%3D%20Point%28%29%0Ap1.x%20%3D%2010%0Aprint%28%22p1x%22,p1.x%29%0Aprint%28%22p2x%22,p2.x%29%0APoint.x%20%3D%203%0Aprint%28%22p1x%22,p1.x%29%0Aprint%28%22p2x%22,p2.x%29&cumulative=false&curInstr=15&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
'''