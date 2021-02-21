## Tuples are the same as 'Lists' except for tuples are constant(cannot be changed).

# tuple creating
myTuple = ("ali", "veli", 1,2,3,4, ['alfa', 1, 'beta'])
myTuple = "ali", "veli", 1,2,3,4, ['alfa', 1, 'beta']

#**** NOTE: if we want to create a tuple which has only one element, we have to add comma after the element otherwise it will be a string variable.
ttt = ("item") # type(ttt): str
ttt = ("item", ) # type(ttt): tuple
#

myTuple = ("ali", "veli", 1,2,3,4, ['alfa', 1, 'beta'])
# accessing the items is the same way as lists
myTuple[::2] #output: ('ali', 1, 3, ['alfa', 1, 'beta'])
myTuple[5:] #output: (4, ['alfa', 1, 'beta'])

myList = list(myTuple) # created a list.

######## METHODS

# max() method returns the item from the tuple with the highest value.
myTuple = (3,7,8,3,4,5,6)
max(myTuple) #output: 8

# min() method returns the item from the tuple with the lowest value.
myTuple = (3,7,8,3,4,5,6)
min(myTuple) #output: 3

# sum()  returns the arithmetic sum of all the items in the tuple.
myTuple = (3,7,8,3,4,5,6)
sum(myTuple) #output: 36

# sorted() returns a sorted version of the tuple. The sorting is in ascending order, and it doesn’t modify the original tuple in Python.
myTuple = (22,4,52,65,73,12,8)
a = sorted(myTuple) #output: [4, 8, 12, 22, 52, 65, 73]
type(a) # list

# index() can be use in same way

# count() can be use in same way

# any() If even one item in the tuple has a Boolean value of True, then this method returns True. Otherwise, it returns False.
myTuple = (1,0,1,0)
any(myTuple) #output: true
myTuple = ('baran',0,0)
any(myTuple) #output: true because string 'baran' does have a Boolean value of true
myTuple = (0,0,0)
any(myTuple) #output: false

# all() unlike any(); all() returns True only if all items have a Boolean value of True. Otherwise, it returns False.
myTuple = (1,0,1,0)
all(myTuple) #output: false

