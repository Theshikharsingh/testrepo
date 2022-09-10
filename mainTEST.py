

#       \d    for number
#       \D  all except number


#  \w  =   it is the combination of these values [a-zA-Z0-9_]

#  \W  =   it is not  the combination of these values [a-zA-Z0-9_] 









# import math
# print('hello world\n')
# print(math.gcd(3,6))

'''if(age)
pko
'''


#  Varialble-  store value  (container)    
# case sensitive,  start with underscore & letter only


# a=34
# b='harry'
# print(type(b))

# print(type(a))


# #   type casting   change value to other data type

# e="31"

# e= int(e)

# print(type(e))

# print(e+3)


# aa= 83
# bb= float(aa)
# cc= str(bb)
# print(cc+ "A")

#   string   

# s= "shikhar"
# ss='''this is
# multi line 
# string'''
# print(s)
# print(s[0:12])

# print(s.strip())

# print(len(s))

# print(s.upper())
# print(s.replace("h","o"))

# s1= "This is a "
# s2= "This is not a"

# print(s1+ s2)

# temp= " This is a {} and he is a good boy by {}".format(s,s1)
# temp= " This is a {0} and he is a good boy by {1}".format(s,s1)
# temp= " This is a {1} and he is a good boy by {0}".format(s,s1)
# print(temp)

# temp= f"this is {s}  an good {s1}"

# print(temp)


#   operators  

# a= 5**2

# a= 5//2

# a=5 % 2

# print(a)

'''  python collection
list 
tuple 
set
dictionary'''



#  List            changable and  allow duplicate also


# lst= [3,5,2,13,6,67]
# var= type(lst)
# lst[2]=57

# lst.append(14)

# lst.insert(1,23)

# lst.pop()

# lst.remove(13)
# lst.sort()

# del lst[1]


# print(lst)
# print(len(lst))
# print(var)



#    tuple                   immutable


# tup= ('shikhar','singh','ram')
# var= type(tup)
# print(var)

# print (tup)


#      set

# s1={4,5,3,6,32,64}

# s2={7,3,56,23}
# s1.add(342)

# s1.update([23,45,67])

# s1.remove(111)           # if no is not present then show error

# s1.discard(111)
# s3= s1.union(s2)
# s3= s1.intersection(s2)
# print(s3)

# print(len(s1))



#    dictionary       key value pair

'''dc={
    "name": "shikhar",
    "roll": 5,
    "subject": "python"
}
'''

# print(dc["name"])

# dc.pop("roll")

# dc.clear()
# del(dc["subject"])

# dc.update({"roll":56})
# print(dc)





#    conditions



'''age=34
if(age>18):
    print("you drive")
elif(age==18):
    print("18 is your age")
else:
    print("not drive")
'''



#     Loops


# for i in range(0,10):
#     print(i)

'''
li= [34,5,"shikhar",45.3]
for i in li:
    print(i)'''



'''i=0
while(i<6): 
    i=i+1
    # if i==3:
    #     break
    if i==2:
        continue
   
    print(f"you are {i}")
'''




#      Function


# def greet():
#     print("hello shikhar")

# greet()


'''def sum(a, b):
    c=a+b
    return c
print(sum(4,5))'''




#      OPPS

# a=input("enter ")
# print(a)



'''class Phone:
    def call(self):
        print("call person")
    def msg(self):
        print("msg to person")

p1= Phone()
p1.call()
'''


#     class and object



'''
class Phone:
    def set_col(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_col(self):
        return self.color
    def show_cost(self):
        return self.cost
    def call(self):
        print("call person")
    def msg(self):
        print("msg to person")

p2= Phone()

p2.set_cost(12499)
p2.set_col("blue")

print(p2.show_col())
print(p2.show_cost())
'''



#     Constructor

'''class Emp:
    def __init__(self,name, age,salary, gender):
        self.name= name
        self.age=age
        self.salary=salary
        self.gender=gender

    def emp_details(self):
        print("name ", self.name)
        print("age ", self.age)
        print("salary ", self.salary)
        print("gender ", self.gender)

e1=Emp("shikhar",22,1499,"male")


e1.emp_details()'''




#     inheritance

'''class Vehicle:
    def __init__(self, milage, cost):
        self.milage= milage
        self.cost=cost
    def show_details(self):
        print("i am a vehical")
        print("milage ", self.milage)
        print("cost ", self.cost)
  

class Car(Vehicle):
    def show_car(self):
        print("car car")

c1=Car(15,200)
c1.show_details()
c1.show_car()'''





#       Polymorphism



#    method overloading and overriding 



'''
class Std:
    
    def sum(self,a=None,b=None,d=None):
        c=0
        if(a!=None and b!=None and d!=None):
            c=a+b+d
        elif(a!=None and b!=None):
            c=a+b
        else:
            c=a
        return(c)
        

aa=Std()
print(aa.sum(3,6))'''







#     method overriding


'''class Vehicle:
    def __init__(self, milage, cost):
        self.milage= milage
        self.cost=cost
    def show_details(self):
        print("i am a vehical")
        print("milage ", self.milage)
        print("cost ", self.cost)
  
  
class Car(Vehicle):
    def __init__(self, milage, cost, tyre,hp):
        super().__init__(milage, cost) 
        self.tyre=tyre
        self.hp=hp


    def show_car_details(self):
        print("i am a car")
        print("tyre ", self.tyre)
        print("hp  ", self.hp)

c1=Car(15,27600,4,350)
c1.show_details()
c1.show_car_details()'''






'''#      Abstraction

from abc import ABC, abstractmethod

class Comp(ABC):
    @abstractmethod
    def process(self):
        pass


com=Comp()
com.process()
'''







#    -------       File Handling      --------


     #  read content

# content=f.readline()   # print line by line file

# content=f.readlines()   # read line separately

'''for line in f:
    print(f.readline()) '''


# print(content)  #   print content

# f.close()    #   close the file

# f = open('firstfile.txt','r') #reading
# f = open('firstfile.txt','a') #appending
# f = open('firstfile.txt', 'w') #write
# f = open('firstfile.txt','x') #create 


#   write

# f=open('firstfile.txt','w')
# f.write("now we are write the text")

# f.close()


#    append

# f=open('firstfile.txt','a')
# f.write("good append")
# f.close()



#     delete file

#  check first then delete 
# import os
'''if os.path.exists('firstfilea.txt'):
    os.remove('firstfilea.txt')
else:
    print("not exist")
'''

# delete a file
# os.remove('firstfile.txt')








#        Regular Expression


import re

nameage='''Jaince is 22 and Theon is 33
Gabriel is 44 and Joey is 21'''


# print(nameage)

#ages= re.findall(r'\d{1,3}',nameage)

#print(ages)


# names= re.findall(r'[A-Z][a-z]*', nameage)

# print(names)

#  create dictionary using two different key and values
'''agedict={}
x=0
for i in names:
    agedict[i]=ages[x]
    x+=1
print(agedict)'''


#   searching the string

'''if re.search('inform','we need to inform him with the latest information'):
    print('available')
else:
    print('not present') '''


#   count all the string

'''allinform= re.findall('inform','we need to inform him with the latest information')
print(allinform)
  '''

#  index of string

'''str='we need to inform him with the latest information'
for i in re.finditer('inform',str):
    l=i.span()
    print(l)
'''


#  find pattern based string

str='sat, hat,jat,mat,pat'
# allstr=re.findall('[shmt]at',str)
# print(allstr)


#  find all but exclude some
somestr=re.findall('[^h-m]at',str)
print(somestr)



#   replace  some  string

'''food= 'hat rat mat pat'

regex= re.compile('[r]at')
food= regex.sub('food',food)
print(food)

'''


#    search

'''randstr='this is a \\dog'
print(re.search(r'\\dog',randstr))'''



#  replace with regex 

'''randstr=#this is a good boy 
#but there
#are so many
regex=re.compile('\n')
randstr=regex.sub(' ',randstr)
print(randstr)
'''


#   find length of string
'''
num='25565'
print('Matches= ', len(re.findall('\d',num)))

print('Matches  5 = ', len(re.findall('\d{5}',num)))
'''


#    match between 5 and 7

'''num=' 123,1234,12345,123456,1234567'

print(" Matches = ", len(re.findall('\d{5,7}',num)))'''





#   check format

'''phn='452-643-6747'
 
if re.search("\w{3}-\w{3}-\w{4}", phn):
    print(" it is the true format number ")
else:
    print(" enter the correct format")
'''


#  check for full name in a correct format

'''if re.search('\w{2,20}\s\w{2,20}','shikhar singh'):
    print("valid name")
else:
    print("not valid")'''



#      check email validity

'''email='shikhae@mdfd.com'
print('Email matches:  ', len(re.findall('[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}',email)))
'''
 










