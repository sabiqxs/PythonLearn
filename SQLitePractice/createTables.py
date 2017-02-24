import sqlite3

idPegawai = input('id pegawai: ')
namaPegawai = input('nama pegawai: ')
tanggalLahir = input('tanggal lahir: ')
gaji = input('gaji karyawan: ')
#
# print('input idPegawai: ', idPegawai)
# print('input nama pegawai: ', namaPegawai)
# print('input tanggal lahir', tanggalLahir)
# print('input gaji karyawan: ', gaji)
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
def read_from_db():
    c.execute('SELECT * FROM dataPegawai')
    # data = c.fetchall()
    # print(data)
    for row in c.fetchall():
        print(row)
def updateData():
    # c.execute('SELECT * FROM dataPegawai')
    # [print(row) for row in c.fetchall()]
    namaResult='gundul'
    namaSelect='jijik'
    c.execute("UPDATE dataPegawai SET namaPegawai = ? WHERE namaPegawai = ?", (namaResult, namaSelect))
    conn.commit()

    c.execute('SELECT * FROM dataPegawai')
    [print(row) for row in c.fetchall()]

def deleteData():
    c.execute("DELETE FROM dataPegawai WHERE namaPegawai = 'afuiiii' ")
    conn.commit()
    c.execute('SELECT * FROM dataPegawai')
    [print(row) for row in c.fetchall()]
# create_table()
data_entry()
# read_from_db()
# updateData()
deleteData()