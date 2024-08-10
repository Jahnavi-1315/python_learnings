#classes and objects
#why are we creating classes and objects?
#how to create a class?
"""to create a class, we are using a keyword called class"""
"""class customer:
    pass
#object creation
c1=customer()
print(c1)
print(type(c1))"""
#what is __main__?
"""is nothing but from which file the class is coming from"""

#attributes
"""these are of 2 types:
1.class attribute: come from class and these attributes accessible by every object(common attributes)
2.object attribute: means unique attributes that can be applicable to particular object"""

"""class customer():
    #create class attributes: how?
    #creating the variable inside the class
    Bank_Name="HDFC Bank"
    Branch="Hyderabad"
    State="Telangana"
    IFSC="HDFC000023"
#create an object
c1=customer()
c2=customer()
#how can an object access class attributes?
print(c1.Bank_Name,c1.State)"""

#create methods for class customer
#what are methods?
"""methods are nothing but creating function inside the class"""
class customer():
    #create class attributes: how?
    #creating the variable inside the class
    Bank_Name="HDFC Bank"
    Branch="Hyderabad"
    State="Telangana"
    IFSC="HDFC000023"
    #creating methods
    #before creating the object attributes,we need to initiate object attributes inside the class
    def __init__(self,name,age,initial_amount,account_num):
        #what is __inti__?
        """when you create an object,by default it runs with init method-->initialisation method"""
        self.name=name
        self.age=age
        self.initial_amount=initial_amount
        self.account_num=account_num
    def welcome(self): #when we are creating a function we need to call with arguments,but while creating methods we shouldnot use arguments so we use self,self is used as a reference to the object
        print(f"Hello {self.name}, Welcome to {self.Bank_Name},{self.Branch}")
    def check_balance(self):
        print(f"your balance is {self.initial_amount}")
    def amount_deposit(self,amount):
        self.initial_amount += amount
        print(f"transaction is completed."
              f"{amount} has been credited to {self.account_num}."
              f"the updated balance is {self.initial_amount}")
    def withdraw(self,amount):
        if amount<=self.initial_amount:
            self.initial_amount -= amount
            print(f"transaction is completed."
                  f"{amount} has been debited to {self.account_num}."
                  f"the updated balance is {self.initial_amount}.")
        else:
            print("insufficient balance")
            self.check_balance()


#create an object
c1=customer("python",26,1000,1234567893)
c2=customer("jaanu",21,1000,9876543322)
#how can an object access class attributes?
"""print(c1.Bank_Name,c1.State)
#how can an object access object attribute?
print(c1.initial_amount)
print(c1.name)
#how can an object access the particular method?
c1.welcome()
c1.check_balance()
c1.amount_deposit(100)
c1.withdraw(2000)"""
c2.withdraw(700)
#what is self?
"""it is an extra parameter in the method definition
 class.method(object)
 self acts as a pointer/reference to access the object"""

"""x="hello"
x.upper()""" #to see the built in code of a method click cntrl and click on method

#refer to the steps done in my_space google colab

#class
#object
#methods
#inheritence
"""the child object can acquire all the properties and behavior of the parent object"""
#polymorphism
"""one task can be performed in many ways"""
#data abstraction
"""data abstraction and encapsulation are synonyms
giving just a reference to the backend code and restricting the code and just perform the functionality"""
#encapsulation
"""restricting the use of uneccessary data in the methods"""
