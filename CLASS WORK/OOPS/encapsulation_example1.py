"""
to hide or prevent data from outside the class

we can use some access specifiers or visibilities modes

=> public
=> private
=> protected

public : by default all the member are public

private : if we declare any varible as private we need to use __in prefix.
        which is only modify by current class.

protected : we need to used _in prefix.
            which is modify by own class and child class.


"""

class products:
    def __init__(self) -> None:
        self.mobile = 5000
        self.__laptop = 30000

    def display(self):
        print("laptop : ",self.__laptop)
        print("mobile : ",self.mobile)

    def changeprice(self,laptopnewprice):
        self.__laptop = laptopnewprice

obj = products()
obj.display()

obj.mobile = 12000
obj.__laptop = 35000

obj.display()

obj.changeprice(45000)

obj.display()