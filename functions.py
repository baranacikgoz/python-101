###### Function reading & writing

def myFunction(myString):
    return myString

print(myFunction("This is my function"))


##### arbitrary(keyfi) arguments *args
# if the number of arguments is unknown

def kidsNames(*kids):
    return kids

print(kidsNames("baran","ali","ahmet"))


##### arbitrary keyword arguments **kwargs
# if the number of keyword arguments is unknown

def personPrinter(**person):
    print(person["lastName"])

personPrinter(name="baran", lastName="acikgoz") #output: acikgoz


##### default parameter value

def eBook(sizeMb,downloadUrl = "book.com"):
    print("Books adress: {}, and size is {}mb".format(downloadUrl,sizeMb))

eBook(13) #output: Books adress: book.com, and size is 13mb



##### Recursion

def recursiveFactoriel(x):
    if(x>0):
        return x*recursiveFactoriel(x-1)
    else:
        return 1

print(recursiveFactoriel(5))


######  LAMBDA

newSum = lambda a,b: a+b
newSum(3,4)

sirasiz_liste = [("b", 3), ("a", 8), ("d", 12), ("c", 1)]

#sorted fonksiyonu ile sıralama yapacagiz, lamda da su ise yarıyor 1.indexteki elemanları secme
sorted(sirasiz_liste, key = lambda x: x[1]) #return: [('c', 1), ('b', 3), ('a', 8), ('d', 12)]
sirasiz_liste #output: [('c', 1), ('b', 3), ('a', 8), ('d', 12)]


########### VECTOR OPERATIONS

#************* OOP(this is long version we don't use in data science)
a = [1,2,3,4]
b = [11,22,33,44]
ab = []

for i in range(0, len(a)):
    ab.append(a[i]*b[i])

ab #output: [11, 44, 99, 176]
#************** OOP(this is long version we don't use in data science)


## FP(Functional programming) this is what we use for the same thing

import numpy as np
a = np.array([1,2,3,4])
b = np.array([11,22,33,44])

a*b #output: array([ 11,  44,  99, 176])















