# # sayilar = ()

# # print(type(sayilar))

# sayilar = (1,3,4,55,66,77,45)

# print(sayilar)
# print(sayilar[2])


# sayilar_liste= [1,3,55,666,777,88,999]
# print(sayilar_liste)

# for i in sayilar_liste:
#     print(i)


# sayi_b = True
# print(type(sayilar[2]))


# deneme_sayilar =1,2,3,4,5,67,6
# print(deneme_sayilar)

# print(type(deneme_sayilar))


# isim,soyisim,age=('ali','veli',33)

# print(isim)
# print(age)

# new_tuple = ('kml','asln','44')

# print(new_tuple)

# ad= 'ali'
# soyad="yilmaz"

# print(ad)
# print(soyad)

import sys

print(help(sys.getsizeof))


isim_listesi= ['kalem','defter','kagit']
tuple_listesi= ('kalem','defter','kagit')

print(sys.getsizeof(isim_listesi))
print(sys.getsizeof(tuple_listesi))

print(dir(isim_listesi))
print('_____'*200)
print(dir(tuple_listesi))

print(len(isim_listesi))




