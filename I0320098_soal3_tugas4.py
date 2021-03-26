#Berat maksimum bagasi
x = 50              #Berat maksimum dalam satuan Ibs
y = x * 0.454       #Berat maksimum dalam satuan kg
print("Berat maksimun yang diperbolehkan yaitu", y, "kg")


#Input berat bagasi dalam satuan kg
a = float(input('Berat bagasi pertama (kg):'))    # berat lebih dari 110 kg
b = float(input('Berat bagasi kedua (kg):'))    # berat 49 kg

print("Berat bagasi pertama:", a, "kg", a<=y)
print("Berat bagasi kedua:", b, "kg", b<=y)