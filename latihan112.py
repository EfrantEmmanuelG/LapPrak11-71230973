def data(nama_lengkap, nim, alamat):
    gabung = nama_lengkap, nim, alamat
    print("Data:", tuple(gabung))
    print("\n")
    print("NIM      :", ' '.join(nim))
    print("NAMA     :", ' '.join(nama_lengkap))
    print("ALAMAT   :", alamat)
    print('\n')
    print("NIM:", tuple(nim))
    print("NAMA DEPAN:", tuple(nama_lengkap.split()[0]))
    print("NAMA TERBALIK:", tuple(nama_lengkap.split()[::-1]))

nama_lengkap = 'Efrant Emmanuel Gunawan'
nim = '71230973'
alamat = 'Cihideung, di Tasikmalaya'

data(nama_lengkap, nim, alamat)
