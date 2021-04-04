## SETS - Kumeler
# non-indexed
# changable
# unique values
# ** NOT: küme mantığı ile işler, bir elemandan birden fazla varsa bir tanesini tutar.
# sirasiz, degistirilebilir, degerleri essiz
## performans odakli yapilardir hiz kazandirir

s = set() # to create a set.

myList = [1,"a","b",3]
s = set(myList)
s #output: {1, 3, 'a', 'b'}

myTuple = ("ali", "veli", 99)
s = set(myTuple)
s #output: {99, 'ali', 'veli'}

ad = "baran_acikgoz"
mySet = set(ad)
mySet #output: {'_', 'a', 'b', 'c', 'g', 'i', 'k', 'n', 'o', 'r', 'z'}

myLLList = ["elon", "musk", "elon", "jeff", "bezos", "bezos", "bezos"]
s = set(myLLList)
s #output: {'bezos', 'elon', 'jeff', 'musk'}


##### METHODS

# add() method adds element
mySet = set([1,2,"ali","baran"])
mySet.add("veli")
mySet #output: {1, 2, 'ali', 'baran', 'veli'}


# remove() method removes an element it returns an ERROR if the element which is to be removed doesn't occur.
mySet = set([1,2,"ali","baran"])
mySet.remove(1)
mySet.remove("baran")
mySet.remove("baran") #ERROR
mySet #output: {2, 'ali'}


# discard() methods removes an elements as well as remove() but doesn't returns ERROR if the object doesn't occur which should be removed.
mySet = set([1,2,"ali","baran"])
mySet.discard("baran")
mySet.discard("baran") #not error
mySet.discard("baran") #not error


# ****************************
# difference() iki kumenin farkini alir. Ayni sekilde "-"eksi ifadesi de farkini alir.
# intersection() iki kumenin kesimini alir. Ayni sekilde "&" ifadesi de kesisimini alir.
# union() ifadesi iki kumenin birlesimini alir.
# symmetric_difference() ikisinde de olmayan elemanlari return eder.
# ****************************


# *******************
# sonunda _update() olan fonksiyonlar return edilen deger ile icine yazilani günceller.
# mesela set1.intersection_update(set2) kodunun anlami: set1 ile set2 nin kesisimini al(1,3) ve bu kesisimi set1 olarak ata.
# bu islem sonucunda set1 artık {1,3}ten olusur, eskisi gibi {1,3,5} degildir.
# *******************


##difference()
set1 = set([1,3,5]) 
set2 = set([1,2,3])

set1.difference(set2)#set1'de olup 2de olmayan
#output: {5}
set1 - set2 #output: {5}

set2.difference(set1)#set2'de olup 1de olmayan
#output: {2}
set2 - set1 #output:{2}


## symmetric_difference()
set1 = set([1,3,5]) 
set2 = set([1,2,3])

set1.symmetric_difference(set2) # 1de olup 2de olmayan ve 2de olup 1de olmayanlar  aynı anda
#output: {2, 5}
set2.symmetric_difference(set1) #output: {2, 5}


## intersection()
set1 = set([1,3,5]) 
set2 = set([1,2,3])

set1.intersection(set2) #output: {1, 3}
set2.intersection(set1) #output: {1, 3}

set1 & set2 #output: {1, 3}
set2 & set1 #output: {1, 3}


## union() kesisim alma
set1 = set([1,3,5]) 
set2 = set([1,2,3])

set1.union(set2) #output: {1, 2, 3, 5}



## _update()
set1 = set([1,3,5]) 
set2 = set([1,2,3])

set1.intersection_update(set2)
set1 #output: {1, 3}

set1 = set([1,3,5]) 
set2 = set([1,2,3])

set2.difference_update(set1)
set2 #output: 2

set1 = set([1,3,5]) 
set2 = set([1,2,3])


# *************** SORGULAR

## isdisJoint() #returns true if two sets don't have an intersection, and returns false if two sets has an intersection
set1 = set([1,3,5]) 
set2 = set([1,2,3])

set1.isdisjoint(set2) #output: False (there is intersection)


## issubset() #altkumesi mi degil mi onu verir
s1 = set([7,8]) 
s2 = set([6,7,8,9])

s1.issubset(s2) #True -> s1 is a subset of s2


## issuperset()
s1 = set([7,8]) 
s2 = set([6,7,8,9])

s2.issuperset(s1) #output: True -> s2 is a superset of s1





