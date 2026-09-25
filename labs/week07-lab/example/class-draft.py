class ClassName:
    """Class docstring"""
    
    def __init__(self, parameters):
        # Constructor method
        self.attribute = parameters
    
    def method_name(self):
        # Instance method
        self.attribute += 6700
        return self.attribute


myObj = ClassName(67)
print(myObj.attribute)
resultFromMethod = myObj.method_name()
print(resultFromMethod)