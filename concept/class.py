class math_operation :
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add (self):
        
        return self.a + self.b        
    


obj = math_operation (1,2)      

print(dir(obj))