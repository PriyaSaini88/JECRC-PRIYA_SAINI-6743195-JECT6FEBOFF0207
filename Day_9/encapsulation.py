'''
Encapsulation :
 1. It is used to provide security to the data(data means variable/properties and methods present inside class).

 How to provide security to the data ?
  To provide security, we have to use access specifiers.
  Three Access Specifier --
  1. Public, (by defalut)
  2. Protected (soft Barrier '_')
  3. Private

  Access Specifier -- 
      It describe who can access the class members(properties and methods).

'''

## Example for Public Access Specifier 
# class temp:
#     a, b, *c, d = 'HELLO'

#     def greeting(self):
#         print('Good Afternoon User')

# class C2(Temp):
#     pass


#  ## Protected Access Specifier
# class Temp:
#     # soft Barrier
#     _a = 10
#     _b = 'I LOVE PYTHON !'  

# obj = Temp()
# print(obj._b)
# print(obj._a)   


## Private Access Specifier

class Temp:
    
    __a = 100

    def __status(self):
        print('class name is Temp')

obj = Temp()
# print(obj.__a)
# obj.__status()

'''
1. By using syntax
2. get and set Method
3. By using @property decorator(setter)

'''
## By using syntax 

'''
obj_name/class_name._classname__propertyname/__methodname  (Accessing)
obj_name/class_name._Classname__MemberNmae = NewValue (Modifying)

'''
# print(obj._Temp__a)
# print(Temp._Temp__a)
# obj._Temp__status()

# obj._Temp__a = '0123456789'
# print(obj._Temp__a)

# def new_method():
#     print('This is new Method')

# obj._Temp__status = new_method
# obj._Temp__status()

## by using set and get method
# class Temp:
#     __a = 100

#     def __status(self):
#         print('class si temp!')
    
#     def get(self):
#         print(self.__a)

#     def set(self, new_val):
#         self.__a = new_val

# obj = Temp()
# obj.get()
# obj.set(20)
# obj.get()

# print(obj._Temp__a)


## By using @property decorator
class Temp:
    __a = 10

    @property
    def get(self):
        print(self.__a)

    @get.setter  # above method name.setter for decorator name
    def set(self, new_val):
        self.__a = new_val

obj = Temp() 
# obj.get() # will give error
obj.get
# obj.set(10000)  ## will give error as these are not methods they are properties
obj.set = 10000
obj.get

print(obj._Temp__a)


