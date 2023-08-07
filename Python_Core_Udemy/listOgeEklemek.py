first,second,third="firstItem","secondItem","thirdItem"

items= [first,second,third]

print(items)
fourth= "fourthItem"
items.append(fourth)

print(items)

items[0]="birinci"
print(items)

print(items[-1])
print(len(items))

items.insert(4,"sonradan geldim gayri")
print(items)

items.insert(len(items), "Essah Son")

print(items)
print(items[2:3])


items_Sondan= items[::-1]
print(items_Sondan)



