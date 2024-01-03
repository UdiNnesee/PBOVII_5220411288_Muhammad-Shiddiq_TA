class Pendidikan:
    def __init__(self, nama):
        self.__nama = nama

    def get_nama(self):
        return self.__nama
    
    def tampil_hasil(self):
        print(f'Nama          : {self.get_nama()}')

class Perguruan_Tinggi(Pendidikan):
    def __init__(self, nama, nama_perguruan_tinggi, program_studi, tingkat, ujian_skripsi, semes1, semes2, semes3, semes4, semes5, semes6, semes7, semes8):
        super().__init__(nama)
        self.__nama_perguruan_tinggi = nama_perguruan_tinggi
        self.__program_studi = program_studi
        self.__tingkat = tingkat
        self.ujian_skripsi = ujian_skripsi
        self.ips_seluruh = [semes1, semes2, semes3, semes4, semes5, semes6, semes7, semes8]

    def get_nama_pt(self):
        return self.__nama_perguruan_tinggi
    
    def get_program_studi(self):
        return self.__program_studi
    
    def get_tingkat(self):
        return self.__tingkat
    
    def hitung_ipk(self):
        ipk = sum(self.ips_seluruh)/len(self.ips_seluruh)
        return ipk
    
    def syarat_lulus(self):
        if self.hitung_ipk() > 2 and self.ujian_skripsi == 'Lulus':
            print(f'Lulus {self.get_tingkat()}\n')
        else:
            print(f'Tidak Lulus\n')

    def tampil_nilai_ips(self):
        angka = 1
        for semester in range(len(self.ips_seluruh)):
            print(f"IP Semester {angka} : {self.ips_seluruh[semester]}")
            semester += 1
            angka += 1

    def tampil_hasil(self):
        super().tampil_hasil()
        print(f'Perguruan_Tinggi   : {self.get_nama_pt()}')
        print(f'Program Studi      : {self.get_program_studi()}')
        print(f'Tingkat            : {self.get_tingkat()}')
        self.tampil_nilai_ips()
        self.syarat_lulus()

class SLTA(Pendidikan):
    def __init__(self, nama, nama_sekolah, jurusan, agama, bindo, binggris, matematika, pkn):
        super().__init__(nama)
        self.__nama_sekolah = nama_sekolah
        self.__jurusan = jurusan
        self.nilai_ijazah = [agama, bindo, binggris, matematika, pkn]

    def get_nama_sekolah(self):
        return self.__nama_sekolah
    
    def get_jurusan(self):
        return self.__jurusan
    
    def tampil_nilai_mapel(self):
        piv = 0
        for nilai_mapel in range(len(self.nilai_ijazah)):
            print(f"Nilai {simpan_mapel[piv]} : {self.nilai_ijazah[nilai_mapel]}")
            nilai_mapel += 1
            piv += 1
    
    def hitung_rata_rata(self):
        rata_rata_nilai = sum(self.nilai_ijazah)/len(self.nilai_ijazah)
        return rata_rata_nilai

    def syarat_lulus(self):
        if self.hitung_rata_rata() >= 70:
            print('Lulus\n')
        else:
            print('Tidak Lulus\n')

    def tampil_hasil(self):
        super().tampil_hasil()
        print(f'Sekolah       : {self.get_nama_sekolah()}')
        print(f'Jurusan       : {self.get_jurusan()}')
        self.tampil_nilai_mapel()
        self.syarat_lulus()

class SMK(SLTA):
    def __init__(self, nama, nama_sekolah, jurusan, agama, bindo, binggris, matematika, pkn, ukk):
        super().__init__(nama, nama_sekolah, jurusan, agama, bindo, binggris, matematika, pkn)
        self.ukk = ukk

    def tampil_nilai_mapel(self):
        super().tampil_nilai_mapel()
        print(f'Nilai UKK : {self.ukk}')
    
    def syarat_lulus(self):
        if self.hitung_rata_rata() >= 70 and self.ukk >= 70:
            print('Lulus\n')
        else:
            print('Tidak Lulus\n')

    def tampil_hasil(self):
        super().tampil_hasil()
        
simpan_mapel = ['Agama', 'Bahasa Indonesia', 'Bahasa Inggris', 'Matematika', 'PKN']

def run():
    kuliahan = Perguruan_Tinggi('Anandava Eka Buana Baskara', 'Universitas Teknologi Yogyakarta', 'Informatika', 'S1', 'Lulus', 3.70, 3.75, 3.85, 3.9, 3.95, 3.97, 3.99, 4)
    sekolahan1 = SLTA('Alzera Wahyu Alif', 'SMA Negeri 50 Jakarta Timur', 'IPS', 96, 84, 80, 82, 77)
    sekolahan2 = SMK('Muhammad Rizki Ananda', 'SMK', 'Rangkaian Perangkat Lunak', 90, 87, 80, 85, 88, 95)
    kuliahan.tampil_hasil()
    sekolahan1.tampil_hasil()
    sekolahan2.tampil_hasil()

run()