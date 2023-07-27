from abc import ABC , abstractmethod

class RBI(ABC):
    @abstractmethod
    def roi(self):
        pass

class SBI(RBI):
    def roi(self):
        print("8.5")

class HDFC(RBI):
    def display(self):
        print("Welcome hdfc")

    def roi(self):
        print("7.5")

sbi = SBI()
sbi.roi()
hdfc = HDFC()
hdfc.roi()
hdfc.display()
