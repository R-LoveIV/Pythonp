class BankAccount:
    
    def __init__(self, int_rate, balance): 

        def deposit(self, amount):
            self.balance += amount
            return self
       
        def withdraw(self, amount):
            if(self.balance - amount) >= 0:
                self.balance -= amount
            else:
                print("Insufficient Funds: Charging a $5 fee")
                self.balance -= 5
            return self
       
        def display_account_info(self):
            print(f"Balance: {self.balance}")
        
            def yield_interest(self):
                if self.balance > 0:
                    self.balance += (self.balance * self.int_rate)
                    return self
        
        
                class User:
                    def __init__(self, name, email):
                        self.name = name
                        self.email = email
                        self.account = BankAccount(int_rate=0.02, balance=0)

                    def make_deposit(self,amount):
                        self.account.deposit(amount)
                        return self
                
                def make_withdrawal(self,amount):
                    self.account.withdraw(amount)
                    return self
                
                def display_user_balance(self):
                    print(self.name)
                    self.account.display_account_info()
                    
                user1 = User("Robert", "robert.gmail")
                user1.make_deposit(100).make_deposit(250).display_user_balance()
                
                user2 = User("D", "D@yahoo.com")
                user2.make_deposit(10000).display_user_balance().withdraw(450).display_user_balance()