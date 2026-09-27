## private data members are accessible only from within the class and not from outside the class.
# class school:
#     def __init__(self):
#         self.__name = 'Davey' #private data
#         self.__add = 'Pune' #private data

#         print(self.__name)
#         print(self.__add)

# obj = school()

## protected data members are accessible from within the class and its subclasses, but not from outside the class.
# class school:
#     def __init__(self):
#         self._name = 'Davey Public School' #protected data
#         self._add = 'Pune' #protected data

#         print(self._name)
#         print(self._add)

# obj = school()

## Public data members are accessible from outside the class, while private and protected data members are not directly accessible from outside the class.

# class school:
#     def __init__(self):
#         self.name = 'Davey Public School' #public data
#         self.add = 'Pune' #public data

#         print(self.name)
#         print(self.add)

# obj = school()

## getter and setter methods are used to access and modify the private data members of a class. They provide a way to encapsulate the data and control access to it.

class mobileinfo:
    def __init__(self):
        self._name = ''

    def getname(self):
        return self._name

    
    def setname(self,name):
        self._name = name
        print('the name of the product is ',self._name)

obj = mobileinfo()
obj.getname()
obj.setname('Iphone 14 Pro Max')