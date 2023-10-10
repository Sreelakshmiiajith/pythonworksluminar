from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass

class   swift(Car):
    def start(self):
        print("swift starts")
    
    def accelerate(self):
        print("swift accelerate")
    def stop(self):
        print("swift stop")
obj=swift()
obj.start()
obj.accelerate()
