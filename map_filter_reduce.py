##################### map()
# elimizdeki bir fonksiyona, elimizdeki bir datanin elemanlarini sirasiyla gonderir ve sonucu tek bir obje olarak geri doner.
 
## example 1
liste = [1,2,3,4,5]

ab = list(map(lambda x: x**2, liste))
ab #output:[1, 4, 9, 16, 25]


##example 2
def starts_with_A(x):
    return x[0] == "A"
    
fruit = ["Apple", "Banana", "Apricot", "Orange"]
list(map(starts_with_A, fruit)) #output: [True, False, True, False]




##################### filter()
# sadece icindeki parametre olan fonksyiondan "true" gelen degerleri alarak bir obje olusturur.

#example 1
def starts_with_A(x):
    return x[0] == "A"
    
fruit = ["Apple", "Banana", "Apricot", "Orange"]
fruit_starts_A = list(filter(starts_with_A, fruit))
fruit_starts_A #output: ['Apple', 'Apricot']


#example 2
liste =[1,2,3,4,5,6,7,8,9,10]
cift_sayilar = list(filter(lambda x:x%2==0, liste))
cift_sayilar #output: [2, 4, 6, 8, 10]




##################### reduce()
# verdigimiz veri tipi icindeki elemanları azaltarak kiyaslama yapar ve azalta azalta kiyaslaya kiyaslaya en sonunda 1 tane deger dondurur.
# kar topu gibi arka arkaya toplamalarda ve kıyaslamalarda kullanılabilir mesela.
from functools import reduce

#example 1
def find_max(a,b):
    if a>b:
        return a
    else:
        return b

numbers = [11,3,9,12,4,15,66]
reduce(find_max, numbers) #output: 66


#example 2
liste = [1,2,3,4]
reduce(lambda a,b: a+b, liste) #output: 10
reduce(lambda a,b: a+b, liste, 22) #output: 32. This 22 is a initial base value. 22+10=32






