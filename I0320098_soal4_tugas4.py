# Syarat
#1. Usia minimal 21 tahun
#2. Lulus ujian kualifikasi

a = int(input('Berapa usia kamu?'))
b = input("Apakah Anda sudah lulus ujian kualifikasi (Y/T)?")

if a >= 21 and b == 'Y' :
    print("Anda dapat mendaftar di kursus")
else :
    print("Anda tidak dapat mendaftar di kursus")