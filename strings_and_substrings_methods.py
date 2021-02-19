# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
print("Baran","Acikgoz", sep='_', end='***') #output: Baran_Acikgoz***

############ STRINGS ###########

# 'len' method shows length
a = "future_of_data"
len(a)

# upper() and lower() methods
a.upper() # output: 'FUTURE_OF_DATA'
a.lower() # output: 'future_of_data'
aUp = a.upper()

# isupper() and islower()
a.isupper() # to ask is upper or not
a.islower() # to ask is lower or not
aUp.isupper()

# replace() method replaces the old character to new character
a.replace("u", "a") # output: 'fatare_of_data'
# this doesn't changes the original a variable a is still "future of data"
replacedA = a.replace("u", "a") # new variable created "fatare_of_data"
a.replace("u", "") #deletes the u, output:'ftre_of_data' 

# strip() method removes from both sides the characters you've entered 
# strip() method's default parameter is ' '(space character)
b = " there_is_something_to_remove "
b.strip() #output:"there_is_something_to_remove"
food = '..rjq,,pizza.rq,j.r'
food.strip(".,rjq") #output: pizza

# center(length, fillChar(opt)) is the opposite of strip
b = 'add_a_character_both_side'
b.center(31, '*') #output: '***add_a_character_both_side***'

# capitalize() method makes only first character upper
cap = 'make me capital'
cap.capitalize() #output: Make me capital

# title() method capitalizes the first letter of every word
t = "i am a title"
t.title() #output: I Am A Title

# swapCase() converts all uppercase letters into lowercase and all lowercase letters into uppercase 
myVar = "eMin(thiEf) seEn by OwNeR whIle sToLe a BikE. He'S in HoSpiTal nOw."
myVar.swapcase() #output: "EmIN(THIeF) SEeN BY oWnEr WHiLE StOlE A bIKe. hE's IN hOsPItAL NoW."

# split() method divides string with commas and makes list, #split(seperator,maxsplit)
s = "i will start a career in data science"
s.split() #output: ['i', 'will', 'start', 'a', 'career', 'in', 'data', 'science']
strVal = "Name : Baran * Job : Engineer * Master : Data Science "
strVal.split("*") #output: ['Name : Baran ', ' Job : Engineer ', ' Master : Data Science ']
#**
myVar = "We would love to see you again, come early"
myVar.split("e") #output: ['W', ' would lov', ' to s', '', ' you again, com', ' ', 'arly']

# ljust(length, character(opt)) and rjust(length, character(opt)) method returns a left-justified version of the given string using a specified character, whitespace being default. The rjust() method aligns the string to the right.
text = 'I will became a data scientist'
sentence = 'and will start my own projects'
text.ljust(35, '_') + sentence #output: 'I will became a data scientist_____and will start my own projects'


# partition() method split string into a tuple consisting of three items: everything before the match, the match itself, and everything after the match.
myVar = "We will eat some delicious food and watch film"
myVar.partition('and') #output: ('We will eat some delicious food ', 'and', ' watch film')

# join() method is used to join all of the items in an iterable (list, dictionary, tuple, set, or even another string) to a string.
# takes one argument string.join(iterable)
myList = ["Lets", "make", "theese", "joint"]
a = "_".join(myList)
a #output: 'Lets_make_theese_joint'

# boolean startswith(value, startIndex(opt), endIndex(opt)) and endswith()
myVar = "$50 is the cost."
myVar.startswith("$") #output: true
schoolNum = "20190808014" 
schoolNum.endswith("08", 0,6) #output: true

# count(value, startIndex(opt), endIndex(opt))
myVar = 'I really really like to eat pizza'
myVar.count('really') #output: 2

# find(value, startIndex(opt), endIndex(opt)) and index() both are the finds the index of the value but find() return -1 if value is not occur while index() returns ERROR
myVar = 'I like to eat pizza really'
myVar.find('really') #output: 20
myVar.index("really") #output: 20
myVar.find('drink') #output: -1 (not found)
myVar.index('drink') #output: ValueError: substring not found

# format() has many uses and it can be applied on both string and numeric data to generate formatted output.
print("User has two dogs called {firstDog} and {secondDog}".format(firstDog="Dinky",secondDog="Prestige"))
print("User has two dogs called {} and {}".format("Dinky","Prestige"))
print("{2} is a student in {0} with number of {1}".format("CSE", "20190808014","Baran"))

######## SUBSTRINGS

myVar = "gelecegi_yazanlar"
myVar[0:3] #output: 'gel'
myVar[:3] #output 'gel'
myVar[-5:] #get the last 5 character #output:'anlar'
myVar[::2] #get the characters with 2 step forwarded



















