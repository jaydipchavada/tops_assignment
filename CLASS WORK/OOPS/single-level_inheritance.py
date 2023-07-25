"""
single-level :
                one class derived proprites of another class
                            A
                            |
                            B


"""

class parent:
    def bike(self):
        print("i have bike")

class child(parent):
    def cycle(self):
        print("i have cycle")

# object creation
obj=child()
obj.bike()
obj.cycle()  
