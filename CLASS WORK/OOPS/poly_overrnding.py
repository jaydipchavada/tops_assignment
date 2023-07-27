
"""
overrinding : two parent and child class both have same name method with same no. of arguments

"""

class vechical:
    def speed(self):
        print("MAX SPEED LIMIT : 80KMH")

class bike(vechical):
    def speed(self):
        print("MAX BIKE SPEED LIMIT : 100KMH")
        return super().speed()

class car(vechical):
    def speed(self):
        print("MAX CAR SPEED LIMIT : 120KMH ")
        return super().speed()
    
obj=car()
obj = bike()
obj.speed()
    