# Dictionary is used in python to store multiple data with key-value pairs.
# non-indexed (sırasız, listelerdeki gibi indexleme islemleri yapilamaz)

myDict = {
    "BTC" : "Bitcoin",
    "ETH" : "Ethereum",
    "TWT" : "Trust Wallet Token"
    }
# there are 3 item, not 6
len(myDict) # 3

# value don't have to be one element
myDict = {
    "BTC" : ["Bitcoin", "BTC/USDT", 1, 2],
    "ETH" : ["Ethereum", "ETH/USDT", 3, 4],
    "TWT" : ["Trust Wallet Token", "TWT/USDT", 5, 6]
    }

# as its non-indexed the code below will be throw an ERROR
myDict[1] #KeyError

# this is true:
myDict["ETH"] #output: ['Ethereum', 'ETH/USDT', 3, 4]

##** dictionary supports nested builds
myDict = {
    "Languages" : {"Python" : "PYT" ,
                    "Java" : "J",
                    "Dart" : "Flutter"
                   },
    
    "Hardware" : {"Intel" : "Core i5",
                  "AMD" : "A9-9425",
                  "Nvidia" : "RTX 3090"
                  }
         }

myDict["Languages"]["Java"] #output: 'J'
myDict["Hardware"]["Nvidia"] #output: 'RTX 3090'
 
# adding & changing
myDict = {
    "BTC" : ["Bitcoin", "BTC/USDT", 1, 2],
    "ETH" : ["Ethereum", "ETH/USDT", 3, 4],
    "TWT" : ["Trust Wallet Token", "TWT/USDT", 5, 6]
    }

myDict["CHZ"] = "Chiliez Coin"
myDict #...... 'CHZ': 'Chiliez Coin'}

##** NOTE: since lists are not constant, we cant assign a list as a key
lll = ["this","is","a","list","as","a","key"]
myDict[lll] = 'key of the list'

##** this will work since tuple is constant
ttt = ("this","is","a","TUPLE","as","a","key")
myDict[ttt] = 'value of the ttt'
myDict #...('this', 'is', 'a', 'TUPLE', 'as', 'a', 'key'): 'value of the ttt'}

myDict["BTC"] = ["btc is future", 99]


######## METHODS

## items() method is used to return a list with the tuple pairs(as 'dict_items') of all keys and values of a dictionary.
# **ONEMLI: items() methoduyla oluşturulan bir degisken, dictionarynin her zaman yansımasıdır yani en başta items = dictionary.items()
#seklinde bir items degiskeni olustursan ondan sonra dictionaryyi güncellesen print(items) yazdıgında dictionarynin guncel hali gelir eski hali degil
myDict = {
    "BTC" : ["Bitcoin", "BTC/USDT", 1, 2],
    "ETH" : ["Ethereum", "ETH/USDT", 3, 4],
    "TWT" : ["Trust Wallet Token", "TWT/USDT", 5, 6]
    }
crypto_tuple = myDict.items()
crypto_tuple # dict_items([('BTC', ['Bitcoin', 'BTC/USDT', 1, 2]), ('ETH', ['Ethereum', 'ETH/USDT', 3, 4]), ('TWT', ['Trust Wallet Token', 'TWT/USDT', 5, 6])])


## keys() method is used to return a list of all keys of a dictionary.
# **ONEMLI : itemstaki olayın aynisi bunda da gecerli
myDict = {
    "BTC" : ["Bitcoin", "BTC/USDT", 1, 2],
    "ETH" : ["Ethereum", "ETH/USDT", 3, 4],
    "TWT" : ["Trust Wallet Token", "TWT/USDT", 5, 6]
    }
my_keys = myDict.keys()
my_keys #output: dict_keys(['BTC', 'ETH', 'TWT'])


## setdefault() method is used to get the value of any particular key from a dictionary if the key exists.
#kısaca eger girdigin key'e karsilik bir deger zaten var ise, setdefault kullanırken yanına yeni bir value yazsan bile onu kabul etmiyor eski valuesu kalıyor.
#Ancak girdigin key yok ise yeni key olusuturup setdefault() yazarken parametre olarak verdigin valueyu da o keyin valuesi yapıyor.
# dictionary.setdefault(key_value [, default_value])
myDict = {
    "BTC" : ["Bitcoin", "BTC/USDT", 1, 2],
    "ETH" : ["Ethereum", "ETH/USDT", 3, 4],
    "TWT" : ["Trust Wallet Token", "TWT/USDT", 5, 6]
    }

myDict.setdefault("BTC") #output: ['Bitcoin', 'BTC/USDT', 1, 2]
myDict.setdefault("BTC", 'bitccccoin') # 'bitccccoin' had not taken as value because "BTC" key already had value as ['Bitcoin', 'BTC/USDT', 1, 2]
myDict.setdefault("XRP", "Ripple")
myDict # .....'XRP': 'Ripple'}


## get() method is similar to setdefault() but get() method doesnt creates a new key and value if doesnt exists which setdefault() creates.
## **ONEMLI: dictionaryde olmayan bir seyi get() ile cagirirken get(para, 0.0) seklinde yazarsak, dictionaryye para keyini eklemez ama return olarak para = 0.00 dondurur.
# mesela
person = {
    'name': 'Phill', 
    'age': 22
    }
print("isim: ", person.get("name", "eger ismi yoksa baran olsn")) #output: isim:  Phill
print("aldigi maas: ", person.get("maas" , "eger maasi yoksa 0.00")) #output: aldigi maas:  eger maasi yoksa 0.00
 

# dictionary.get(key_value , default_value)
myDict = {
    "BTC" : ["Bitcoin", "BTC/USDT", 1, 2],
    "ETH" : ["Ethereum", "ETH/USDT", 3, 4],
    "TWT" : ["Trust Wallet Token", "TWT/USDT", 5, 6]
    }

myDict.get("ONT", "ONT coin") #
myDict # didn't add "ONT" : "ONT coin"

myDict.get("BTC") #output: ['Bitcoin', 'BTC/USDT', 1, 2]
myDict.get("BTC", "bitttcoooinn") # same as setdefault(); the value of the "BTC" is still ['Bitcoin', 'BTC/USDT', 1, 2] 


## The pop() method is used to remove the element from a dictionary based on the key value. It RETURNS the value of removed key.
# **ONEMLI: eger pop()a yazdıgın key var ise siler ve sildigi keyin valuesini return eder. Eger yazdıgın key yok ise ama pop(olmayan_key, rastgele_value) seklinde iki argumanı da yazarsan, o key olmadıgı halde 2. yazdıgın arguman olan valueyi yine de return eder.
# dictionary.pop(key [, value])
myDict = {
    "BTC" : ["Bitcoin", "BTC/USDT", 1, 2],
    "ETH" : ["Ethereum", "ETH/USDT", 3, 4],
    "TWT" : ["Trust Wallet Token", "TWT/USDT", 5, 6]
    }

removed_coin = myDict.pop("TWT")
myDict # there is no more '"TWT" : ["Trust Wallet Token", "TWT/USDT", 5, 6]'   myDict = {'BTC': ['Bitcoin', 'BTC/USDT', 1, 2], 'ETH': ['Ethereum', 'ETH/USDT', 3, 4]}
removed_coin # output: ['Trust Wallet Token', 'TWT/USDT', 5, 6]

eger_var_ise_silindi = myDict.pop("RVN", "Raven Coin")
print("pop('RVN') yazdıginiz icin eger 'RVN' keyi sozlukte var ise valuesi olan: ",eger_var_ise_silindi, "silindi")


## update() method is used between two dictionaries.  If any key of the second dictionary matches with any key of the first dictionary then the corresponding value of the first dictionary will be updated by the corresponding value of the second dictionary. The keys of the second dictionary that do not match with any key of the first dictionary those elements of the second dictionary are added at the end of the first dictionary.

old_employees = {"Baran" : "Salary: 100",
                 "Ali" : "Salary: 200",
                 "Ahmet" : "Salary: 300"
    }
new_employees = {"Yakup" : "Salary : 300",
                 "Mustafa" : "Salary : 200",
                 "Baran" : "Salary : 600",
                 "Ali" : "Salary : 400"
    }

old_employees.update(new_employees)
# old_employees {'Baran': 'Salary : 600',
#  'Ali': 'Salary : 400',
#  'Ahmet': 'Salary: 300',
#  'Yakup': 'Salary : 300',
#  'Mustafa': 'Salary : 200'}


## fromkeys() method creates a new dictionary from the given sequence of elements with a value provided by the user.
# dictionary.fromkeys(sequence[, value])
myDict = {
    "BTC" : ["Bitcoin", "BTC/USDT", 1, 2],
    "ETH" : ["Ethereum", "ETH/USDT", 3, 4],
    "TWT" : ["Trust Wallet Token", "TWT/USDT", 5, 6],
    "RVN" : 'Raven Coin'
    }

keys = ["ETH", "RVN"]
values = ["value"]

newDict = myDict.fromkeys(keys, values)
newDict # {'ETH': ['value'], 'RVN': ['value']}

## copy() method can be used as the same

## clear() method can be used as the same

