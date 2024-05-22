import unittest
from bank_account import BasicAccount, SavingsAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.basic_account = BasicAccount("John Doe", "123456", 1000)
        self.savings_account = SavingsAccount("Jane Doe", "654321", 1000)

    def test_deposit(self):
        self.basic_account.deposit(500)
        self.assertEqual(self.basic_account.get_balance(), 1500)

    def test_withdraw(self):
        self.basic_account.withdraw(200)
        self.assertEqual(self.basic_account.get_balance(), 800)
        with self.assertRaises(ValueError):
            self.basic_account.withdraw(1000)

    def test_transfer(self):
        self.basic_account.transfer(300, self.savings_account)
        self.assertEqual(self.basic_account.get_balance(), 700)
        self.assertEqual(self.savings_account.get_balance(), 1300)

    def test_apply_interest(self):
        self.savings_account.apply_interest()
        self.assertEqual(self.savings_account.get_balance(), 1020)

    def test_withdraw_savings(self):
        self.savings_account.withdraw(100)
        self.assertEqual(self.savings_account.get_balance(), 900)
        self.savings_account.withdraw(100)
        self.savings_account.withdraw(100)
        with self.assertRaises(ValueError):
            self.savings_account.withdraw(100)

    def test_reset_withdrawals(self):
        self.savings_account.withdraw(100)
        self.savings_account.withdraw(100)
        self.savings_account.withdraw(100)
        self.savings_account.reset_withdrawals()
        self.savings_account.withdraw(100)
        self.assertEqual(self.savings_account.get_balance(), 600)

if __name__ == '__main__':
    unittest.main()
