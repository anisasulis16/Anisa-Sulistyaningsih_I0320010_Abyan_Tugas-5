# Membuat program grading nilai
print('Selamat datang di program penilaian')
print('...................................')

# Menginputkan data
nama_siswa = input('Siapakah nama Anda?: ')
nilai = int(input('Berapa nilai Anda?: '))


# Memproses data
if nilai >= 85:
    print('Halo,',nama_siswa, '!' , 'Nilai Anda setelah dikonversi adalah A')
elif nilai >= 80:
    print('Halo,', nama_siswa, '!' , 'Nilai Anda setelah dikonversi adalah A-')
elif nilai >= 75:
    print('Halo,', nama_siswa, '!' , 'Nilai Anda setelah dikonversi adalah B+')
elif nilai >= 70:
    print('Halo,', nama_siswa, '!' , 'Nilai Anda setelah dikonversi adalah B')
elif nilai >= 65:
    print('Halo,', nama_siswa, '!' , 'Nilai Anda setelah dikonversi adalah C+')
elif nilai >= 60:
    print('Halo,', nama_siswa, '!' , 'Nilai Anda setelah dikonversi adalah C')
else:
    pass
print()

