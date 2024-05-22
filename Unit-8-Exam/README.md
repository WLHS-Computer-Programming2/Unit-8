# Unit 8 Take Home Exam

## Task

You are to implement a simple banking system that consists of a basic account and a savings account. See the UML diagram below for details.

## Sample Use
```
# Creating a BasicAccount instance
basic_account = BasicAccount("John Doe", "123456")
basic_account.deposit(1000)
basic_account.withdraw(500)
print(basic_account.get_balance())  # Output: 500.0

# Creating a SavingsAccount instance
savings_account = SavingsAccount("Jane Doe", "654321", 1000)
savings_account.deposit(500)
savings_account.apply_interest()
print(savings_account.get_balance())  # Output: 1530.0

# Transfer between accounts
basic_account.transfer(200, savings_account)
print(basic_account.get_balance())  # Output: 300.0
print(savings_account.get_balance())  # Output: 1730.0
```
## Testing your code

I have attached the same tester file that I will use to test your code. As long as you name your methods the same, you name your module bank_account.py, and you place bank_tester.py in the folder, you should be able to run bank_tester.py and, if your code works, you will see
```
Ran 6 tests in 0.000s

OK
```
### UML Diagram

![UML Diagram](https://github.com/WLHS-Computer-Programming2/Unit-8/blob/main/Unit-8-Exam/Unit8_UML.PNG)
