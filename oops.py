# How to define a class?
# class classname:
#           '''documentation class'''
#           variables=>properties/attributes
#           methods=>Actions/Behaviour

#class Student:
    #'''this class is develped by durga for demo purpose'''
    # variables
    # methods
#print(Student.__doc__)
#help(Student)

#this class is develped by durga for demo purpose
#Help on class Student in module __main__:

#class Student(builtins.object)
# |  this class is develped by durga for demo purpose
# |  
# |  Data descriptors defined here:
# |  
# |  __dict__
# |      dictionary for instance variables (if defined)
# |  
# |  __weakref__
# |      list of weak references to the object (if defined)

# Demo to define a class

#class Student:
#    def __init__(self):
#        self.name='Durga'
#        self.rollno=101
#        self.marks=90
#
#    def talk(self):
#        print('Hello my name is:',self.name)
#        print('My Rollno is:',self.rollno)
#        print('My marks are:',self.marks)

#s=Student()
#print(s.name)     #Durga
#print(s.rollno)   #101
#print(s.marks)    #90
#s.talk()

# Hello my name is: Durga
# My Rollno is: 101
# My marks are: 90

#class Student:
#    def __init__(self,name,rollno,marks):
#        self.name=name
#        self.rollno=rollno
#        self.marks=marks
#    def talk(self):
#        print('Hello my name is:',self.name)
#        print('My rollno is:',self.rollno)
#        print('My marks are:',self.marks)
#s1=Student('Piyush',24144,95)
#s2=Student('Sharma',23274,99)
#s1.talk()
#s2.talk()

#Hello my name is: Piyush
#My rollno is: 24144
#My marks are: 95

#Hello my name is: Sharma
#My rollno is: 23274
#My marks are: 99

#-----------------------------------------------------------------------------------------------------------------------------------
# self Variable:

#class Test:
#    def __init__(self):
#        print('Address of object pointed by self:',id(self))
#t=Test()
#print('Address of object pointed by t:',id(t))

#Address of object pointed by self: 2110013103456
#Address of object pointed by t: 2110013103456

#class Test:
#    def __init__(self):
#        print('constructor')
#    def m1(self,x):
#        print('x value is:',x)

#t=Test()  #constructor
#t.m1(10)  #x value is: 10

# self is not a keyword we can use anything. The first argument will be considered as self but not recommended.Not considered good programming practice.


#class Student:
#    def __init__(delf,name,rollno,marks):
#        delf.name=name
#        delf.rollno=rollno
#        delf.marks=marks
#    def talk(kelf):
#        print('Hello my name is:',kelf.name)
#        print('my roll no is:',kelf.rollno)
#        print('my marks are:',kelf.marks)
#s1=Student('Bunny',101,95)
#s1.talk()

#Hello my name is: Bunny
#my roll no is: 101
#my marks are: 95

#-----------------------------------------------------------------------------------------------------------------------------------
# constructor: __init__

#class Test:
#    def __init__(self):
#        print('constructor execution..')

#t1=Test()   #constructor execution..
#t2=Test()   #constructor execution..
#t3=Test()   #constructor execution..

#class Student:
#    def __init__(self,name,rollno,marks):
#        print('creating instance variable and performing initialization')
#        self.name=name
#        self.rollno=rollno
#        self.marks=marks

#s1=Student('Sunny',101,90)  
#s2=Student('Bunny',102,95) 

#print(s1.name,s1.rollno,s1.marks) #Sunny 101 90
#print(s2.name,s2.rollno,s2.marks) #Bunny 102 95 

#creating instance variable and performing initialization
#creating instance variable and performing initialization

#class Test:
#    def m1(self):
#        print('method execution...')

#t=Test()
#t.m1()     #method execution...

#class Test:
#    def __init__(self):
#        print('constructor execution...')
#t=Test()      #constructor execution...  
#t.__init__()  #constructor execution...
#t.__init__()  #constructor execution...
#t.__init__()  #constructor execution...

#class Test:
#    def __init__(self):
#        print('No-arg constructor')
#
#    def __init__(self,x):
#        print('One-arg constructor') # Two methods with  same name most recent will be considered

#t=Test() #TypeError: __init__() missing 1 required positional argument: 'x'

#t=Test(10) #One-arg constructor

#-----------------------------------------------------------------------------------------------------------------------------------
# Mini application to understand oop.

#class Movie:
#    def __init__(self,a,b,c):
#        self.title=a
#        self.hero=b
#        self.heroin=c
#    def info(self):
#        print('Movie Name:',self.title)
#        print('Hero Name:',self.hero)
#        print('Heroin Name:',self.heroin)
#
#list_of_movies=[]

#while True:
#    title=input('Enter Movie Name:')
#    hero=input('Enter Hero Name:')
#    heroin=input('Enter Heroin Name:')
#    m=Movie(title,hero,heroin)
#    list_of_movies.append(m)
#    print('Movie added to the list successfully...')
#    option=input('Do you want to add another movie [Yes|No]:')
#    if option.lower()=='no':
#        break
#print('All Movies Information...')
#for movie in list_of_movies:
#    movie.info()
#    print()

#-----------------------------------------------------------------------------------------------------------------------------------
# Same name for class and method.

#class Test:
#    def Test(self):
#        print('It is some special method')
#t=Test() #constructor will be executed __init__()
#t.Test() #Test() method wiil be executed==>It is some special method

#-----------------------------------------------------------------------------------------------------------------------------------
# Variables

#class Student:
#    shcool_name='Durgasoft'     # Static variable
#    def __init__(self,name,rollno):
#        
#        self.name=name
#        self.rollno=rollno      # Instance variables
#    
#    def info(self):
#        x=10                    # Local variable
#        for i in range(x):
#            print(i)
    
#-----------------------------------------------------------------------------------------------------------------------------------
# Methods

#class Test:
#    @classmethod
#    def m1(cls):
#        print(id(cls))
#
#print(id(Test)) #2010374541408
#Test.m1()       #2010374541408   

#class Student:  
#    schoolname='Durgasoft' 
#    def __init__(self,name,rollno):
#        self.name=name
#        self.rollno=rollno
#    
#    # Instance Method
#    def getStudentInfo(self):
#        print('Student Name:',self.name)
#        print('Student rollno:',self.rollno)
#
#    # Class Method
#    @classmethod
#    def getSchoolInfo(cls):
#        print('School Name:',cls.schoolname)
#
#    # Static Method / general utility method
#    @staticmethod
#    def getSum(a,b):
#        return a+b

#-----------------------------------------------------------------------------------------------------------------------------------
# Various places to declare Instance variables

# 1. Inside constructor by using self

#class Test:
#    def __init__(self):
#        self.a=10
#        self.b=20
#t=Test()
#print(t.__dict__)   #{'a': 10, 'b': 20}

# 2. Inside instance method by using self

#class Test:
#    def __init__(self):
#        self.a=10
#        self.b=20
#    def m1(self):
#        self.c=30
#t=Test()
#t.m1()
#print(t.__dict__)  #{'a': 10, 'b': 20, 'c': 30}

# 3. Outside of the class by using object reference variable

#class Test:
#    def __init__(self):
#        self.a=10
#        self.b=20
#    def m1(self):
#        self.c=30
#t=Test()           #a and b will be added to the object
#t.m1()             #c will be added to the object
#t.d=40             #d will be added to the object
#print(t.__dict__)  #{'a': 10, 'b': 20, 'c': 30, 'd': 40}

#class Test:
#    def __init__(self):
#        self.a=10
#        self.b=20
#    def m1(self):
#        self.c=30
#t1=Test()       #a and b will be added to the t1 
#t1.m1()         #c will be added to the t1   
#t1.d=40         #d will be added to the t1
#t2=Test()       #a and b will be added to the t2 
 
#print(t1.__dict__)  #{'a': 10, 'b': 20, 'c': 30, 'd': 40}
#print(t2.__dict__)  #{'a': 10, 'b': 20}

#-----------------------------------------------------------------------------------------------------------------------------------
# Access,update and delete instance variable:

# Access

# Inside class
#class Test:
#    def __init__(self):
#        self.a=10
#        self.b=20
#    def display(self):
#        print(self.a)
#        print(self.b)
# Outside Class
#t=Test()
#t.display() #10
             #20
              
#print(t.a)  #10
#print(t.b)  #20

# Delete

#class Test:
#    def __init__(self):
#        self.a=10
#        self.b=20
#        self.c=30
#        self.d=40

# Inside class
#    def m1(self):
#        del self.c

#t1=Test()
#t1.m1()
#print('t1:',t1.__dict__) #t1: {'a': 10, 'b': 20, 'd': 40}

# Outside Class
#t2=Test()
#del t2.b,t2.d
#print('t2:',t2.__dict__) #t2: {'a': 10, 'c': 30}

# Update
#class Test:
#    def __init__(self):
#        self.a=10
#        self.b=20

#t1=Test()
#t1.a=888
#t1.b=999

#t2=Test()
#print('t1:',t1.__dict__)  #t1: {'a': 888, 'b': 999}
#print('t2:',t2.__dict__)  #t2: {'a': 10, 'b': 20}

#-----------------------------------------------------------------------------------------------------------------------------------
# Various places to declare static variable:

#class Test:
#    # Inside class
#    a=10    # static variable

#    def __init__(self):
#        # Inside constructor using class name
#        Test.b=20
#    def m1(self):
#        # Inside method using class name
#        Test.c=30
#    @classmethod
#    def m2(cls):
#        # Inside classmethod by using cls/class name
#        cls.d=40
#        Test.e=50
#    @staticmethod
#    def m3():
#        # Inside staticmethod by using classname
#        Test.f=60
#t=Test()
#t.m1()
#Test.m2()
#Test.m3()
#Test.g=70
#print(Test.__dict__)

#-----------------------------------------------------------------------------------------------------------------------------------
# Access static variable:

# 1. Inside constructor by using self or classname

#class Test:
#    a=10
#    def __init__(self):
#        #Inside constructor by using self or classname
#        print(self.a)
#        print(Test.a)
#    def m1(self):
#        #Inside instance method by using self or classname
#        print(self.a)
#        print(Test.a)
#    @classmethod
#    def m2(cls):
#        #Inside classmethod by usng cls or classname
#        print(cls.a)
#        print(Test.a)   
#    @staticmethod
#    def m3():
#        #Inside staticc ethod by using classname
#        print(Test.a)
        
#t=Test()
#Outside class either by using object reference variable or classname
#print(t.a)
#print(Test.a)
#t.m1()
#t.m2()
#t.m3()

#-----------------------------------------------------------------------------------------------------------------------------------
# Modify value of static variable:

#class Test:
#    a=10
#    def __init__(self):
#        Test.a=20
#    def m1(self):
#        Test.a=30
#    @classmethod
#    def m2(cls):
#        cls.a=40
#        Test.a=50
#    @staticmethod
#    def m3():
#        Test.a=60

#t=Test()
#t.m1()
#Test.m2()
#Test.m3()
#Test.a=70
#print(Test.a)

#-----------------------------------------------------------------------------------------------------------------------------------
# Examples of instance and static variable 

#class Test:
#    a=10
#    def m1(self):
#        self.a=888
#t1=Test()
#t1.m1()
#print(Test.a) #10
#print(t1.a)   #888

#class Test:
#    a=10
#    def m1(self):
#        Test.a=888
#t1=Test()
#t1.m1()
#print(Test.a) #888
#print(t1.a)   #888

#class Test:
#    a=10
#    def __init__(self):
#        self.b=20
#t1=Test()
#t2=Test()
#print('t1:',t1.a,t1.b) #t1: 10 20
#print('t2:',t2.a,t2.b) #t2: 10 20
#t1.a=888 # Instance variable
#t1.b=999 # Instance variable
#print('t1:',t1.a,t1.b) #t1: 888 999
#print('t2:',t2.a,t2.b) #t2: 10 20

#class Test:
#    a=10
#    def __init__(self):
#        self.b=20
#
#t1=Test()
#t2=Test()
#print('t1:',t1.a,t1.b)       #t1: 10 20
#print('t2:',t2.a,t2.b)       #t2: 10 20
#Test.a=888
#Test.b=999
#print('t1:',t1.a,t1.b)       #t1: 888 20
#print('t2:',t2.a,t2.b)       #t2: 888 20      
#print('Test:',Test.a,Test.b) #Test: 888 999

#class Test:
#    a=10
#    def __init__(self):
#        self.b=20
#
#t1=Test()
#t2=Test()
#Test.a=888
#Test.b=999
#t1.b=999
#print('t1:',t1.a,t1.b)  #t1: 888 999
#print('t2:',t2.a,t2.b)  #t2: 888 20

#class Test:
#    a=10
#    def __init__(self):
#        self.b=20
#    def m1(self):
#        self.a=888
#        self.b=999
#t1=Test()
#t2=Test()
#t1.m1()
#print('t1:',t1.a,t1.b)  #t1: 888 999
#print('t2:',t2.a,t2.b)  #t2: 10 20

#class Test:
#    a=10
#    def __ini__(self):
#        self.b=20
#    def m1(self):
#        self.a=888
#        self.b=999
#t1=Test()
#t2=Test()
#t1.m1()
#t2.m1()
#print('t1:',t1.a,t1.b)  #t1: 888 999
#print('t2:',t2.a,t2.b)  #t2: 888 999

#class Test:
#    a=10
#    def __init__(self):
#        self.b=20
#    @classmethod
#    def m1(cls):
#        cls.a=888
#        cls.b=999
#t1=Test()
#t2=Test()
#t1.m1()
#print('t1:',t1.a,t1.b)        #t1: 888 20          
#print('t2:',t2.a,t2.b)        #t2: 888 20  
#print('Test:',Test.a,Test.b)  #Test: 888 999 

#-----------------------------------------------------------------------------------------------------------------------------------
# Delete static variable:

#class Test:
#    a=10
#    @classmethod
#    def m1(cls):
#        #del Test.a
#        #del cls.a
#
#del Test.a
#print(Test.__dict__)

#class Test:
#    a=10
#    def __init__(self):
#        Test.b=20
#        del Test.a
#    def m1(self):
#        Test.c=30
#        del Test.b
#    @classmethod
#    def m2(cls):
#        Test.d=40
#        del Test.c
#    @staticmethod
#    def m3():
#        Test.e=50
#        del Test.d
#t=Test()
#t.m1()
#t.m2()
#t.m3()
#print(Test.__dict__)

#class Test:
#    a=10
#t=Test()
#print(t.a)  # 10
#del t.a     # AttributeError: a
#del Test.a  # correct

#-----------------------------------------------------------------------------------------------------------------------------------
# Instance variables vs static variables

#class Test:
#    a=10
#    def __init__(self):
#        self.b=20
#t1=Test()
#t2=Test()
#Test.a=888
#t1.b=999
#print('t1:',t1.a,t1.b)  #t1: 888 999
#print('t2:',t2.a,t2.b)  #t2: 888 20

#-----------------------------------------------------------------------------------------------------------------------------------
# Local variables:

#class Test:
#    @staticmethod
#    def average(list1):
#        result=sum(list1)/len(list1)
#        print('The average:',result)
#    @staticmethod
#    def wish(name):
#        for i in range(10):
#            print('Good evening:',i,name)
#list1 =[10,20,30,40]
#Test.average(list1)     
#Test.wish('Piyush')

#The average: 25.0
#Good evening: 0 Piyush
#Good evening: 1 Piyush
#Good evening: 2 Piyush
#Good evening: 3 Piyush
#Good evening: 4 Piyush
#Good evening: 5 Piyush
#Good evening: 6 Piyush
#Good evening: 7 Piyush
#Good evening: 8 Piyush
#Good evening: 9 Piyush

#class Test:
#    def m1(self):
#        a=10
#        print(a)
#    def m2(self):
#        print(a)
#t=Test()
#t.m1()      #10
#t.m2()      #NameError: name 'a' is not defined

#-----------------------------------------------------------------------------------------------------------------------------------
# Mini Bank Application

#class Customer:
#    '''Customer class developed by Durga for bank operations'''
#    bankname='DURGABANK'
#    def __init__(self,name,balance=0.0):
#        self.name=name
#        self.balance=balance
#    def deposit(self,amount):
#        self.balance=self.balance+amount
#        print('Balance after Deposit:',self.balance)
#    def withdraw(self,amount):
#        if amount>self.balance:
#            print('Insufficient funds...\ncannot perform this operation')
#        else:
#            self.balance=self.balance-amount
#            print('Balance after withdraw:',self.balance)
#
#print('Welcome to',Customer.bankname)
#name=input('Enter your name:')
#c=Customer(name)
#while True:
#    print('d-Deposit\nw-Withdraw\ne-Exit')
#    option=input('Choose your option:')
#    if option.lower()=='d':
#        amount=float(input('Enter amount to deposit:'))
#        c.deposit(amount)
#    elif option.lower()=='w':
#        amount=float(input('Enter amount to withdraw:'))
#        c.withdraw(amount)
#    elif option.lower()=='e':
#        print('Thank you for banking')
#        break
#    else:
#        print('Your option is Invalid...\nplease choose valid option')

#-----------------------------------------------------------------------------------------------------------------------------------
# Instance method:

#class Student:
#    def __init__(self,name,marks):
#        self.name=name
#        self.marks=marks
#    def display(self):
#        print('Hi',self.name)
#        print('Your marks are:',self.marks)
#    def grade(self):
#        if self.marks>=60:
#            print('You got First Grade')
#        elif self.marks>=50:
#            print('You got second grade')
#        elif self.marks>=35:
#            print('You go thirrd grade')
#        else:
#            print('You are failed')
#n=int(input('Enter number of students:'))
#for i in range(n):
#    name=input('Enter your name:')
#    marks=int(input('Enter your marks:'))
#    s=Student(name,marks)
#    s.display()
#    s.grade()

#-----------------------------------------------------------------------------------------------------------------------------------
# Setter and Getter methods:

# Setter method(mutator method):

#def setMarks(self,marks):
#    self.marks=marks

# Getter method(accesor method):

#def getMArks(self):
#    return self.marks

#class Student:
#    def setName(self,name):
#        self.name=name
#    def getName(self):
#        return self.name
#    def setMarks(self,marks):
#        self.marks=marks
#    def getMarks(self):
#        return self.marks
#
#n=int(input('Enter number of students:'))
#students=[]
#for i in range(n):
#    s=Student()
#    name=input('Enter Student name:')
#    marks=int(input('Enter marks:'))
#    s.setName(name)
#    s.setMarks(marks)
#    students.append(s)
#for s in students:
#    print('Hello',s.getName())
#    print('Your marks are',s.getMarks())
#    print()    

#-----------------------------------------------------------------------------------------------------------------------------------
# Class Methods:

#class Bird:
#    wings=2
#    @classmethod
#    def fly(cls,name):
#        print('{} flying with {} wings'.format(name,cls.wings))
#
#Bird.fly('Parrot')
#Bird.fly('Crow')

# Program to track number of objects created for a class

#class Test:
#    count=0
#    def __init__(self):
#        Test.count+=1
#    @classmethod
#    def getNOfObjects(cls):
#        print('The number of objects created:',cls.count)
#
#Test.getNOfObjects()
#t1=Test()
#t2=Test()
#t3=Test()
#t4=Test()
#Test.getNOfObjects()

#The number of objects created: 0
#The number of objects created: 4

#-----------------------------------------------------------------------------------------------------------------------------------
# Static methods:

#class Test:
#    @staticmethod
#    def m1():
#        pass
#Test.m1()

#class DurgaMath:
#    @staticmethod
#    def add(a,b):
#        print('The sum:',a+b)
#    @staticmethod
#    def product(a,b):
#        print('The Product:',a*b)
#    @staticmethod
#    def average(a,b):
#        print('The average:',(a+b)/2)
#
#DurgaMath.add(10,20)        #The sum: 30
#DurgaMath.product(10,20)    #The Product: 200                   
#DurgaMath.average(10,20)    #The average: 15.0  

#-----------------------------------------------------------------------------------------------------------------------------------
#class Test:
#    def m1():
#        print('some method')
#t=Test()
#t.m1()      #Error

# Instance method
#class Test:
#    def m1(x):
#        print('some method')
#t=Test()
#t.m1()      #some method

# Static method
#class Test:
#    def m1():
#        print('some method')
#Test.m1()   #some method

#class Test:
#    def m1(x):
#        print('some method')
#Test.m1()   #Error

#class Test:
#    def m1(x):
#        print('some method')
#Test.m1(10)     #some method

#-----------------------------------------------------------------------------------------------------------------------------------
# Accessing Members of one class inside another class:

#class Employee:
#    def __init__(self,eno,ename,esal):
#        self.eno=eno
#        self.ename=ename
#        self.esal=esal
#    def display(self):
#        print('Employee Number:',self.eno)
#        print('Employee Name:',self.ename)
#        print('Employee Salary:',self.esal)

#class Manager:
#    def updateEmpSal(emp):
#        emp.esal=emp.esal+10000
#        emp.display()

#emp=Employee(100,"Piyush",45000)
#Manager.updateEmpSal(emp)

#Employee Number: 100
#Employee Name: Piyush
#Employee Salary: 55000

#-----------------------------------------------------------------------------------------------------------------------------------
# Inner classes:

#class Outer:
#    def __init__(self):
#        print('Outer Object Creation...')
#    class Inner:
#        def __init__(self):
#            print('Inner Class Object Creation')
#        def m1(self):
#            print('Inner Class Method...')

#o=Outer()   #Outer Object Creation... 
#i=o.Inner() #Inner Class Object Creation 
#i.m1()      #Inner Class Method...

#Outer().Inner().m1()

# Nesting of inner class:

#class Outer:
#    def __init__(self):
#        print('Outer Class Object creation...')
#    class Inner:
#        def __init__(self):
#            print('Inner class Object creation...')
#        class InnerInner:
#            def __init__(self):
#                print('InnerInner class Object creation...')
#            def m1(self):
#                print('Nested Inner class method...')

#o=Outer()          #Outer Class Object creation... 
#i=o.Inner()        #Inner class Object creation...
#ii=i.InnerInner()  #InnerInner class Object creation...
#ii.m1()            #Nested Inner class method...

#Outer().Inner().InnerInner().m1()

#Outer Class Object creation...
#Inner class Object creation...
#InnerInner class Object creation...
#Nested Inner class method...

#class Outer:
#    def __init__(self):
#        print('Outer obj creation...')
#    class Inner:
#        def __init__(self):
#            print('Inner obj creation') 
#        class InnerInner:
#            def __init__(self):
#                print('InnerInner obj creation')
#            @staticmethod
#            def m1():
#                print("Nested Inner class static method")

#Outer().Inner().InnerInner.m1()

# Outer obj creation...
# Inner obj creation
# Nested Inner class static method 

#class Human:
#    class Head:
#        def talk(self):
#            print("talking")
#        class Brain:
#            def think(self):
#                print('thinking')

#human=Human()
#head=human.Head()
#head.talk()         #talking
#brain=head.Brain() 
#brain.think()       #thinking


#Human().Head().talk()           #talking
#Human().Head().Brain().think()  #thinking

#class Human:
#    def __init__(self,name):
#        self.name=name
#        self.head=self.Head()

#    def info(self):
#        print('Hello, my self',self.name)
#        print('I am full busy with')
#        self.head.talk()
#        self.head.brain.think()

#    class Head:
#        def __init__(self):
#            self.brain=self.Brain()
        
#        def talk(self):
#            print('Talking...')

#        class Brain:
#            def think(self):
#                print('Thinking...')

#human=Human("Piyush")
#human.info()

#Hello, my self Piyush
#I am full busy with
#Talking...
#Thinking..

#class Human:
#    def __init__(self,name):
#        print('Humna object creation...')
#        self.name=name
#        self.head=self.Head()
#    def info(self):
#        print('Hello, myself',self.name)
#        print("I'am too busy with")
#        self.head.talk()
#        self.head.brain.think()
#    class Head:
#        def __init__(self):
#            print('Head object creation...')
#            self.brain=self.Brain()
#        def talk(self):
#            print('talking')
#        class Brain:
#            def __init__(self):
#                print('Brain object creation...')
#            def think(self):
#                print('thinking')
#
#human=Human("Piyush")
#human.info()

#class Person:
#    def __init__(self,name,dd,mm,yyyy):
#        print('Person Object creation...')
#        self.name=name
#        self.dob=self.DOB(dd,mm,yyyy)
#    def info(self):
#        print('Name:',self.name)
#        self.dob.display()
#    
#    class DOB:
#        def __init__(self,dd,mm,yyyy):
#            print('DOB Object creation...')
#            self.dd=dd
#            self.mm=mm
#            self.yyyy=yyyy
#        def display(self):
#            print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyyy))            
#p=Person("Piyush",31,3,1999)
#p.info()

#Person object creation...
#DOB object creation...    
#Name: Piyush    
#DOB=31/3/1999  

#-----------------------------------------------------------------------------------------------------------------------------------
# Nested methods:

#class Test:
#    def m1(self):
#        a=10
#        b=20
#        print('The sum:',a+b)
#        print('The produt:',a*b)
#        print('The difference:',a-b)
#        print('The average:',(a+b)/2)
#
#        a=100
#        b=200
#        print('The sum:',a+b)
#        print('The product:',a*b)
#        print('The difference:',a-b)
#        print('The average:',(a+b)/2)

#class Test:
#    def m1(self):
#        def calc(a,b):
#            print('The sum:',a+b)
#            print('The product:',a*b)
#            print('The difference:',a-b)
#            print('The average:',(a+b)/2)
#            print()
#        calc(10,20)
#        calc(100,200)
#        calc(1000,2000)
#t=Test()
#t.m1()

#The sum: 30
#The product: 200
#The difference: -10
#The average: 15.0

#The sum: 300
#The product: 20000
#The difference: -100
#The average: 150.0

#The sum: 3000
#The product: 2000000
#The difference: -1000
#The average: 1500.0

#-----------------------------------------------------------------------------------------------------------------------------------
# Garbage collector and Destructor:

#import gc
#print(gc.isenabled())   #True
#gc.disable()
#print(gc.isenabled())   #False
#gc.enable()
#print(gc.isenabled())   #True

# Destructors:

#import time
#class Test:
#    def __init__(self):
#        print('Object Initialization activities')
#    def __del__(self):
#        print('Fulfilling last wish and performing cleanup activities...')
#
#t=Test()
#t=None
#time.sleep(10)
#print('End of application')


#class Test:
#    def __init__(Self):
#        print('Object initialisation activity')
#    def __del__(Self):
#        print('Fulfilling last wish and performing cleanup activity...')
#t1=Test()
#t2=Test()
#print('End of program.')

#class Test:
#    def __init__(self):
#        print("object initialisation activity")
#    def __del__(self):
#        print('Fulfilling last wishes and performing cleanup activity')
#
#t1=Test()
#t2=Test()
#t1=None
#t2=None
#print('end of application')

#import time
#class Test:
#    def __init__(self):
#        print('Constructor execution...')
#    def __del__(self):
#        print('Destructor execution')
#t1=Test()
#t2=t1
#t3=t1
#del t1
#time.sleep(10)
#print('Object not destroyed after deleting t1')
#del t2
#time.sleep(10)
#print('Object not destroyed even after deleting t2')
#time.sleep(10)
#print('Removing last refrence')
#del t3
#print('End of application')

#import time
#class Test:
#    def __init__(self):
#        print('Constructor execution')
#    def __del__(self):
#        print('Destructor execution')
#
#l=[Test(),Test(),Test()]
#print('Making list object eligible for garbage collection...')
#time.sleep(4)
#del l
#time.sleep(4)
#print('end of program')

#-----------------------------------------------------------------------------------------------------------------------------------
# What is the difference between del t and t=None?

# 1. del t
#class Test:
#    def __init__(self):
#        print('Constructor')
#    def __del__(self):
#        print('Destructor')

#t=Test()
#del t
#print('End of program')

# 2. t=None
#class Test:
#    def __init__(self):
#        print('Constructor')
#    def __del__(self):
#        print('Destructor')

#t=Test()
#t=None
#print('E#nd of program')
#print(t)

# How to find the number of references of  an object?
# sys getrefcount()

#import sys
#class Test:
#    pass

#t1=Test()
#t2=t1
#t3=t2
#t4=t3
#del t3,t4
#print(sys.getrefcount(t1))    

#-----------------------------------------------------------------------------------------------------------------------------------
# Using Members of One class another class

# By composition (HAS-A relationship)
# By inheritance (IS-A relationship)

# HAS-A :

#class Engine:
#    def __init__(self):
#        self.power='125KW'
#    def useEngine(self):
#        print('Engine Specific Functionality')

#class Car:
#    def __init__(self):
#        self.engine=Engine()
#    def useCar(self):
#        print('Car Requires Engine Functionality')
#        self.engine.useEngine()
#        print(self.engine.power)
#c=Car()    
#c.useCar()

#Car Requires Engine Functionality
#Engine Specific Functionality
#125KW

#class Car:
#    def __init__(self,name,model,color):
#        self.name=name
#        self.model=model
#        self.color=color
#    def getInfo(self):
#        print('Car Name:{},Model:{},Color:{}'.format(self.name,self.model,self.color))

#class Employee:
#    def __init__(self,ename,eno,car):
#        self.ename=ename
#        self.eno=eno
#        self.car=car
#    def empInfo(self):
#        print('Employee Name:',self.ename)
#        print('Employee Number:',self.eno)
#        print('Employee Car Info:')
#        self.car.getInfo()

#car=Car('Innova','2.5V','Grey')
#e=Employee('Durga',872425,car)
#e.empInfo()

# Employee Name: Durga
# Employee Number: 872425
# Employee Car Info:
# Car Name:Innova,Model:2.5V,Color:Grey


#class Sportsnews:
#    def sportsInfo(self):
#        print('Sports Information-1')
#        print('Sports Information-2')
#        print('Sports Information-3')
#        print('Sports Information-4\n')

#class MovieNews:
#    def moviesInfo(self):
#        print('Movies Information-1')
#        print('Movies Information-2')
#        print('Movies Information-3')
#        print('Movies Information-4\n')

#class PoliticsNews:
#    def politicsInfo(self):
#        print('Politics Information-1')
#        print('Politics Information-2')
#        print('Politics Information-3')
#        print('Politics Information-4\n')

#class DurgaNews:
#    def __init__(self):
#        self.sports=Sportsnews()
#        self.movies=MovieNews()
#        self.politics=PoliticsNews()
   
#    def getTotalNews(self):
#        print('Welcome to Durga News')
#        print('---------------------')
#        self.sports.sportsInfo()
#        self.movies.moviesInfo()
#        self.politics.politicsInfo()

#d=DurgaNews()
#d.getTotalNews()

#class DurgaNews:
#    def __init__(self,sportsNews,movieNews,politicsNews):
#        self.sports=sportsNews
#        self.movies=movieNews
#        self.politics=politicsNews

#    def getTotalNews(self):
#        print('Welcome to Durga News')
#        print('---------------------')
#        self.sports.sportsInfo()
#        self.movies.moviesInfo()
#        self.politics.politicsInfo()

#sports=Sportsnews()
#movie=MovieNews()
#politics=PoliticsNews()
#dNews=DurgaNews(sports,movie,politics)
#dNews.getTotalNews()

#-----------------------------------------------------------------------------------------------------------------------------------
# IS-A realionship (Inheritance)

#class P:
#    def m1(self):
#        print('Parent class Method')

#class C(P):
#    def m2(slef):
#        print('Child class Method')

#c=C()
#c.m1()
#c.m2()


#class P:
#    a=10
#    def __init__(self):
#        print('Parent constructor')
#        self.b=20
#    def m1(self):
#        print('Parent Instance Method')
#    @classmethod
#    def m2(cls):
#        print('Parent class Method')
#    @staticmethod
#    def m3():
#        print('Parent static Method')

#class C(P):
#    pass

#c=C()
#print(c.a)   #10 
#print(c.b)   #20 
#c.m1()       #Parent Instance Method 
#c.m2()       #Parent class Method
#c.m3()       #Parent static Method   


#class Person:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def eatndrink(self):
#        print('Eat Biryani & Drinking Beer')

#class Emplyee(Person):
#    def __init__(self,name,age,eno,esal):
#        self.name=name
#        self.age=age
#        self.eno=eno
#        self.esal=esal
#    def work(self):
#        print('Coding Python Programs')
#    def empInfo(self):
#        print('Employee Name:',self.name)
#        print('Employee Age:',self.age)
#        print('Employee Number:',self.eno)
#        print('Employee Salary:',self.esal)
    
#e=Emplyee('Durga',48,872425,10000)
#e.eatndrink()
#e.work()
#e.empInfo()

# Using super() to use constructor of parent class 
#class Person:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def eatndrink(self):
#        print('Eat Biryani & Drinking Beer')

#class Emplyee(Person):
#    def __init__(self,name,age,eno,esal):
#        super().__init__(name,age)
#        self.eno=eno
#        self.esal=esal
#    def work(self):
#        print('Coding Python Programs')
#    def empInfo(self):
#        print('Employee Name:',self.name)
#        print('Employee Age:',self.age)
#        print('Employee Number:',self.eno)
#        print('Employee Salary:',self.esal)
    
#e=Emplyee('Durga',48,872425,10000)
#e.eatndrink()
#e.work()
#e.empInfo()

# IS-A VS HAS-A

#class Car:
#    def __init__(self,name,model,color):
#        self.name=name
#        self.model=model
#        self.color=color
#    def getinfo(self):
#        print('\t Car Name:{}\n\tmodel:{}\n\tcolor:{}'.format(self.name,self.model,self.color))

#class Person:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def eatndrink(self):
#        print('Eating Biryani And Drinking Beer')

#class Employee(Person):
#    def __init__(self, name, age,eno,esal,car):
#        super().__init__(name, age)
#        self.eno=eno
#        self.esal=esal
#        self.car=car
#    def work(self):
#        print('Coding Python Programs...')
#    def empInfo(self):
#        print('Employee Name:',self.name)
#        print('Employee Age:',self.age)
#        print('Employee Number:',self.eno)
#        print('Employee Salary:',self.esal)
#        print('Employee Car Information')
#        print('------------------------')
#        self.car.getinfo()                  
#car=Car('Polo','GT','White')
#e=Employee('Piyush',23,4267715,35000,car)
#e.eatndrink()
#e.work()
#e.empInfo()

#-----------------------------------------------------------------------------------------------------------------------------------
# Composition VS Aggeragation

# Composition:

#class University:
#    def __init__(self):
#        self.dept=self.Department()
#    class Department:
#        pass
#u=University()

# Aggeragation:

#class Professor:
#    pass
#class Deaprtment:
#    def __init__(self,prof):
#        self.prof=prof
#prof=Professor()
#csdept=Deaprtment(prof)
#itdept=Deaprtment(prof)

#-----------------------------------------------------------------------------------------------------------------------------------
# Types Of Inheritance:

# Single Inheritance:

#class P:
#    def m1(self):
#        print('Parent Method')
#class C(P):
#    def m2(self):
#        print('Child Method')    
#c=C()
#c.m1()
#c.m2()

# Multi-Level Inheritance:

#class P:
#    def m1(self):
#        print('Parent Method')
#class C(P):
#    def m2(self):
#        print('Child Method')
#class CC(C):
#    def m3(self):
#        print('Sub Child Method')
#cc=CC()
#cc.m1()
#cc.m2()
#cc.m3()

# Hierarchical Inheritance:

#class P:
#    def m1(self):
#        print('Parent Method')
#class C1(P):
#    def m2(self):
#        print('Child 1 Method')
#class C2(P):
#    def m3(self):
#        print('Child 2 Method')

#c1=C1()
#c1.m1()
#c1.m2()

#c2=C2()
#c2.m1()
#c2.m3()

# Multiple Inheritance:

#class P1:
#    def m1(self):
#        print('Parent 1 Method')
#class P2:
#    def m2(self):
#        print('Parent 2 Method')
#class C(P1,P2):
#    def m3(self):
#        print('Child Method')
#c=C()
#c.m1()
#c.m2()
#c.m3()

#class P1:
#    def m1(self):
#        print('Parent 1 Method')
#class P2:
#    def m1(self):
#        print('Parent 2 Method')
#class C(P1,P2):
#    def m2(self):
#        print('Child Method')
#c=C()
#c.m1()

#-----------------------------------------------------------------------------------------------------------------------------------
# Method Resolution Order(MRO) Alogrithm:

#class A:
#    def m1(self):
#        print('class A method')
#class B(A):
#      pass
#class C(A):
#    pass
#class D(B,C):
#    pass
#d=D()  #DBCAO
#d.m1()

#class A:
#    pass
#class B:
#    pass
#class C:
#    def m1(self):
#        print('C class method')
#class D(A,B):
#    pass
#class E(B,C):
#    pass
#class F(D,E,C):
#    pass

#print(A.mro()) #[<class '__main__.A'>, <class 'object'>]
#print(B.mro()) #[<class '__main__.B'>, <class 'object'>]
#print(C.mro()) #[<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
#print(D.mro()) #[<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
#print(E.mro()) #[<class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
#print(F.mro()) #[<class '__main__.F'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

#f=F()
#f.m1() # FDAEBC

#class A: pass
#class B: pass
#class C: pass
#class D(A,B): pass
#class E(A,C): pass
#class F(D,E): pass

#print(F.mro())  #FDEABCO

#-----------------------------------------------------------------------------------------------------------------------------------
# super():

#class P:
#    def m1(self):
#        print('Parent Method')
#class C(P):
#    def m1(self):
#        self.m1()
#        print('Child Method')
#c=C()
#c.m1() #RecursionError: maximum recursion depth exceeded


#class P:
#    def m1(self):
#        print('Parent method')
#class C(P):
#    def m1(self):
#        super().m1()
#        print('Child method')
#c=C()
#c.m1()


#class P:
#    a=10
#    def __init__(self):
#        print('Parent constructor')
#    def m1(self):
#        print('Parent Instance method')
#    @classmethod
#    def m2(self):
#        print('Parent class method')
#    @staticmethod
#    def m3():
#        print('Parent Static method')
#class C(P):
#    def __init__(self):
#        print('Child constructor')
#    def method1(self):
#        print(super().a)
#        super().m1()
#        super().m2()
#        super().m3()
#        super().__init__()
#c=C()
#c.method1()

#Child constructor
#10
#Parent Instance method
#Parent class method
#Parent Static method
#Parent constructor

#class P:
#    a=10
#    def __init__(self):
#        print('Parent constructor')
#    def m1(self):
#        print('Parent Instance method')
#    @classmethod
#    def m2(self):
#        print('Parent class method')
#    @staticmethod
#    def m3():
#        print('Parent Static method')
#class C(P):
#    def __init__(self):
#        print('Child constructor')
#    def method1(self):
#        print(self.a)
#        self.m1()
#        self.m2()
#        self.m3()
#        super().__init__()
#c=C()
#c.method1()

#Child constructor
#10
#Parent Instance method
#Parent class method
#Parent Static method
#Parent constructor

#class Person:
#    def __init__(self,name,age,height,weight):
#        self.name=name
#        self.age=age
#        self.height=height
#        self.weight=weight
#    def display(self):
#        print('Name:',self.name)
#        print('Age:',self.age)
#        print('Height:',self.height)
#        print('Weight:',self.weight)
#class Student(Person):
#    def __init__(self,name,age,height,weight,rollno,marks):
#        self.name=name
#        self.age=age
#        self.height=height
#        self.weight=weight
#        self.rollno=rollno
#        self.marks=marks
#    def display(self):
#        print('Name:',self.name)
#        print('Age:',self.age)
#        print('Height:',self.height)
#        print('Weight:',self.weight)
#        print('Rollno:',self.rollno)
#        print('Marks:',self.marks)
#s=Student('Ravi',24,5.6,90,24144,98)
#s.display()



#class Person:
#    def __init__(self,name,age,height,weight):
#        self.name=name
#        self.age=age
#        self.height=height
#        self.weight=weight
#    def display(self):
#        print('Name:',self.name)
#        print('Age:',self.age)
#        print('Height:',self.height)
#        print('Weight:',self.weight)
#class Student(Person):
#    def __init__(self,name,age,height,weight,rollno,marks):
#        super().__init__(name,age,height,weight)
#        self.rollno=rollno
#        self.marks=marks
#    def display(self):
#        super().display()
#        print('Rollno:',self.rollno)
#        print('Marks:',self.marks)
#s=Student('Ravi',24,5.6,90,24144,98)
#s.display()

#-----------------------------------------------------------------------------------------------------------------------------------
# Polymorphism:

# Operator overloading:

# +:
#print(10+20)          
#print('durga'+'soft') 

# *:
#print(10 * 20)
#print('durga'*3)

# + for objects:

#class Book:
#    def __init__(self,pages):
#        self.pages=pages
#    def __add__(self,other):
#        total_pages=self.pages+other.pages
#        return total_pages
#b1=Book(100)
#b2=Book(200)
#print(b1+b2)

#class Book:
#    def __init__(self,pages):
#        self.pages=pages
#    def __add__(self,other):
#        total_pages=self.pages+other.pages
#        return total_pages
#b1=Book(100)
#b2=Book(200)
#b3=Book(300)
#print(b1+b2+b3)

#class Student:
#    def __init__(self,name,marks):
#        self.name=name
#        self.marks=marks
#    def __gt__(self,other):
#        return self.marks>other.marks
#    def __le__(self,other):
#        return self.marks<=other.marks
#s1=Student('durga',100)
#s2=Student('Ravi',200)
#s3=Student('Shiva',50)
#print(s1<s2)
#print(s1<=s2)
#print(s3<=s1)
#print(s1>=s2)
#print(s1>=s3)

# * operator overloading:

#class Employee:
#    def __init__(self,name,salaryPerDay):
#        self.name=name
#        self.salaryPerDay=salaryPerDay
#    def __mul__(self,other):
#        return (self.salaryPerDay*other.workingDays)
#class TimeSheet:
#    def __init__(self,name,workingDays):
#        self.name=name
#        self.workingDays=workingDays
#    def __mul__(self,other):
#        return (self.workingDays*other.salaryPerDay)
#e=Employee('Durga',1000)
#t=TimeSheet('Durga',25)
#print('This month salary:',e*t)
#print('This month salary:',t*e)

# __str__():

#class Student:
#    def __init__(self,name,rollno,marks):
#        self.name=name
#        self.rollno=rollno
#        self.marks=marks
#    def __str__(self):
#        # return self.name
#        return 'Name:{},Rollno:{},Marks:{}'.format(self.name,self.rollno,self.marks)
#s1=Student('Durga',101,95)
#s2=Student('Ravi',102,98)
#print(s1)
#print(s2)   
 
# + operator overloading for nesting:

#class Book:
#    def __init__(self,pages):
#        self.pages=pages
#    def __add__(self,other):
#        print('Add Method Executed')
#        return Book(self.pages+other.pages)
#    def __mul__(self,other):
#        print('Mul Method Executed')
#        return Book(self.pages*other.pages)
#    def __str__(self):
#        return 'The total Number of pages:{}'.format(self.pages) 
# 
#b1=Book(100)
#b2=Book(200)
#b3=Book(300)
#b4=Book(500)
#print(b1*b2+b3*b4)

#-----------------------------------------------------------------------------------------------------------------------------------
# Method overloading not is supported in Python. If multiple methods are declared with same name then the last method is considered 
# by PVM. 

#class test:
#    def m1(self):
#        print('no-arg method')
#    def m1(self,x):
#        print('one-arg method')
#    def m1(self,x,y):
#        print('two-arg method')
#t=test()
#t.m1(1,2)

#class Test:
#    def m1(self,x):
#        print('{}-argument method'.format(x.__class__.__name__))
#t=Test()
#t.m1('Durga')  #str-argument method 
#t.m1(10)       #int-argument method     
#t.m1(10.5)     #float-argument method 
#t.m1(True)     #bool-argument method  

#class Test:
#    def m1(self,a=None,b=None,c=None):
#        if a is not None and b is not None and c is not None:
#            print('Three-argumnet method')
#        elif a is not None and b is not None:
#            print('two-argument method')
#        elif a is not None:
#            print('one-argument method')
#        else:
#            print('no-argument method')        
#t=Test()
#t.m1()         #no-argument method 
#t.m1(10)       #one-argument method   
#t.m1(10,20)    #two-argument method   
#t.m1(10,20,30) #Three-argumnet method 

#class Test:
#    def m1(self,*args):
#        print('variable length argument method')
#t=Test()
#t.m1(10,20,30,40,5,0+6,0,)

#class Test:
#    def add(self,*args):
#        total=0
#        for x in args:
#            total += x
#        print('The sum:',total)
#t=Test()
#t.add(10,20,30,40,50,60,4,0)

#-----------------------------------------------------------------------------------------------------------------------------------
# Constructor overloading:

#class Test:
#    def __init__(self):
#        print('No arg constructor')
#    def __init__(self,x):
#        print('One arg constructor')
#    def __init__(self,x,y):
#        print('Two arg constructor')
#
#t=Test(1,2)    #Two arg constructor


#class Test:
#    def __init__(self,a=None,b=None,c=None):
#        print('Constructor with 0|1|2|3 arguments')
#t=Test(1,2)

#class Test:
#    def __init__(self,*args):
#        total=0
#        for x in args:
#            total+=x
#        print(total)
#
#t=Test(10,20,30,40,50)

#-----------------------------------------------------------------------------------------------------------------------------------
# Overriding

# Method overriding:

#class Parent:
#    def property(self):
#        print('Land + Gold + Cash + Power')
#    
#    def marry(self):        # overridden method
#        print('Appalamma')
#
#class Child(Parent):
#    def marry(self):            # overriding method
#        print('Katrina Kaif')
#
#c=Child()
#c.property()    #Land + Gold + Cash + Power
#c.marry()       #Katrina Kaif

#class Parent:
#    def property(self):
#        print('Land + Gold + Cash + Power')
#    
#    def marry(self):        # overridden method
#        print('Appalamma')
#
#class Child(Parent):
#    def marry(self):            # overriding method
#        print('Katrina Kaif')            
#        super().marry()         #Appalamma
#
#c=Child()
#c.property()    #Land + Gold + Cash + Power
#c.marry()       #Katrina Kaif  

# Constructor overriding:

#class Parent:
#    def __init__(self):
#        print('Parent constructor')  # overriden constructor
#
#class Child(Parent): 
#    def __init__(self):
#        print('Child contructor')    # overriding constructor
#        super().__init__()
#c= Child()


#class Person:
#    def __init__(self,name,age,height,weight):
#        self.name=name
#        self.age=age
#        self.height=height
#        self.weight=weight
#    
#    def display(self):
#        print('Name:',self.name)
#        print('Age:',self.age)
#        print('Height:',self.height)
#        print('Weight:',self.weight)


#class Employee(Person):
#    def __init__(self, name, age, height, weight,eno,esal):
#        self.name=name
#        self.age=age
#        self.height=height
#        self.weight=weight
#        self.eno=eno
#        self.esal=esal
#    def display(self):
#        print('Name:',self.name)
#        print('Age:',self.age)
#        print('Height:',self.height)
#        print('Weight:',self.weight)
#        print('Employee Number:',self.eno)
#        print('Employee Salary:',self.esal)
#        
#e=Employee('Piyush',23,177,86,865,50000)
#e.display()        


#class Person:
#    def __init__(self,name,age,height,weight):
#        self.name=name
#        self.age=age
#        self.height=height
#        self.weight=weight
#    
#    def display(self):
#        print('Name:',self.name)
#        print('Age:',self.age)
#        print('Height:',self.height)
#        print('Weight:',self.weight)
#
#class Employee(Person):
#    def __init__(self,name,age,height,weight,eno,esal):
#        super().__init__(name,age,height,weight)
#        self.eno=eno
#        self.esal=esal
#        
#    def display(self):
#        super().display()
#        print('Employee Number:',self.eno)
#        print('Employee Salary:',self.esal)
#        
#e=Employee('Piyush',23,177,86,865,50000)
#e.display() 

#-----------------------------------------------------------------------------------------------------------------------------------
# Abstraction

# Abstractor method:

#from abc import abstractmethod
#
#class Vehicle:
#    
#    @abstractmethod
#    def getNoofWheels(self):
#        pass

# Absract class

#from abc import ABC, abstractmethod
#
#class Vehicle(ABC):
#    @abstractmethod
#    def getNoofWheels(self):
#        pass
#
#class Bus(Vehicle):
#    def getNoofWheels(self):
#        return 6
#
#class Auto(Vehicle):
#    def getNoofWheels(self):
#        return 3
#b=Bus()
#print(b.getNoofWheels())
#a=Auto()
#print(a.getNoofWheels())

#from abc import * 
#class Test:
#    @abstractmethod
#    def m1(self):
#        pass
#t=Test()

#from abc import *

#class Test(ABC):
#    @abstractmethod
#    def m1(self):
#        pass
#class Subtest(Test):
#    pass
#
#s=Subtest()  #TypeError: Can't instantiate abstract class Subtest with abstract method m1

#class Test(ABC):
#    @abstractmethod
#    def m1(self):
#        pass
#    @abstractmethod
#    def m2(self):
#        pass
#
#class Subtest(Test):
#    def m1(self):
#        print('m1 method implementation')
#
#s=Subtest()
#s.m1()      #TypeError: Can't instantiate abstract class Subtest with abstract method m2

#class Test(ABC):
#    @abstractmethod
#    def m1(self):
#        pass
#    @abstractmethod
#    def m2(self):
#        pass
#class Subtest(Test):
#    def m1(self):
#        print('m1 method implementation')
#    def m2(self):
#        print('m2 method implementation')
#
#s=Subtest()
#s.m1()      #m1 method implementation    
#s.m2()      #m2 method implementation     


#class Test(ABC):
#    def m1(self):
#        print('Non-abstract method')
#    @abstractmethod
#    def m2(self):
#        pass
#class Subset(Test):
#    def m2(self):
#        print('m2 method')
#
#s= Subset()
#s.m1()      #Non-abstract method
#s.m2()      #m2 method

#-----------------------------------------------------------------------------------------------------------------------------------
# Interfaces In Python

#from abc import ABC, abstractmethod


#class Test(ABC):
#    def m1(self):
#        print('Hi')
#    @abstractmethod
#    def m2(self):
#        pass
  
# Interface
#class Test(ABC):
#    @abstractmethod
#    def m1(self):
#        pass
#    @abstractmethod
#    def m2(self):
#        pass

#from abc import  *

#class CollegeAutomation(ABC):
#    @abstractmethod
#    def m1(self):
#        pass
#    @abstractmethod
#    def m2(self):
#        pass
#    @abstractmethod
#    def m3(self):
#        pass
#
#class DurgaSoftImpl(CollegeAutomation):
#    def m1(self):
#        print('m1 method implementation')        
#    def m2(self):
#        print('m2 method implementation')        
#    def m3(self):
#        print('m3 method implementation')        
#    
#d=DurgaSoftImpl()
#d.m1()    
#d.m2()
#d.m3()

#-----------------------------------------------------------------------------------------------------------------------------------
# Public members, Private members, Protected members:

# Public members:

#class Test:
#    def __init__(self):
#        self.x = 10
#    
#    def m1(self):
#        print('This is public method')
#    
#    def m2(self):
#        print(self.x)
#        self.m1()
#t=Test()
#t.m2()
#print(t.x)
#t.m1()

# Private members:

#x=10       # Public variable
#__x=10     # Private variable

#class Test:
#    def __init__(self):
#        self.__x=10                 # Private variable
#    
#    def __m1(self):                 # Private method
#        print("Private Method")
#    
#    def m2(self):
#        print(self.__x)
#        self.__m1()
#
#t=Test()           #10                    
#t.m2()             #Private Method                     
#print(t._Test__x)  #10       
#t._Test__m1()      #Private Method 

# Protected members:

#class Test:
#    def __init__(self):
#        self._x = 10
#    
#    def m1(self):
#        print(self._x)
#
#class SubTest(Test):
#    def m2(self):
#        print(self._x)
#
#t=SubTest()    
#t.m1()       #10   
#t.m2()       #10      
#print(t._x)  #10

#-----------------------------------------------------------------------------------------------------------------------------------
# Data Hiding:

#class Account:
#    def __init__(self,initial_balance):
#        self.__balance = initial_balance
#
#a= Account(10000)
#print(a.__balance)  # Attribute Error

#class Account:
#    def __init__(self,initial_balance):
#        self.__balance = initial_balance
#    
#    def getBalance(self):
#        # validation / authentication
#        return self.__balance
#
#a=Account(10000)
#print(a.getBalance())       #10000

#-----------------------------------------------------------------------------------------------------------------------------------
# Abstraction:

# Hiding implementation only highlighting service.

#-----------------------------------------------------------------------------------------------------------------------------------
# Encapsulation (Binding data and corresponding behaviour in a single unit):

# Encapsulation = Data hiding + Abstraction

#class Account:
#    def __init__(self,initial_balance):
#        self.__balance = initial_balance
#
#    def getBalance(self):
#        # validation / Authentication
#        return self.__balance
#    
#    def deposit(self,amount):
#        # validation/ Authentication
#        self.__balance += amount
#
#    def withdraw(self,amount):
#         # validation/ Authentication
#        self.__balance -= amount

