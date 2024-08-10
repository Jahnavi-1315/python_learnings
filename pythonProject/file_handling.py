
#file handling
"""handling certain file which is not python such as pdf,json,html et
ti handle the file in python we require a inbuilt function which is "open function"
while you are handlng the file,we will be having 4 modes
modes: r,a,w,x
x-mode: it is used ti create a new file"""
#f=open('trail.txt','x')
#w-mode: over write mode
"""
f=open('trail.txt','w')
f.write("i am applying write mode to mmy file,"
        "if i write one more time my content can be overwritten")
f.close()"""
#r=read mode->to read the content in the file
"""by default when you use the open function, it is in read mode"""
"""f=open('trail.txt','r')
print(f.read())
f.close()"""
#write mode:
"""f=open('trail.txt','w')
f.write("i am overwriting my content in the file,"
        "so the previous content can be overwritten")
f.close()

#a-mode->append mode
f=open('trail.txt','a')
f.write("i am adding extra content at the end of the existing content")
f.close()
#read the file
f=open('trail.txt')
print(f.read())
f.close()
"""


#generators
"""is a function which returns the value of iterator that produce a sequence of values when iterated over"""
#when we have to use the generators?
"""if we want to generate the large sequence of values,then generators are useful,
but we dont want to store all of them in the memory at once"""
#use the keyword "def",instead of "return", we have to use "yield"
"""def my_generator(n):
    value=0
    #loop until the counter is less than n
    while value<n:
        yield value
        value+=1
#iterate over a generator to genarate sequence of values
for value in my_generator(5):
    print(value)"""
'''when you are using integer directly into for loop,it throws an error use it with range function 
when you are using generators then use yield, it supports int object in for loop'''

#pickling:
"""the process of converting any type of object in python 
for example(list,tuple,set,arrays, etc) into bytes is known as pickling"""
"""when it comes to python these pickling conversation is known as serialisation,deserialisation"""
"""pickle coverts the 2-d data into 1-d data and storing it
and in same way 1-d to 2-d"""
#1-dimensional data-point
#2-dimensional data-point
#what is bytes? 0's and 1's is known as bytes
"""to do the pickling,we need to use the package called pickle"""
import pickle
#open a pickle file.txt
pickle_file=open("pickle2.txt","wb") #work and bytes
#use pickle.dump to dump the file
my_dict={'1':"a",'2':"b"}
pickle.dump(my_dict,pickle_file)
#pickle.dump(collection_name,pickle_file name)
pickle_file=open("pickle2.txt",'rb')
#load the data that you have stored
new_dict=pickle.load(pickle_file)
print(new_dict)

"""step1:import the pickle library
step2:creating a pickle file in work and byte mode(wb)
step3: use "pickle.dump" to convert the data
step4:if we want ot read the actual data by using "open("pickle filename","rb")
step5:after that load the data into new_file
step6:print the file"""

#pip