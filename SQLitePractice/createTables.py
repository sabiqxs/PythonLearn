import sqlite3

idPegawai = input('id pegawai: ')
namaPegawai = input('nama pegawai: ')
tanggalLahir = input('tanggal lahir: ')
gaji = input('gaji karyawan: ')

print('input idPegawai: ', idPegawai)
print('input nama pegawai: ', namaPegawai)
print('input tanggal lahir', tanggalLahir)
print('input gaji karyawan: ', gaji)
conn = sqlite3.connect('learnSQL.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dataPegawai(idPegawai REAL, namaPegawai VARCHAR, tanggalLahir VARCHAR, gaji REAL)')

def data_entry():
    c.execute("INSERT INTO dataPegawai VALUES(?, ?, ?, ?)",(idPegawai, namaPegawai, tanggalLahir, gaji))
    print('Inputing data was successed')
    conn.commit()
    c.close()
    conn.close()

# create_table()
data_entry()