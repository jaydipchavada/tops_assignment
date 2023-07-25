class A:
    def inputA(self):
        self.num1 = int(input("Enter number 1: "))
        self.num2 = int(input("Enter number 2: "))

class B(A):
    def addition(self):
        return self.num1 + self.num2

class C(A):
    def multiplication(self):
        return self.num1 * self.num2
    def division(self):
        return self.num1 / self.num2


b = B()
c = C()

b.inputA()
print(b.addition())

c.inputA()
print(c.multiplication())
print(c.division())
