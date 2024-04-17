# Unit 8 HW 1
For this homework, it is okay to keep all of your code in one file. Submit this as one file called Unit8HW1.py
## Question 1:
Write a class definition for a vehicle. A vehicle is defined by attributes:
* Number of wheels
* Number of occupants
* Color

Decide the type of each data attribute and document this

## Question 2:
Create 2 vehicle instances using the class we wrote previously. 
* One red vehicle with 2 wheels, and 1 occupant
* One green vehicle with 18 wheels, and 3 occupants
* Print the first one's number of occupants
* Print the second one's color

## Question 3:
Add on to the code from above for class Vehicle.
Create another method for the vehicle class named add_n_occupants, which takes in an int n. 
When called, self's number of occupants increases by n. It returns the total occupants after the increase. 
For example,

```
v1 = Vehicle(4,2,'blue')
print(v1.occ)   # prints 2
print(v1.add_n_occupants(3))   # prints 5
print(v1.occ) # prints 5
```

## Question 4:
Add another data attribute to the Vehicle class, called max_occupancy,
which is always 5. This attribute is not passed in as a parameter, but 
is defined in the init.
Modify the add_n_occupants methods such that if adding the occupants exceeds the max_occupancy allowed for that vehicle, 
  * you do not perform the increase, and
  * you raise a ValueError with an appropriate message

## Question 5:
Modify the Vehicle class __init__ such that if a vehicle is created without specifying a color then the color is set to "black".
(Hint: remember default parameters?)
