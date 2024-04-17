# Unit 8 HW 2

Create a simple fraction class to represent fractions. You will need to decide
what makes a fraction and you need to have the following methods

* an ```__init__```
* a ```__str__```
* an ``` __eq__```
* times
* divide
* add
* subtract


You do not have to worry about reducing fractions to their simplest form. Here
is an example of how your code should work for addition. You can google
butterfly method which works well for two fractions (can get unwieldy for more)

```
f1 = Fraction(1,5)
f2 = Fraction(2,3)
sum = f1+f2
print(sum)
>>> 13/15
```
Notice it prints outs nicely as a string, not a float. Include 3 test cases for each operation and use assert to make sure they pass. For example,

```
f1 = Fraction(1,5)
f2 = Fraction(2,3)
assert(f1+f2 == Fraction(13,15))
```