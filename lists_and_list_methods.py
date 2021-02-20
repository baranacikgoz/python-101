######## LISTS AND LIST METHODS
#[]
#list()

random = ['ali', 20, 'baran', 10, 'veli', 12.5]
numbers_and_notes = [["ali","baran","veli"],[10,20,30]]
schools_students_info = ["akdeniz uni", numbers_and_notes]

type(schools_students_info[0]) #output: string

all_in_one_list = [random, numbers_and_notes, schools_students_info]

del all_in_one_list # deletes the list if we've finished the deal with it and dont want to use much ram

names_notes = ['ali', 20, 'baran', 10, 'veli', 12.5]
names_in_names_notes = names_notes[::2]
names_in_names_notes #output: ['ali', 'baran', 'veli']

names_in_names_notes[:2] = "ahmet", "mehmet"
names_in_names_notes #output: ['ahmet', 'mehmet', 'veli']

listtt = ['mustafa', 'kemal', 'ataturk']
listtt += ["salih"] + ["bozok"]
listtt #output: ['mustafa', 'kemal', 'ataturk', 'salih', 'bozok']
del listtt[-1] #output: ['mustafa', 'kemal', 'ataturk', 'salih']

####### METHODS

## insert() method adds a value in a specific position
# insert(position, item)
myList = ['Asus', 'Nvidia', 'GigaByte']
myList.insert(1, 'AMD')
myList #output: ['Asus', 'AMD', 'Nvidia', 'GigaByte']

## append() method adds a value at the end of the list.
# append(item)
myList = ['Asus', 'Nvidia', 'GigaByte']
myList.append('AMD')
myList #output: ['Asus', 'Nvidia', 'GigaByte', 'AMD']

##index(), copy(), sort(), reverse(), clear()

## remove() method is used to remove a particular item from the list.
# list.remove(item)

myList = ['Asus', 'Nvidia', 'GigaByte', 'Lenovo', 'AMD']
myList.remove('Lenovo')
myList #output: ['Asus', 'Nvidia', 'GigaByte', 'AMD']

## extend() method is used to merge two list items and store the merged items in the first list.
#first_list.extends(second_list)
a = ['Asus', 'Nvidia', 'GigaByte']
b = ['Alpha', 'Gamma', 'Beta']
a.extend(b)
a #output: ['Asus', 'Nvidia', 'GigaByte', 'Alpha', 'Gamma', 'Beta']
a += b #output: ['Asus', 'Nvidia', 'GigaByte', 'Alpha', 'Gamma', 'Beta']
#**** NOTE: if we use append instead of extend the result will be list in list: ['Asus','Nvidia','GigaByte',['Alpha', 'Gamma', 'Beta']]

## count() method is used to count the number times that any given item appears in a list.
# list.count(item)
a = [3,5,7,'ahmet',12,5,'ahmet',22,23,'veli', 'ahmet']
a.count(5) #output: 2
a.count("ahmet") #output: 3

## index() method is used to obtain the position value of any item in the list if it exists; otherwise, it generates a ValueError.
#list.index(item)
a = [3,5,7,'ahmet',12,5,'ahmet',22,23,'veli', 'ahmet']
a.index('ahmet')

## copy() method is used to make a copy of a list.
# list.copy() doesn't take any argument

a = [1,2,3]
b = [4,5,6]
aOriginal = a.copy()
a.extend(b)
a #output: [1, 2, 3, 4, 5, 6]
aOriginal #[1, 2, 3]
 
## sort() method is used to sort list data.
# list.sort() doesn't take any argument

a = [12,15,2,22,17,9,7]
a.sort()
a #output: [2, 7, 9, 12, 15, 17, 22]

## reverse() method is used to reverse the items in any list.
# list.reverse() doesn't take any argument

a = [12,15,2,22,17,9,7]
a.sort() # [2, 7, 9, 12, 15, 17, 22]
a.reverse()
a #output: [22, 17, 15, 12, 9, 7, 2]

## clear() method is used to remove all the items in a list and to empty lists. 
# list.clean() doesn't take any argument

a = [12,15,2,22,17,9,7]
a.clear()
a #output: []

