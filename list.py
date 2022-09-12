# Mathematical operators for tuple
# +,*

#+: Both arguments should be tuple.

#t1=(10,20,30)
#t2=(40,50,60)
#t3=t1+t2
#print(t3)      (10, 20, 30, 40, 50, 60)

#*: one argument should be tuple another should be int type

#t1=(10,20,30)
#t2=t1*3
#print(t2)      (10, 20, 30, 10, 20, 30, 10, 20, 30)

#t1=(10,20)
#t2=(30,40)
#t3=t1+t2
#t4=t3*3
#print(t4)      (10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40)

#--------------------------------------------------------------------------------------
# Equaltiy operators for tuple
# ==,!=

#t1=('Cat','Rat','Dog')
#t2=('Cat','Rat','Dog')
#t3=('CAT','RAT','DOG')
#t4=('Rat','Dog','Cat')
#print(t1==t2)           True
#print(t1==t3)           False
#print(t1==t4)           False

#--------------------------------------------------------------------------------------
# Relational operators for tuple
#<,<=,>,>=

#t1=(10,20,30)
#t2=(30,15,40)
#print(t1<t2)            True

#--------------------------------------------------------------------------------------
# Membership operator

#t=(10,20,30)
#print(10 in t) 
#print(50 not in t)
#print(60 in t)

#-------------------------------------------------------------------------------------
# Important metheods and functions for list.
# len(),count(),index()

#t=(10,20,20,30,40)
#print(len(t))          5
#print(t.count(20))     2
#print(t.index(20))     1

#-------------------------------------------------------------------------------------
# Reversing and sorting elements of tuple.

#t=(10,20,30,40)
#r=reversed(t)
#t1=tuple(r)
#print('Original tuple:',t)       #Original tuple: (10, 20, 30, 40) 
#print('Reversed tuple:',t1)      #Reversed tuple: (40, 30, 20, 10)

#t=(20,15,0,10)
#t.sort()           #AttributeError: 'tuple' object has no attribute 'sort'

#t=(20,10,15,0)
#l=sorted(t)
#t1=tuple(l)
#print('Original tuple:',t)        #Original tuple: (20, 10, 15, 0)
#print('Sorted tuple:',t1)         #Sorted tuple: (0, 10, 15, 20)   

#t=(20,15,0,10)
#l=sorted(t,reverse=True)
#t1=tuple(l) 
#print('Reverse sorted tuple:',t1)   #Reverse sorted tuple: (20, 15, 10, 0)           

#-------------------------------------------------------------------------------------
# max() & min() functions for tuple:

#t=(20,10,0,5,15)
#print(max(t))       #20
#print(min(t))       #0

#-------------------------------------------------------------------------------------
# Tuple packing and unpacking:

# Packing

#a=10
#b=20
#c=30
#d=40
#t=a,b,c,d
#print(t)           #(10, 20, 30, 40)
#l=[a,b,c,d]
#print(l)           #[10,20,30,40]

# Unpacking

#t=(10,20,30,40)
#a,b,c,d = t
#print(a,b,c,d)     #10 20 30 40

#t=(10,20,30,40) 
#a,b,c=t            #ValueError: too many values to unpack (expected 3)
#a,b,c,d,e=t        #ValueError: not enough values to unpack (expected 5, got 4)


#t=(10,20,30,40)
#a,*b=t              # Variable length argument
#print(a)            #10
#print(b)            #[20,30,40]

#-------------------------------------------------------------------------------------
# Tuple comprehension:

#l=[x*x for x in range(1,6)]
#print(type(l))                #<class 'list'>
#print(l)                      #[1, 4, 9, 16, 25]

#t=(x*x for x in range(1,6))
#print(type(t))                #<class 'generator'>
#print(t)                      #<generator object <genexpr> at 0x0000026999B325E8>

#l=[x*x for x in range(1,6)]
#t=tuple(l)
#print(t)                      #(1, 4, 9, 16, 25)

#-------------------------------------------------------------------------------------
# Differences betweeen list and tuple

# List
# l=[10,20,30,40]
# More memory
# Performance is low 
# List is unhashable

# Tuple
# t=(10,20,30,40)
# Less memory
# Performance is high
# Tuple is hashable



#import collections
#l=[10,20,30]
#t=(10,20,30)
#print(isinstance(l,collections.Hashable))     #Fasle
#print(isinstance(t,collections.Hashable))     #True
#print(hash(t))                                #-6299925204498084005
#print(hash(l))                                #TypeError: unhashable type: 'list'
 
#s={10,20}
#l=[10,20,30]
#t=(10,20,30)
#s.add(t)
#print(s)                #{10, (10, 20, 30), 20}
#s.add(l)                #TypeError: unhashable type: 'list'

d={}
l=[10,20,30]
t=(10,20,30)
d[t]='A' 
print(d)                 #{(10, 20, 30): 'A'}
d[l]='B'                 #TypeError: unhashable type: 'list'
