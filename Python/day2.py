# # # # # # square = [**2]
# # # # # # reverse [::-1]

# # # # # #str = '937492837software@#$&^%&@'
# # # # # #op = ''
# # # # # #for i in str:
# # # # # #    if i.isalnum():
# # # # # #        op = op+i
# # # # # # print (op[::-1])


# # # # # # str = 'HELLO software'
# # # # # # op = ''
# # # # # # for i in str :
# # # # # #     if i.isupper():
# # # # # #         op = op+i.lower()
# # # # # #     else:
# # # # # #         op = op+i.upper()
# # # # # # print (op[::-1])

# # # # # # str = 'softwaretest9832746879493'
# # # # # # list = sorted(str)
# # # # # # op = ''.join(list)
# # # # # # print(op)

# # # # # # str = 'softwaretest9832746879493'      
# # # # # # al = []
# # # # # # num = []
# # # # # # for i in str:
# # # # # #     if i.isalpha():
# # # # # #         al.append(i)
# # # # # #     else:
# # # # # #         num.append(i)
# # # # # # op = ''.join(sorted(al)+sorted(num))
# # # # # # print(op)

# # # # # # str = 'apple','mango','banana','grapes','mango','banana','grapes'
# # # # # # duplicates = []
# # # # # # seen = set()
# # # # # # for i in str:
# # # # # #     if i in seen:
# # # # # #         duplicates.append(i)
# # # # # #     else:
# # # # # #         seen.add(i)
# # # # # # op = ''.join(duplicates)
# # # # # # print(op)

# # # # # # strr = 'Banglore'
# # # # # # dict = {}
# # # # # # op = ''
# # # # # # for i in strr:
# # # # # #     dict[i] = dict.get(i,0)+1
# # # # # # for k,v in dict.items():
# # # # # #     op = op + k + str(v)
# # # # # # print(op)

# # # # # # str = 's2higb3211kjb2h31kj2h3g1'
# # # # # # op = ''
# # # # # # x=1
# # # # # # for i in str:
# # # # # #     if i.isnumeric():
# # # # # #         x = int(i)
# # # # # #     else:
# # # # # #         d=i
# # # # # #         op = op + x*d
# # # # # # print(op)        

# # # # # # list = []
# # # # # # for i in range(1,20):
# # # # # #     if i%2==0:
# # # # # #         list.append(f'{i} = {i * i}')
# # # # # # print(list)

# # # # # # dict = {}
# # # # # # for i in range(1,20):
# # # # # #     if i%2==0:
# # # # # #         # dict[i] = 1
# # # # # #         dict[i] = i * i
    
# # # # # # print(dict)

# # # # # class product:
# # # # #     def show(self):
# # # # #         print('the name of the product ',self.name)
# # # # #         print('the price of the product ',self.price)
# # # # # obj = product()
# # # # # obj.name = 'mobile'
# # # # # obj.price = 900000
# # # # # obj.show()

# # # # class product:
# # # #     def __init__(self,name,price,category):
# # # #         self.name = name
# # # #         self.price = price
# # # #         self.category = category
# # # #     def show(self):
# # # #         print(self.name)
# # # #         print(self.price)
# # # #         print(self.category)



# # # # obj = product('mobile', 900000, 'electronics')
# # # # obj.show()

# # #INHERITANCE

# # # class school:
# # #     def show(self):
# # #         print(self.name)
# # #         print(self.add)
# # # class IIT(school):
# # #     def display (self):
# # #         print("Welcome to IIT Bombay")

# # # obj = IIT()
# # # obj.name = 'DAVEY'
# # # obj.add='Pune'
# # # obj.show ()
# # # obj.display()

# # # MULTILEVEL INHERITANCE
# # class school:
# #     def show(self):
# #         print(self.name)
# #         print(self.add)
# # class IIT(school):
# #     def display (self):
# #         print("Welcome to IIT Bombay")
# # class groundchild(IIT):
# #     def printdetails(self):
# #         print("Welcome to IIT Bombay Groundchild")

# # obj = groundchild()
# # obj.name = 'DAVEY'
# # obj.add='Pune'
# # obj.show ()
# # obj.display()
# # obj.printdetails()

# ## #MULTIPLE INHERITANCE
# class parent1:
#     def show(self):
#         print('this is parent class school')

# class parent2:
#     def display(self):
#         print('this is parent class IIT')


# class child(parent1, parent2):
#     def printdetails(self):
#         print('this is child class')

# obj = child()
# obj.show()
# obj.display()
# obj.printdetails()

# class product:
#     def show(self):
#         print(self.name)
#         print(self.price)

# class IIT(product):
#     def show (self):
#         print("Welcome to IIT Bombay")

# obj = IIT()
# obj.name = 'DAVEY'
# obj.price = 900000
# obj.show ()

# class product:
#     def show(self,name = ''):
#         print('this is very good product')

# obj = product()
# obj.show()
# obj.show('Laptop')

