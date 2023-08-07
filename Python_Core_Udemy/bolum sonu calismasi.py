age = input ("lutfen sayigiriniz" )

if not age.isdigit():
    print("yasi dogru giriniz")
else:
    if  int(age)>18:
        print("18 den buyuk")
    else:
        print("18 yasindan kucuk")