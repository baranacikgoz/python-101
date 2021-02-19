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


## remove() , extend(), count(), index(), copy(), sort(), reverse(), clear()





