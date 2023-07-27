
class student:
    def display(self):
        print("this is student class display")

    def display(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        print(self.num1)
        print(self.num2)

obj = student()
obj.display(12,23)
obj.display()

"""
    noted : python does not support method overloading 
"""