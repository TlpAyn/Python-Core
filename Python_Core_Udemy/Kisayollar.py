items =[
"ilk_oge",
"cable",
"keybods",
"pc",
"tahtaKalem",
"rrrr",
"son_oge"
]

print(len(items))

print("python " in items)
item= input("Bu egitimde hangi yazilim dili var ? ")

if item in items:
    print(item + " +  bilgisi var")
else:
    print("yok")


print("kac adet cable var ", items.count("rrrr") )

print("indexi nedir pc nin", items.index("pc") )

items.remove("pc")
print(items)
print(items.pop())
print(items.pop(0))
print(items)

number=[1, 2, 3, 4, 5, 6, 7, ]
print(max(number))