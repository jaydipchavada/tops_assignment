"""
30) What relationship is appropriate for Student and Person ?
=>
"""

class student:
    def __init__(self, student):
        self.student = student

class person:
    def __init__(self, person, student):
        self.person = person
        self.student = student

s = student("Python Programming")
p = person("Anjali", s)

print(s.student)
print(p.person)

