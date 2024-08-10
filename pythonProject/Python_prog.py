    #create a sum() so it can take 2 arguments to do sum
"""def sum(a,b):
        print(a+b)
a=int(input())
b=int(input())
sum(a,b)"""

#write a python function to sum all the numbers in a list
#sample list: [8,2,3,0,7]
#expected output:[20]

"""def sum(number):
    total=0
    for x in number:
        total = total + int(x)
    print(total)
number=list(input())
sum(number)"""

"""def sum(number):
    total=0
    for x in number:
        total = total + int(x)
    print(total)
number=[8,2,3,0,7]
sum(number)

#write a function to multiply all the elements in a collection
def mul(number):
    total=1
    for x in number:
        total = total * x
    print(total)
number=[1,2,3,4]
mul(number)

#write a python function to print even numbers from the given list
#sample list:[1,2,3,4,5,6,7,8,9]
#output:[2,4,6,8]
def even(numbers):
    list=[]
    for x in numbers:
        if x%2==0:
            list.append(x)
    print(list)
numbers = [1, 2, 3, 4,5,6,7,8,9]
even(numbers)

#write a function that converts a decimal number into binary numbers
def dec(number):
    if number>1:
        dec(number//2)
    print(number%2,end="")
dec(6)

def dec(number):
    if number>1:
        dec(number//2)
    return(number%2)
print(dec(6))

sum=10
def f(x):
    return x+sum
print(f(5))"""

"""return:- return is a special keyword that you can use inside a function or method to send the functon back to the caller."""
#len("hello")
#type("hello")
#we need to use the print statement in order to see the value returned
"""def f1(x):
    print(x)
f1(10)"""

"""def f2(x):
    return(x)
f2(10)""" #it wont return any value
"""print(f2(10))""" #it prints the value

#what is the purpose of return
"""when you return the value, you can decide what you gonna do with the value"""
"""x=len(input("enter the string: "))
print(x**2)"""

"""def f2(x):
    print(x)
print(f2(10))""" #->none
#why we are getting none?
"""when i use print(x) and given the argument f1(20) the 20 will get to the f2(x)place and first prints the 20"""
"""first the function is called it goes to function and prints the value then the last print statement is empty so it prints none"""

"""def f3(x):
    return(x)
print(f3(10))"""
#then it returns only the value

"""sum=10
def fun_sum(x):
    return x+sum
print(fun_sum(100))"""

"""sum=10
def fun_sum(x):
    a=x+sum # returns none 
print(fun_sum(100))"""

"""sum=10
def fun_sum(x):
    a=x+sum
    return a #prints 110 as value of a is returnes to the function and function is printed
print(fun_sum(100))"""

#write a program to print sum of range of numbers
#sample input: 7
#expected output:28

"""num=int(input())
sum=0
for i in range(0,num+1):
    sum=sum+i
print(sum)"""

"""num=int(input())
sum=sum(range(1,num+1)) #1 as in start value and num+1 is end value
print(sum)"""

#list comprehension:
"""it offers a smaller line of code that you can create a new list from the existing list"""
"""list_friuts=["Apple","banana","kiwi","cherry","anar"]
#print the fruits with letter "a" in it and store it in new list
letter_a=[]
for x in list_friuts:
    if "a" in x[0:1]:
        letter_a.append(x)
print(letter_a)"""

"""list_friuts=["Apple","banana","kiwi","cherry","anar"]
#new_list=[items(i) for items(i) in "collecction name"]
new_list=[x for x in list_friuts if "e" in x]
print(new_list)"""

#print the list without banana in it
"""list_friuts=["Apple","banana","kiwi","cherry","anar"]
new_list=[x for x in list_friuts if x!="banana"]
print(new_list)"""

#take as set of numbers being sepated with thw spaces
"""user=input().split()
print(user)
print(type(user))"""
#how to convert this string of elements in list to integer?
"""user=input().split()
print(user)
print(type(user))
number=[]
for x in user:
    number.append(int(x))
print(number)
print(type(number))"""

#user=input().split()
"""number=tuple(map(int,input().split()))
print(number)"""
"""
double=tuple(map(lambda a:a*2, map(int,input().split())))
print(double)"""
"""map(int,input().split())--> map storing entire thing/data, if we want it to be in a readable format,we need to add tuple,list,set"""

#---------------------------------------------
"""filter()-> collection_name(filter(function,iterable))"""
"""filter gives output of the collection if the condition is true"""
age=[10,20,30,40,50]
"""def adult(x):
    if x>=18:
        return x
f1=list(filter(adult,age))
print(f1)"""
"""f1=list(filter(lambda a : a >=18,age))
print(f1)"""

#how can i give more expressions when i am using the conditional statements.
#can we use logical operators in lambda
"""f1=list(filter(lambda a : a >=18 and a<=40,age))
print(f1)"""
"""f2=list(filter(lambda a:18<=a<=40,age))
print(f2)
#list comprehension,lambda,map,filter along with sending 1 function as argument to other function
age=[10,20,30,40,50]
def adult(x):
    if x>=18:
        return x
f1=list(map(adult,age))
print(f1)"""

#regular expressions is a built in package which is known as "re"
#why do we use regular expressions: RegEx is a sequence of characters that forms a search pattern
"""how can we import a RegEx"""

"""import re
text="hello world!"
#search whether the word is present or not
x= re.search("world!$",text)
print(x)"""

#RegEx functions:
"""findall()-->returns a list containing all matches
search-->returns a match object
split-->returns a list
sub-->replace one or many matches with the string"""

"""self: is nothing but a pointer,by default it will take you to the expression"""
