class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def info(self):
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)
        print("Prodi:", self.prodi)
        print("Fakultas:", self.fakultas)
        print("Tempat Tinggal:", self.tempat_tinggal)
        print("Asal:", self.asal)

mahasiswa1 = Mahasiswa("Muhammad Nursan", "A", "Pendidikan Komputer", "FKIP", "Perum. Dosen Unmul Sempaja", "Muara Badak")

mahasiswa1.info()


