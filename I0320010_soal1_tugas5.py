# program menyapa pengunjung hotel berdasar jenis kelamin

# menginputkan variabel
print('Isilah data pengunjung berikut!')
print("...............................")
nama_pengunjung = input('Siapakah nama Anda?: ')
jenis_kelamin = input('Apakah jenis kelamin Anda (P/L)?: ')

#Memproses data
if jenis_kelamin.upper() == 'P':
    print('Selamat datang, Nyonya ', nama_pengunjung)
else:
    print('Selamat datang, Tuan ', nama_pengunjung)
print()