firstName= "talip"
lastName="ayan"

fullName = firstName[0].upper() + " " + lastName

print(fullName)

fullName = f"Merhaba {firstName[0].upper()}.{lastName}"

print(fullName)

print("sonuc "+ str(10 *10)) # calismaz cunku str ile int birlesmez.

def calculate (number ):
    return number * number

print(calculate(10))