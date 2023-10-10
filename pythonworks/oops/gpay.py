from abc import ABC,abstractmethod
class banking(ABC):
    @abstractmethod
    def fundtransfer(self):
        pass
    @abstractmethod
    def balance_enquiry(self):
        pass
    @abstractmethod
    def transactionhistory(self):
        pass
class gpay(banking):
    def fundtransfer(self):
        print("trasnferring....")
    def balance_enquiry(self):
        print("your account balance is...")
    def transactionhistory(self):
        print("transaction history")
obj=gpay()
obj.fundtransfer()
obj.balance_enquiry()
obj.transactionhistory()
    