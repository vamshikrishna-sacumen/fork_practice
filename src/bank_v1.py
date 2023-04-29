import abstract

class Bank_v1(abstract.bank):
    bank_name = 'Axis'
    bank_branch = 'Guwahati'
    bank_roi = 6
    def __init__(self, name, ac_num, age, address, balance):
        self.name = name
        self.ac_num = ac_num
        self.age = age
        self.address = address
        self.balance = balance

    @classmethod
    def display_generic(cls):
        print(f'Bank name is {cls.bank_name}')
        print(f'Bank Branch is {cls.bank_branch}')
        print(f'Bank Rate of Interest is {cls.bank_roi}')

    @staticmethod
    def get_withdrawl_amount():
        amount = int(input('Enter the amount you want to withdraw: '))
        return amount
    
    def display_specific(self):
        print(f'Name of the customer is {self.name}')
        print(f'Age of the customer is {self.age}')
        print(f'Address of the customer is {self.address}')
        print(f'Account number of the customer is {self.ac_num}')
        print(f'Customer has a total balance of {self.balance} indian rupees.')
    
    def withdraw(self):
        withdraw_amount = self.get_withdrawl_amount()
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print(f'Withdrawl successfull. Your current balance is {self.balance}')
        else:
            print("Insufficient Balance.")

    def deposite(self):
        deposite_amount = int(input("Enter the amount you want to make a deposite: "))
        self.balance += deposite_amount
        print(f'Deposite successfull. Your current balance is {self.balance}')
if __name__ == '__main__':
    obj = Bank_v1('Sourabh', 123456789, 25, 'Assam, Barpeta', 550000)
    print("Bank details are as follows\n")
    obj.display_generic()
    print("*"*30)
    print("Customer details are as follows\n")
    obj.display_specific()
    print("*"*30)
    print("calling withdraw method")
    obj.withdraw()
    print("*"*30)
    print("calling deposite method")
    obj.deposite()