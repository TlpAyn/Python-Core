alacaklar = set()

# print(dir(alacaklar))

# print(help(alacaklar.add))

alacaklar.add("araba")
alacaklar.add("ev")
alacaklar.add("kitap")
alacaklar.add("kagit")
alacaklar.add("kagit")

# alacaklar.clear()

# alacaklar.remove("armut")

alacaklar.discard("armut")

alacaklar= {'tel','mel','kel'}

print(alacaklar)


tek_sayilar=set([1,3,5,7,9,10])
cift_sayilar=set([2,4,6,8,10])

print(cift_sayilar.union(tek_sayilar))

print(cift_sayilar.intersection(tek_sayilar))