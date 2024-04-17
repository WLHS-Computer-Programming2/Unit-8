'''
Name:
Date:
Assignment:
'''

# Vehicle class here
class Vehicle:
    def __init__(self,num_wheels:int,num_occupants:int,color:str='black'):
        self.wheels = num_wheels
        self.occ = num_occupants
        self.color = color
        self.max_occupancy = 5

    def add_n_occupants(self,n:int)->int:
        if self.occ + n > 5:
            raise ValueError("Too many occupants")
        else:
            self.occ += n
        return self.occ
    

def main():
    v1 = Vehicle(2,1,"red")
    v2 = Vehicle(18,3,"green")
    print(v1.occ)
    print(v2.color)
    v1.add_n_occupants(3)
    print(v1.occ)
    try:
        v1.add_n_occupants(2)
    except ValueError:
        print(v1.occ)
    v3 = Vehicle(4,2)
    print(v3.color)
if __name__ == '__main__':
    main()



