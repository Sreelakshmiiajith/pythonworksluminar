class bank:
    bank_name:str
    acno:str
    person_name:str
    ac_type:str
    balance:int
    def create(self,b_name,accno,p_name,ac_type,bal):
        self.bank_name=b_name
        self.acno=accno
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} has been credited with {amount} avl bal is {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("transaction failed insufficient balance")
        else:
            self.balance-=amount
            print(f"your{self.bank_name} has been debited with {amount} avl balance is {self.balance}")
    def get_balance(self):
        print(f"your available balnce ={self.balance}")
        

obj1=bank()
obj1.create("sbi","2234","vijay","current",4000)
obj1.deposit(2000)
obj1.withdraw(1000)


obj2=bank()
obj2.create("sbi","13247","jhon","savings","49000")
