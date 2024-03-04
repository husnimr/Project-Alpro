'''
Kelompok TIM : Error403Forbidden
1. J0303211150 Reneta Mega Zaskia
2. J0303211153 Husni Mubarok Ramadhan
3. J0303211154 Rohmat Hidayatulloh '''
print("<=================================>\n")
print("PROGRAM KONVERSI WAKTU (JAM,MENIT,DETIK)")
print("\n<=================================>")

print("1. Jam ke menit")
print("2. Jam ke detik")
print("3. Menit ke detik")
print("4. Menit ke jam")
print("5. Detik ke menit")
print("6. Detik ke jam")

print("<=================================>\n")

pilih = input("Pilih salah satu program konversi diatas(nomornya saja, contoh: 1): ")

if pilih == "1":
	print("\n==== Konversi jam ke menit ====")
	pilsatu = int(input("Masukan jumlah jam (angka saja): "))
	jamkemenit = pilsatu*60
	print(pilsatu, "jam sama dengan",jamkemenit,"menit")
elif pilih == "2":
	print("\n==== Konversi jam ke detik ====")
	pildua = int(input("Masukan jumlah jam (angka saja): "))
	jamkedetik = pildua*3600
	print(pildua, "jam sama dengan",jamkedetik,"detik")
elif pilih == "3":
	print("\n==== Konversi menit ke detik ====")
	piltiga = int(input("Masukan jumlah menit (angka saja): "))
	menitkedetik = piltiga*60
	print(piltiga, "menit sama dengan",menitkedetik,"detik")
elif pilih == "4":
	print("\n==== Konversi menit ke jam ====")
	pilempat = int(input("Masukan jumlah menit (angka saja): "))
	menitkejam = pilempat/60
	print(pilempat, "menit sama dengan",menitkejam,"jam")
elif pilih == "5":
	print("\n==== Konversi detik ke menit ====")
	pillima = int(input("Masukan jumlah detik (angka saja): "))
	detikkemenit = pillima/60
	print(pillima, "detik sama dengan",detikkemenit,"menit")
elif pilih == "6":
	print("\n==== Konversi detik ke jam ====")
	pilenam = int(input("Masukan jumlah detik (angka saja): "))
	detikkejam = pilenam/3600
	print(pilenam, "detik sama dengan",detikkejam,"jam")
else:
	print ('\nPilihan konversi yang anda masukan salah, harap coba lagi!')
