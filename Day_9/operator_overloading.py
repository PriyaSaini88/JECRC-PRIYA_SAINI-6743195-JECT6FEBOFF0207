'''
--> Operator Overloading : It is a phenomenon of making the operators to work onuser-defined data types 
by invoking respective magic methods.

--> Magic Method / Dundar : it s a special type of methods in which double underscores will be there at the satrting and ending of the method's name.

--Example:
1. __add__
2. __sub__
3.__mul_
4. __floordiv__
5. __truediv__
6. __mod__

--- if we do not use operator overloading then what will happen?
   For using the operators inside user_defined data types we have to use operator overloading

--- syntax:
    class ClassName:
        def __init__(self, val):
            self.val = val

        def __add__(self, ano_obj):
            return self.val + ano_obj.val

    obj1 = ClassName(val1)
    obj2 = ClassName(val2)
    print(obj1 + obj2)     ## obj1. __add__(obj2)

'''

class MyDT:
    def __init__(self, val):
        self.val = val


    def __str__(self):
        return str(self.val) 

    def __add__(self, *ano_obj):
        sum = self.val
        for i in ano_obj:
            sum += i.val
        return MyDT(sum)       

    # def __add__(self, ano_obj):   ## if only two objects are there
    #     return self.val + ano_obj.val

   ## if multiple objects are there    

    def add(self, *args):
        sum = self.val
        for i in args:
            sum += i.val
        return sum     

    # def __sub__(self, ano_obj):
    #     return self.val - ano_obj.val

    def __sub__(self, *ano_obj):
        diff = self.val
        for i in ano_obj:
            diff -= i.val
        return MyDT(diff)    

    def sub(self, *args):
        diff = self.val
        for i in args:
            diff -= i.val
        return diff        

    # def __mul__(self, ano_obj):
    #     return self.val * ano_obj.val 

    def __mul__(self, *ano_obj):
        product = self.val
        for i in ano_obj:
            product *= i.val
        return MyDT(product)


    def mul(self, *args):
        product = self.val
        for i in args:
            product *= i.val
        return product    

    def __floordiv__(self, ano_obj):
        return self.val // ano_obj.val

    def __truediv__(self, ano_obj):
        return self.val / ano_obj.val

    def __mod__(self, ano_obj):
        return self.val % ano_obj.val                   

# print(MyDT(10) + MyDT(20))
print(MyDT(10) + MyDT(20) + MyDT(50) + MyDT(100))
# print(MyDT.add(MyDT(10), MyDT(30), MyDT(70), MyDT(100)))

# print(MyDT(100.36) - MyDT(21.56))
print(MyDT(100.36) - MyDT(21.56) - MyDT(12))
# print(MyDT.sub(MyDT(200), MyDT(50), MyDT(30), MyDT(12))) 

# print(MyDT(10) * MyDT(20))
print(MyDT(10) * MyDT(20) * MyDT(40))
# print(MyDT.mul(MyDT(12), MyDT(20), MyDT(30)))

# print(MyDT(70) / MyDT(20)) 
# print(MyDT(102) // MyDT(13))
# print(MyDT(49) % MyDT(6))      