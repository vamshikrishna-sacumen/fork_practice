import bank_v1

class Bank_v2(bank_v1.Bank_v1):
    bank_branch = 'Bangalore'
    bank_roi = 7
    def __init__(self, name, ac_num, age, address, balance, pin):
        super().__init__(name, ac_num, age, address, balance)
        self.pin = pin

    @staticmethod
    def get_pin():
        pin = int(input("Enter your pin: "))
        return pin


    def withdraw(self):
        for attempts in range(3,-1,-1):
            entered_pin = self.get_pin()
            if self.pin == entered_pin:
                return super().withdraw()
            else:
                print(f'Incorrect pin. You have only {attempts} attempts left.')
        print("Session aborted.")

    def deposite(self):
        entered_pin = self.get_pin()
        if self.pin == entered_pin:
            return super().deposite()
        else:
            print("Incorrect pin you have to start again.")

if __name__ == '__main__':
    obj = Bank_v2('sourabh', 1234567890, 25, 'Bangalore', 400876, 2691)
    obj.withdraw()
    print("*"*30)
    print("calling deposite method:-")
    obj.deposite()
    print("*"*30)
    print("Bank details are as follows:-\n")
    obj.display_generic()
    print("*"*30)
    print("Customer details are as follows:-\n")
    obj.display_specific()