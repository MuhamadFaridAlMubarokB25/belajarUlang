nama = 'farid'
nim = '2509106087'

namainput = input('Masukkan Nama Anda: ')
niminput = input('Masukkan NIM Anda: ')

print("""
+---------------+-------------+
|     Menu      |    Pajak    |
+---------------+-------------+
| Pecel lele    | 5%          |
| Mie Ayam      | 8%          |
| Nasi Padang   | 10%         |
+---------------+-------------+""")

harga = int(input('\nMasukkan Harga Makanan: '))

pecel = harga * (5 / 100)
mie = harga * (8 / 100)
nasi = harga * (20 / 100)

totalpecel = harga + pecel
totalmie = harga + mie
totalnasi = harga + nasi

print(f'\n{nama} dengan NIM {nim} ingin membeli makanan seharga (Rp inputan Harga makanan)')

print(f'Jika dia membeli pecel lele, maka ia harus membayar {totalpecel} setelah mendapat pajak 5%.')
print(f'Jika dia membeli mie ayam, maka ia harus membayar {totalmie} setelah mendapat pajak 8%.')
print(f'Jika dia membeli nasi padang ia harus membayar Rp {totalnasi} setelah mendapat pajak 10%.')






