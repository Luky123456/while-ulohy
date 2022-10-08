x=input("Zadaj mi slovo: ")
y=x
y=str(y)
z=0
f=0
dlzka=len(y)
while z != True:
    x = input("Zadaj mi slovo: ")
    y = x
    y = str(y)
    f=len(y)
    dlzka+=f
    z=y.startswith("x")
dlzka-=f
print("Počet znakov všetkých slov je:",dlzka)