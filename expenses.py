suma=0
wydatki=[]
wydatki1=int(input("Wpisz liczbe wydatków: "))
for i in range(wydatki1):
    wydatki.append(float(input("Wpisz wydatek: ")))
suma =sum(wydatki)
print("Wydałes", suma,"zł")