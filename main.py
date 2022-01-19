mahasiswa = []
no = 1
while True:
    nama =str(input("masukan nama :".format(no)))
    nim =int(input("masukan NIM :".format(no)))
    nilai = [0, 0, 0]
    nilai_tugas = int(input("masukan nilai tugas :"))
    nilai_uts = int(input("masukan nilai uts :"))
    nilai_uas = int(input("masukan nilai uas"))

    nilai[0] = nilai_tugas
    nilai[1] = nilai_uts
    nilai[2] = nilai_uas
    akhir = float(nilai_tugas / 3.5 + nilai_uts / 3.5 + nilai_uas / 3.5)

    tambah = ('|' + str(no) + '|' + str(nama) + '|' + 
    str(nim) + '|' + str(nilai_tugas) + '|' + str(nilai_uts) + '|' + 
    str(nilai_uas) +'|' + "%.2f" % (akhir) + '|'.format(no))
    mahasiswa.append(tambah)
    verify = input('tambah data ? (y/n)')
    if verify == 'y':
        mahasiswa = mahasiswa
        no += 1
    else:
        print ('===============================================')
        print ('| no | nama | Nim | tugas | uts | uas | akhir |')
        print ('===============================================')
        for data in mahasiswa:
            print(format(data))
        print('=================================================')
        exit()
