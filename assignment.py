class Atm:
    balance:int = 5000
    pin:int = 1234
    pin_code = int(input("Enter Your PIN Code: "))
    def check_pin(self,):
        self.pin_code
        if self.pin_code == self.pin:
            print("Your PIN is correct")
            self.check_balance()
        else:
            print("Invalid PIN Code")
    def check_balance(self):
        if self.balance> 0:
            print(f"Your Current Balance is {self.balance}")
        else:
            print("Your balance is 0!")
    def deposite(self,):
        self.pin_code
        if self.pin_code == self.pin:
            amount = int(input("Enter amount to deposite: "))
            self.balance += amount
            print(f"Amount You Enter {amount} is Deposite in your Account")
            self.check_balance()
        else:
            print("Invalid PIN Code")
    def with_draw(self):
        self.pin_code
        if(self.pin_code==self.pin):
            amount = int(input("Enter Amount to Withdraw: "))
            if amount > self.balance:
                print("Amount you Enter is not in your balance")
            else:
                self.balance -= amount
                print(f"You Enter Amount {amount} is with draw from your balance  ")
                self.check_balance()
                





    
            
                
atm1 =  Atm()
# atm1.check_pin()
atm1.deposite()
atm1.with_draw()
print(atm1)
# atm1.check_balance()
# atm1.check_pin(int(input("Enter your pin: ")))
# atm1.deposite()
# atm1.with_draw()



                
        

        
    
    
