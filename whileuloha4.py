x=input("Zadaj mi číslo: ")
y=x
y=int(y)
počet=0
výsledok=0
while x != 0:
    x = input("Zadaj mi číslo: ")
    x=int(x)
    y+=x
    počet+=1
výsledok=y/int(počet)
print("Artitmetický priemer čísel bol",výsledok)
