# Unit 8 HW 3
For this homework, it is okay to keep all of your code in one file. Submit this as one file called Unit8HW3.py
## Question 1:
Make a class called Restaurant. The ```__init__()``` method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called ```describe_restaurant()``` that prints these two pieces of information, and a method called ```open_restaurant()``` that prints a message indicating that the restaurant is open.

Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

Extra: Make this more Pythonic and have ```__str__``` and describe restaurant do the same thing in an efficient way.

## Question 2:
Start with your class from Question 1. Create three different instances from the class, and call ```describe_restaurant()``` (or print) for each instance.


## Question 3:
Make a class called User for a computer user. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called ```describe_user()``` that prints a summary of the user’s information. Make another method called ```greet_user()``` that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.

## Question 4:
Start with your program from Question 1. Add an instance attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.

Add a method called ```set_number_served(...)``` that lets you set the number of customers that have been served by some amount. Call this method with a new number and print
the value again.
Add a method called ```increment_number_served(...)``` that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.

## Question 5:
Add an attribute called login_attempts to your User class
from Question 3. Write a method called ```increment_login_attempts()``` that increments the value of login_attempts by 1. Write another method called ```reset_login_attemps()``` that resets the value of ```login_attempts``` to 0. Make an instance of the User class and call ```increment_login_attempts()``` several times. Print the value of ```login_attempts``` to make sure it was incremented properly, and then call ```reset_login_attempts()```. Print ```login_attempts``` again to make sure it was reset to 0.
