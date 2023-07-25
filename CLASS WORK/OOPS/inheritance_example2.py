"""
2) multilevel :
                A
                |
                B
                |
                c

3) multi-ple:
                A         B
                |         |
                -----------
                    |
                    c

4) hierarchical inheritance :
                    A
                    |
            -----------------
            |               |
            b               c


5) hybrid inheritance :
                        A
                        |
                    ------------
                    |         |
                    B         C
                    |
                    D
"""

class a:
    num1=10
    num2=20

    def displaya(self):
        print(self.num1)
        print(self.num2)
class b:
    num3=10
    num4=20

    def displayb(self):
        print(self.num3)
        print(self.num4)
class c(a,b):
    def addition(self):
        self.ans=a.num1 + a.num2
        return self.ans
    
    def multiplication(self):
        self.ans=b.num3 * b.num4
        return self.ans
    """
            A       B
            --------
                |
                c
    """
    
obj = c()
obj.displaya()
# obj.displayb()
print(obj.addition())
print(obj.multiplication())