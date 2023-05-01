from bank_v2 import *

class Bank_v3(Bank_v2):
    bank_branch = 'New York'
    def __init__(self, name, ac_num, age, address, balance, pin, adhar):
        super().__init__(name, ac_num, age, address, balance, pin)
        self.adhar = adhar

    @staticmethod
    def get_loan_amount():
        amount = int(input("Enter the amount you want a loan of: "))
        return amount
    
    def display_specific(self):
        super().display_specific()
        print(f'Adhar number of the customer is {self.adhar}')
    
    def loan(self):
        amount = self.get_loan_amount()
        if self.balance >= 30000:
            self.balance += amount
            print("Loan approved.")
            print(f'Your bank account is creadited INR {amount}. Your total balance is INR {self.balance}')
        else:
            print("Loan not approved. Your account does not hold the minimum balance needed for the approval of this loan. Your account should hold minimum of INR 30000")

if __name__ == '__main__':
    obj = Bank_v3('Hambley', 12345, 22, 'New York', 400876, 2961, 'DWFPP01345')
    # obj = Bank_v3('Hambley', 12345, 22, 'New York', 400, 2961, 'DWFPP01345')
    obj.display_specific()
    print("*"*30)
    obj.loan()
    print("*"*30)
    obj.withdraw()
            
