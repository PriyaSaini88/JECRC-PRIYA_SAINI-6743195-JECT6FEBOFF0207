'''
Abstraction: 
    Hiding the internal implementation and showing only functionality to end user.

Abstract Method :
    If a method or a function consists of only declarartion not definition then it will be called as  "Abstract Method"

Abstract Class:
    If a class consits of at least one abstract method, it will be called as "Abstract Class".

Concret Class:
    It consists of zero(0) abstract method. 

abc: Module
ABC: Absract Base Class             

''' 

from abc import ABC, abstractmethod 

class ATM(ABC):  ## Abstract Class
    @abstractmethod
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_bal(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass


class SBI_ATM(ATM): ## concret class
    def generate_pin(self):
        print('It is used to generate ATM pin')

    def forget_pin(self):
        print('Not able to remember the pin! Then forget now!')

    def check_bal(self):
        print('No balance is there in your account!')

    def withdraw(self):
        print('Do not withdraw money! Please!')

    def deposit(self):
        print('Save money by giving it to me!')   

obj = SBI_ATM()
obj.generate_pin()
obj.forget_pin()
obj.check_bal()
obj.withdraw()
obj.deposit()
                     