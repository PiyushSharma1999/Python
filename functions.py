#def calculate(a,b):
#    print('The sum:',a+b)
#    print('The differnece:',a-b)
#    print('The product:',a*b)
#calculate(20,10)
#calculate(200,100)
#calculate(2000,1000)

#The sum: 30
#The differnece: 10
#The product: 200
#The sum: 300
#The differnece: 100
#The product: 20000
#The sum: 3000
#The differnece: 1000
#The product: 2000000

#------------------------------------------------------------------------------------------------------------------------------------
# Types of functions:

# 1. Built-in function: print(),eval(),etc...

# 2. User defined functions:

# Syntax:

# def function_name(parameters):
#        ''' doc String'''
#        body
#        return value
 
#------------------------------------------------------------------------------------------------------------------------------------
# Write a function to print wish message:

#def wish():
#    print('Hello friends, Good evening')
#wish()
#wish()
#wish()
  
#Hello friends, Good evening
#Hello friends, Good evening
#Hello friends, Good evening  

#------------------------------------------------------------------------------------------------------------------------------------
# Functon Parameters:

# Write a function to take name of the student as input and print wish message by name.

#def wish(name):
#    print('Hello',name,'Good evening!!!')
#wish('Durga')                              #Hello Durga Good evening!!!
#wish('Piyush')                             #Hello Piyush Good evening!!!
#wish()                         #TypeError: wish() missing 1 required positional argument: 'name'


# Write a function to take a number as input and print it's square value.

#def squareit(num):
#    sq=num*num
#    print('The square of {} is:{}'.format(num,sq))

#squareit(10)         #The square of 10 is:100
#squareit(4)          #The square of 4 is:16
#squareit(3)          #The square of 3 is:9

#------------------------------------------------------------------------------------------------------------------------------------
# Return Statement:

# Write afunction to accept 2 numbers as input and return sum.

#def add(a,b):
#    sum=a+b
#    return sum
#result=add(10,20)
#print('The sum:',result)        #The sum: 30
#print('The sum:',add(100,200))    #The sum: 300
 
#def f1():
#    print('Hello')
#z=f1()
#print('The return value:',z)    

#Hello
#The return value: None

#------------------------------------------------------------------------------------------------------------------------------------
# Write a function to find factorial of given positive int vale.

#def factorial(num):
#    result=1
#    while num>=1:
#        result=result*num
#        num-=1
#    return result
#for i in range(1,6):
#    print('The factorial of',i,'is',factorial(i))

#The factorial of 1 is 1
#The factorial of 2 is 2
#The factorial of 3 is 6
#The factorial of 4 is 24
#The factorial of 5 is 120

#------------------------------------------------------------------------------------------------------------------------------------
# Returning multiple values from a function:

#def sum_sub(a,b):
#    sum=a+b
#    sub=a-b
#    return sum,sub
#x,y=sum_sub(20,10)
#print('The sum:',x)         #The sum: 30
#print('The subtraction:',y) #The subtraction: 10

# Internally multiple values are returned as single Tuple

#def calc(a,b):
#    sum=a+b
#    sub=a-b
#    mul=a*b
#    div=a/b
#    return sum,sub,mul,div
#t=calc(20,10)
#print(type(t))              #<class 'tuple'>
#print(t)                    #(30, 10, 200, 2.0)
#print('The results are:') 
#for x in t:
#    print(x)

#The results are:
#30
#10
#200
#2.0

#------------------------------------------------------------------------------------------------------------------------------------
# Types of arguments:

# 1. Positional argument:

#def sub(a,b):
#    print(a-b)
#sub(200,100)      # 100
#sub(100,200)      #-100
#sub(100)      #TypeError: sub() missing 1 required positional argument: 'b'


# 2. Keyword arguments:

#def sub(a,b):
#    print(a-b)
#sub(a=200,b=100)  #100
#sub(b=100,a=200)  #100   
 
#def sub(a,b):
#    print(a-b)
#sub(a=200,b=100)  #100
#sub(b=100,a=200)  #100   
#sub(200,b=100)    #100 
#sub(a=200,100)    #SyntaxError

# 3. Default arguments:

#def wish(name):
#    print('Heloo',name,'Good evening') 
#wish()   # TypeError
#wish('Durga')  #Heloo Durga Good evening   

#def wish(name='Guest'):
#    print('Hello',name,'Good evening')
#wish()                                    #Hello Guest Good evening
#wish('Doctor')                            #Hello Doctor Good evening   


#def wish(name='Guest',msg='Good Morning'):
#    print('Hello',name,msg)
#wish()                       #Hello Guest Good Morning
#wish('Durga')                #Hello Durga Good Morning       
#wish('Durga','Good evening') #Hello Durga Good evening

#def wish(name,msg='Good morning'):
#    print('Hello',name,msg)
#wish('Durga')                  #Hello Durga Good Morning
#wish('Durga','Good Evening')   #Hello Durga Good Evening

#def wish(name='Guest',msg):
#    pass

# SyntaxError: non-default argument follows default argument

# 4. Variable lenght argument:

#def f1(*n):
#    print("Variable length argument  function")
    
#f1()
#f1(10)
#f1(10,20,30,40)

#Variable length argument  function
#Variable length argument  function
#Variable length argument  function

#def f1(*n):
#    print(type(n))   #<class 'tuple'>
#    print(n)         #()
#f1() 

#def sum(*n):   
#    total=0
#    for x in n:
#        total+=x
#    print('The sum is:',total)

#sum()          #The sum is: 0
#sum(10)        #The sum is: 10
#sum(10,20)     #The sum is: 30
#sum(10,20,30)  #The sum is: 60

#def f1(*n):
#    print(n)
#f1(10,20)                    #(10,20)
#f1((10,20,30),(40,50,60))    #((10, 20, 30), (40, 50, 60))      
     
#def f1(x,*y):
#    print(x)      #10             #10
#    print(y)      #(20, 30, 40)   #()
#f1(10,20,30,40)    
#f1(10)
#f1()              #TypeError: f1() missing 1 required positional argument: 'x'

#def f(*x,y):
#    print(x)
#    print(y)
#f(10,20,30,40)     #TypeError: f() missing 1 required keyword-only argument: 'y'
#f(10,20,30,y=40)   

#(10, 20, 30)
#40

#def f1(*x,*y):
#    print(x)
#    print(y)

# SynatxError: invalid synax
# We can't take more than one variable length argument

#------------------------------------------------------------------------------------------------------------------------------------
#  Difference between *args and **kwargs

#def f1(**kwargs):
#    print(kwargs)
#f1()
#f1(name='Durga',rollno=101) 
#f1(A=10,B=20,C=30,D=40)

#{}
#{'name': 'Durga', 'rollno': 101}
#{'A': 10, 'B': 20, 'C': 30, 'D': 40}

#def f1(*args,**kwargs):
#    print(args)          #(10, 20)
#    print(kwargs)        #{'A': 30, 'B': 40}
#f1(10,20,A=30,B=40)

#------------------------------------------------------------------------------------------------------------------------------------
#def f(arg1,arg2,arg3=4,arg4=8):
#    print(arg1,arg2,arg3,arg4)
#f(3,2)                           #3 2 4 8
#f(10,20,30,40)                   #10 20 30 40
#f(25,50,arg4=100)                #25 50 4 100
#f(arg4=2,arg1=3,arg2=4)          #3 4 4 2
#f()                             #TypeError: f() missing 2 required positional arguments: 'arg1' and 'arg2'
#f(arg3=10,arg4=20,30,40)        #SyntaxError: positional argument follows keyword argument
#f(4,5,arg2=6)                   #TypeError: f() got multiple values for argument 'arg2'
#f(4,5,arg3=5,arg5=6)            #TypeError: f() got an unexpected keyword argument 'arg5'

#------------------------------------------------------------------------------------------------------------------------------------
# Types of variable:
# 1. Global variables
# 2. Local variables

# 1. Global varibles: the variables which are decalred outside a function.

#a=10
#def f1():
#    print(a)
#def f2():
#    print(a)
#f1()            #10
#f2()            #10

# 2. Local variables: the variables which aare declared inside a function.

#def f1():
#    a=10
#    print(a)
#def f2():
#    print(a)
#f1()              #10
#f2()              #NameError: name 'a' is not defined      

#------------------------------------------------------------------------------------------------------------------------------------
# Need of global keyword:

#a=10
#def f1():
#    a=20
#    print(a)
#def f2():
#    print(a)
#f1()           #20   Local variable value
#f2()           #10   Global variable value

# global keyword

# 1. To bring global variable to the function for the required modification

#a=10
#def f1():
#    global a 
#    a=20     # we are changing the value of global variable
#    print(a)
#def f2():
#    print(a)
#f1()           #20
#f2()           #20
       

#def f1():
#    a=10
#    print(a)
#def f2():
#    print(a)
#f1()         #10
#f2()         #NameError: name 'a' is not defined

# 2. To decalre gloabal variable explixitly inside a function

#def f1():
#    global a 
#    a=10
#    print(a)
#def f2():
#    print(a)
#f1()          #10
#f2()          #10

#a=777
#def f1():
#    print(a)
#    global a
#    a=999
#    print(a)
#f1()           #SyntaxError: name 'a' is used prior to global declaration    

#a=777
#def f1():
#    global a
#    a=999
#    print(a)
#f1()           #999

#a=888
#def f1():
#    a=999
#    print(a)
#f1()             #999 local value

#a=888
#def f1():
#    a=999
#    print(globals()['a'])  #{'a':888,....}
#    print(globals().get('a'))
#f1() 
#888   
#888

#------------------------------------------------------------------------------------------------------------------------------------
# Recursive functions:

# Factorial:

# without recursion:

#def factorial(n):
#    result=1
#    while n>=1:
#        result*=n
#        n-=1
#    return result
#for i in range(1,6):
#    print('The factorial of',i,'is:',factorial(i))    

# with recursion:

#def factorial(n):
#    if n==0:
#        result=1
#    else:
#        result=n*factorial(n-1)
#    return result
#print('The factorial of 3 is:',factorial(3)) #The factorial of 3 is: 6           
#print('The factorial of 4 is:',factorial(4)) #The factorial of 4 is: 24
#for i in range(11):
#    print('The factorial of',i,'is:',factorial(i))

#The factorial of 0 is: 1
#The factorial of 1 is: 1
#The factorial of 2 is: 2
#The factorial of 3 is: 6
#The factorial of 4 is: 24
#The factorial of 5 is: 120
#The factorial of 6 is: 720
#The factorial of 7 is: 5040
#The factorial of 8 is: 40320
#The factorial of 9 is: 362880
#The factorial of 10 is: 3628800

#------------------------------------------------------------------------------------------------------------------------------------
# Internal Tracing of Recursive Function Execution:

#def factorial(n):
#    print('Execution of factorial function for n=',n)
#    if n==0:
#        result=1
#    else:
#        result=n*factorial(n-1)
#    print('Returning factorial ({}) is:{}'.format(n,result))
#    return result
#print(factorial(10)) 

#Execution of factorial function for n: 3
#Execution of factorial function for n: 2
#Execution of factorial function for n: 1
#Execution of factorial function for n: 0
#Returning factorial (0) is:1
#Returning factorial (1) is:1
#Returning factorial (2) is:2
#Returning factorial (3) is:6
#6
    
#--------------------------------------------------------------------------------------------------------------------------------------
#Maximum Recursion Depth In Python:

#count=0
#def factorial(n):
#    global count
#    count+=1
#    print('Execution of factorial functin n:',n)
#    if n==0:
#        result=1
#    else:
#        result=n*factorial(n-1)
#    return result
#print(factorial(994))
#print('The number of times factorial function execution:',count) 

#RecursionError: maximum recursion depth exceeded while calling a Python object

#--------------------------------------------------------------------------------------------------------------------------------------
# Anonymous functions/Lambda functions:

# Noraml function:

#def squareit(n):
#    return n*n

# Anonymous function:

#s=lambda n:n*n
#print('The square of 4 is:',s(4))  #The square of 4 is: 16
#for i in range(1,11):
#    print('The square of {} is:{}'.format(i,s(i)))

#The square of 1 is:1
#The square of 2 is:4
#The square of 3 is:9
#The square of 4 is:16
#The square of 5 is:25
#The square of 6 is:36
#The square of 7 is:49
#The square of 8 is:64
#The square of 9 is:81
#The square of 10 is:100

# Lambda function to find sum of given 2 numbers.

#s=lambda a,b:a+b
#print(s(10,20))      #30 
#print(s(100,200))    #300

# Lambda function to find biggest of two numbers.

# For 2 input values:

#bigger = lambda a,b: a if a>b else b
#print(bigger(10,20))    # 20
#print(bigger(-10,-20))  #-10

# For 3 input values:

#bigger =lambda a,b,c:a if a>b and a>c else b if b>a and b>c else c
#print(bigger(10,20,30))      # 30
#print(bigger(-10,-20,-30))   #-10 

#--------------------------------------------------------------------------------------------------------------------------------------
# Function as argument to another function:

# filter():

# filter(function,sequence)

# Wtihout filter():

#l=[0,1,2,3,4,5,6,7,8,9,10]
#def isEven(n):
#    if n%2==0:
#        return True
#    else:
#        return False
#l1=[]
#for n in l:
#    if isEven(n)==True:
#        l1.append(n)
#print(l1)                   #[0, 2, 4, 6, 8, 10]    

# With filter():

#l=[0,1,2,3,4,5,6,7,8,9,10]
#def isEven(n):
#    if n%2==0:
#        return True
#    else:
#        return False
#l1=filter(isEven,l)
#print(type(l1))         #<class 'filter'>      

#l2=list(filter(isEven,l))
#print(type(l2))            #<class 'list'>
#print(l2)                  #[0, 2, 4, 6, 8, 10]

# filter() with lambda:

#l=[0,1,2,3,4,5,6,7,8,9,10]
#even=list(filter(lambda n:n%2==0,l))
#print(l1)     #[0, 2, 4, 6, 8, 10]
#odd=list(filter(lambda n:n%2!=0,l))
#print(odd)    #[1, 3, 5, 7, 9]

# The numbers which are divisible by 3 and odd

#l=[0,1,2,3,4,5,6,7,8,9,10]
#nby3odd=list(filter(lambda n:n%3==0 and n%2!=0,l))
#print(nby3odd)    #[3, 9]

#heroins=['KatrinaKaif','KareenaKapoor','Anushka','Deepika','SunnyLeone','Malika']
#startswithK=list(filter(lambda name:name[0]=='K',heroins))
#print(startswithK)   #['KatrinaKaif', 'KareenaKapoor']

# name length divisible by 5
#lengthby5=list(filter(lambda name:len(name)%5==0,heroins))
#print(lengthby5)     #['SunnyLeone']

# name length odd

#odd=list(filter(lambda name:len(name)%2!=0,heroins))
#print(odd)  #['KatrinaKaif', 'KareenaKapoor', 'Anushka', 'Deepika']

#--------------------------------------------------------------------------------------------------------------------------------------
# map():
# map(function,sequence)

#l=[1,2,3,4,5]
#def squreIt(n):
#    return n*n
#l1=list(map(squreIt,l))
#print(l1)                     #[1, 4, 9, 16, 25]

#l=[1,2,3,4,5]
#l1=list(map(lambda n:n*n,l))
#print(l1)                     #[1, 4, 9, 16, 25]
 
#l=[1,2,3,4,5]
#l1=list(map(lambda n:n**2,l))
#print(l1)                     #[1, 4, 9, 16, 25]

#l1=[1,2,3,4,5]
#l2=[5,10,15,20,25]
#l3=list(map(lambda x,y:x*y,l1,l2))
#print(l3)                     #[5, 20, 45, 80, 125]

#l1=[1,2,3,4,5,6,7,8,9,10]
#l2=[5,10,15,20,25]
#l3=list(map(lambda x,y:x*y,l1,l2))
#print(l3)                     #[5, 20, 45, 80, 125]

#l1=[1,2,3,4,5,6,7,8,9,10]
#l2=[1,2,3,4,5,6,7,8,9,10]
#l3=[1,2,3,4,5,6,7,8,9,10]
#l4=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
#print(l4)     #[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

#--------------------------------------------------------------------------------------------------------------------------------------
# reduce() function:
# reduce is not python inbuilt function

#from functools import *
#l=[10,20,30,40,50]
#result=reduce(lambda x,y:x+y,l)
#print(result)                     #150
 
#from functools import *
#l=[10,20,30,40,50]
#result=reduce(lambda x,y:x-y,l)
#print(result)                     #-130

#from functools import *
#l=[10,20,30,40,50]
#result=reduce(lambda x,y:x*y,l)
#print(result)                    #12000000

# Find the sum of first 100 numbers by using reduce() function.
# n*(n+1)/2

#from functools import *
#result=reduce(lambda x,y:x+y,range(1,101))
#print(result)                   #5050

