from bank_v2 import *

class Bank_v3(Bank_v2):
    def loan(self):
        int(input("Enter amount you want a loan of: "))
        if self.balance >= 10300:
            print("Loan approved.")
        else:
            print("Loan not approved.")