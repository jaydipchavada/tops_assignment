class student :
    def input(self,fname,subject):
        self.fname = fname
        self.subject = subject

    def display(self):
        print("name : ",self.fname)
        print("subject : ",self.subject)

obj = student()
obj.input("jaydip","python")
obj.display()