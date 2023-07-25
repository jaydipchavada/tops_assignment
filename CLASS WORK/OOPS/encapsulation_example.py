class shop:
    def setproduct(self,productname):
        self.prductname= productname

    def getproduct(self):
        return self.prductname
    
obj = shop()
obj.setproduct("mobile")
print(obj.getproduct())