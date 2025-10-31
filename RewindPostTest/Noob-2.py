import random
kode = ['AB7D', 'FCEK', 'SADW', ]

nama = 'farid'
nim = '087'

print('\nSelamat Datang di Menu Awal Pembayaran Uang Kuliah Tunggal')
print('\nSilahkan Login Terlebih Dahulu')

namainp = input('Masukkan Nama Anda: ')
niminp = input('Masukkan NIM Anda: ')
print()
print(random.choice(kode))
print()

kodeinp = input('Masukkan KODE: ')

if namainp == nama and niminp == nim:
    print('\nLogin Berhasil!')
elif namainp == nama or niminp == nim:
    print('Login Gagal!. Nama Atau NIM Salah')
    exit()
else:
    print('Login Gagal Wak')
    exit()

if kodeinp in kode:
    print()
else:
    print('Kode Salah! Silahkan Masukkan Kode Dengan Benar')
    exit()

print('''Total UKT Adalah Rp. 6.000.000, Silahkan Pilih Opsi Pembayaran
+----+-----------------+------------+
| No | Opsi Pembayaran |   Pajak    |
+----+-----------------+------------+
| 1. | Lunas           | 1%         |
| 2. | 2x Per Semester | 5%         |
| 3. | 4x Per Semester | 8%         |
| 4. | 6x Per Semester | 12%        |
+----+-----------------+------------+''')

pilih = int(input('Pilih Opsi Pembayaran (1- 4): '))

if pilih == 1:
    print('')