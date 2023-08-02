"""
29) What relationship is appropriate for Course and Faculty ?
=>
"""
class Course:
    def __init__(self, subject):
        self.subject = subject

class Faculty(Course):
    def __init__(self,teacher):
        self.teacher = teacher

c = Course("python")
f = Faculty("anjali")

print(c.subject)  
print(f.teacher)  
