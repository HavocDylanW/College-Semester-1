import random
from time import time
import os

# Import module border #

usrnme = []
usrnis = []

def biodataUser():

    # Input Biodata pemain. #

    print ("="*41)
    print ("[!] Silahkan masukan Biodata sebelum bermain!")
    print ("-"*41)

    # Input menggunakan append agar Biodata User masuk kedalam list. #

    usrnme.append (input("[!] Nama : "))
    usrnis.append (input("[!] NIS  : "))
    print ("-"*42)
    print ("[?] Apakah Biodata yang dimasukan sudah benar?")
    print ("    [1] Benar            [2] Salah")

    # Looping untuk mencegah error karena kesalahan Input User. #

    ulangBiodata = input("Masukan Pilihan : ")

    while True:
        if ulangBiodata == "1":
            quizMenu()
            break
        elif ulangBiodata == "2":
            del usrnme[0]
            del usrnis[0]
            biodataUser()
            break

        print ("[!!] Tidak ada pilihan yang sesuai! Silahkan pilih kembali,")
        print ("[?] Apakah Biodata yang dimasukan sudah benar?")
        print ("    [1] Benar            [2] Salah")
        ulangBiodata = input("Masukan Pilihan : ")


# Quiz Menu #

def quizMenu():

    os.system('cls')
    print ("="*32, "Quiz Biologi", "="*32)
    print ("  Selamat datang", *usrnme,"di Quiz Biologi! Silahkan pilih Bab yang diinginkan!")
    print (" ", "-"*74)
    print ("[1] Bab I   Ruang Lingkup Biologi")
    print ("[2] Bab II  Virus")
    print ("[3] Bab III Bakteri")
    print ("[4] Bab IV  Protista")
    print ("[5] Bab V   Fungi")
    print ("\n\n[9] Exit")
    print ("="*78)

    pilihBab = input("Masukan Pilihan : ")

    # Looping untuk mencegah error karena kesalahan Input User. #

    while True:
        if pilihBab == "1":
            bab1()
            break
        elif pilihBab == "2":
            bab2()
            break
        elif pilihBab == "3":
            bab3()
            break
        elif pilihBab == "4":
            bab4()
            break
        elif pilihBab == "5":
            bab5()
            break
        elif pilihBab == "9":
            exit
            break

        print ("\n[!!] Tidak ada Bab dengan pilihan tersebut, silahkan pilih kembali!")
        pilihBab = input("Masukan Pilihan : ")

### Bab I #################
# Ruang Lingkup Biologi   #
###########################

def bab1():

    # Mendefinisikan variable dan list untuk penyimpanan data yang diraih dari Input User. #

    historyUser = []
    scoreBenar = 0
    scoreSalah = 0
    nomor = 0

    ##
    mulaiTimer = time()

    # Menyatukan list, range dalam list pertanyaan menggunakan metode Zip, dan mendefinisikannya. #
    # List pertanyaan yang telah disatukan, kemudian di shuffle menggunakan module random. #

    # Metode Zip / Zip function digunakan untuk membentuk iterator berisi item dengan cara mendapatkan #
    # iterable (bisa satu atau lebih) yang kemudian digabungkan ke dalam tuple dan dikembalikan. #

    # Iterable berupa satu atau lebih iterator yang terdiri dari string, list tuple, dict dan lain lain. #

    order = list(range(len(pertanyaanBab1)))
    random.shuffle(order)

    os.system ('cls')
    print ("="*32)
    print ('|', "Bab I", "                      |")
    print ('|', "Ruang Lingkup Biologi", '      |')
    print ("="*32)

    # Pemanggilan pertanyaan menggunakan fungsi For untuk melakukan perulangan dalam interval suatu list #

    for i in order:
        # Memberikan nilai pada nomor untuk setiap interval yang dikeluarkan, untuk mencetak nomor soal #
        # setiap perulangan dilakukan. #

        # Menggunakan huruf " f " sebelum tanda kutip agar dapat menulis {ekspresi}. #

        # [i] disini merujuk pada interval, sedangkan [0] ataupun [1] merujuk pada urutan suatu list. #
        nomor += 1
        print (f'\nPertanyaan {nomor}')
        print ('[?]', pertanyaanBab1[i][0])
        print (' ','\n  '.join(jawabanBab1[i]))

        # Menggunakan fungsi .upper() untuk merubah string dari Input User menjadi huruf kapital, #
        # sekaligus mencegah error yang di akibatkan oleh Input User menggunakan huruf kecil. #

        # Menyimpan jawaban user menggunakan .append dalam setiap bab agar dapat dicetak kembali. #

        jawabanUser = input('Jawab : ').upper()
        historyUser.append (jawabanUser)

        if jawabanUser == pertanyaanBab1[i][1]:
            print ('\n~ Jawaban tepat! ~')
            scoreBenar += 1
        else:
            print ('Jawaban yang tepat adalah', *pertanyaanBab1[i][1],'bukan', jawabanUser)
            scoreSalah += 1

    ##
    selesaiTimer = time()

    # Penjumlahan nilai User berdasarkan tepatnya jawaban yang di input. #
    # Dan, mencetak kembali seluruh data yang telah disimpan dalam variable maupun list. #

    nilai = scoreBenar * 10
    totalTimer = selesaiTimer - mulaiTimer

    print ('\n')
    print ('[!]','='*72,'[!]')
    print (' '*36, 'Hasil Quiz')
    print ('   ','='*72,'   ')
    print ('    Nama : ', *usrnme)
    print ('    NIS  : ', *usrnis)
    print ('    Berikut adalah hasil Quiz yang diraih oleh siswa dengan identitas diatas')
    print ('   ','-'*72,'   ')

    # Menggunakan fungsi .join untuk mengubah Array list menjadi string saat akan dicetak. #

    print ('    Waktu mengerjakan yang diraih : ', '%.2f'% totalTimer, 'Detik!')
    print ('    History Jawaban               : ', ' '.join(historyUser))
    print ('    Jawaban tepat yang diraih     : ', scoreBenar)
    print ('    Jawaban salah yang diraih     : ', scoreSalah)
    print ('    Nilai yang diraih             : ', nilai)

    print ("\n[?] -----------------------------[ Quiz Menu ]------------------------------ [?]")
    print ("  [1] Lanjutkan Bab (Bab II)      [2] Kembali ke Menu Bab       [3] Exit")

    mengulang = input("\nMasukan Pilihan : ")

    # Looping untuk mencegah error karena kesalahan Input User. #
    # Menggunakan fungsi break, agar mencegah terjadinya error berupa loop yang terus berulang. #

    while True:
        if mengulang == "1":
            bab2()
            break
        elif mengulang == "2":
            quizMenu()
            break
        elif mengulang == "3":
            exit
            break
        
        print ("\nTidak ada pilihan yang sesuai! Silahkan pilih kembali,")
        mengulang = input("Masukan Pilihan : ")

### Bab II ################
# Virus                   #
###########################

def bab2():

    # Mendefinisikan variable dan list untuk penyimpanan data yang diraih dari Input User. #

    historyUser = []
    scoreBenar = 0
    scoreSalah = 0
    nomor = 0

    ##
    mulaiTimer = time()

    # Menyatukan list, range dalam list pertanyaan menggunakan metode Zip, dan mendefinisikannya. #
    # List pertanyaan yang telah disatukan, kemudian di shuffle menggunakan module random. #

    # Metode Zip / Zip function digunakan untuk membentuk iterator berisi item dengan cara mendapatkan #
    # iterable (bisa satu atau lebih) yang kemudian digabungkan ke dalam tuple dan dikembalikan. #

    # Iterable berupa satu atau lebih iterator yang terdiri dari string, list tuple, dict dan lain lain. #

    order = list(range(len(pertanyaanBab2)))
    random.shuffle(order)

    os.system ('cls')
    print ("="*32)
    print ('|', "Bab II", "                      |")
    print ('|', "Virus", '                       |')
    print ("="*32)

    # Pemanggilan pertanyaan menggunakan fungsi For untuk melakukan perulangan dalam interval suatu list #

    for i in order:
        # Memberikan nilai pada nomor untuk setiap interval yang dikeluarkan, untuk mencetak nomor soal #
        # setiap perulangan dilakukan. #

        # Menggunakan huruf " f " sebelum tanda kutip agar dapat menulis {ekspresi}. #

        # [i] disini merujuk pada interval, sedangkan [0] ataupun [1] merujuk pada urutan suatu list. #
        nomor += 1
        print (f'\nPertanyaan {nomor}')
        print ('[?]', pertanyaanBab2[i][0])
        print (' ','\n  '.join(jawabanBab2[i]))

        # Menggunakan fungsi .upper() untuk merubah string dari Input User menjadi huruf kapital, #
        # sekaligus mencegah error yang di akibatkan oleh Input User menggunakan huruf kecil. #

        # Menyimpan jawaban user menggunakan .append dalam setiap bab agar dapat dicetak kembali. #

        jawabanUser = input('Jawab : ').upper()
        historyUser.append (jawabanUser)

        if jawabanUser == pertanyaanBab2[i][1]:
            print ('\n~ Jawaban tepat! ~')
            scoreBenar += 1
        else:
            print ('Jawaban yang tepat adalah', *pertanyaanBab2[i][1],'bukan', jawabanUser)
            scoreSalah += 1

    ##
    selesaiTimer = time()
    
    # Penjumlahan nilai User berdasarkan tepatnya jawaban yang di input. #
    # Dan, mencetak kembali seluruh data yang telah disimpan dalam variable maupun list. #

    nilai = scoreBenar * 10
    totalTimer = selesaiTimer - mulaiTimer

    print ('\n')
    print ('[!]','='*72,'[!]')
    print (' '*36, 'Hasil Quiz')
    print ('   ','='*72,'   ')
    print ('    Nama : ', *usrnme)
    print ('    NIS  : ', *usrnis)
    print ('    Berikut adalah hasil Quiz yang diraih oleh siswa dengan identitas diatas')
    print ('   ','-'*72,'   ')

    # Menggunakan fungsi .join untuk mengubah Array list menjadi string saat akan dicetak. #

    print ('    Waktu mengerjakan yang diraih : ', '%.2f'% totalTimer, 'Detik!')
    print ('    History Jawaban               : ', ' '.join(historyUser))
    print ('    Jawaban tepat yang diraih     : ', scoreBenar)
    print ('    Jawaban salah yang diraih     : ', scoreSalah)
    print ('    Nilai yang diraih             : ', nilai)

    print ("\n[?] -----------------------------[ Quiz Menu ]------------------------------ [?]")
    print ("  [1] Lanjutkan Bab (Bab III)      [2] Kembali ke Menu Bab       [3] Exit")

    mengulang = input("\nMasukan Pilihan : ")

    # Looping untuk mencegah error karena kesalahan Input User. #
    # Menggunakan fungsi break, agar mencegah terjadinya error berupa loop yang terus berulang. #

    while True:
        if mengulang == "1":
            bab3()
            break
        elif mengulang == "2":
            quizMenu()
            break
        elif mengulang == "3":
            exit
            break
        
        print ("\nTidak ada pilihan yang sesuai! Silahkan pilih kembali,")
        mengulang = input("Masukan Pilihan : ")

### Bab III ###############
# Bakteri                 #
###########################

def bab3():

    # Mendefinisikan variable dan list untuk penyimpanan data yang diraih dari Input User. #

    historyUser = []
    scoreBenar = 0
    scoreSalah = 0
    nomor = 0

    ##
    mulaiTimer = time()

    # Menyatukan list, range dalam list pertanyaan menggunakan metode Zip, dan mendefinisikannya. #
    # List pertanyaan yang telah disatukan, kemudian di shuffle menggunakan module random. #

    # Metode Zip / Zip function digunakan untuk membentuk iterator berisi item dengan cara mendapatkan #
    # iterable (bisa satu atau lebih) yang kemudian digabungkan ke dalam tuple dan dikembalikan. #

    # Iterable berupa satu atau lebih iterator yang terdiri dari string, list tuple, dict dan lain lain. #

    order = list(range(len(pertanyaanBab3)))
    random.shuffle(order)

    os.system ('cls')
    print ("="*32)
    print ('|', "Bab III", "                      |")
    print ('|', "Bakteri", '                      |')
    print ("="*32)

    # Pemanggilan pertanyaan menggunakan fungsi For untuk melakukan perulangan dalam interval suatu list #

    for i in order:
        # Memberikan nilai pada nomor untuk setiap interval yang dikeluarkan, untuk mencetak nomor soal #
        # setiap perulangan dilakukan. #

        # Menggunakan huruf " f " sebelum tanda kutip agar dapat menulis {ekspresi}. #

        # [i] disini merujuk pada interval, sedangkan [0] ataupun [1] merujuk pada urutan suatu list. #
        nomor += 1
        print (f'\nPertanyaan {nomor}')
        print ('[?]', pertanyaanBab3[i][0])
        print (' ','\n  '.join(jawabanBab3[i]))

        # Menggunakan fungsi .upper() untuk merubah string dari Input User menjadi huruf kapital, #
        # sekaligus mencegah error yang di akibatkan oleh Input User menggunakan huruf kecil. #

        # Menyimpan jawaban user menggunakan .append dalam setiap bab agar dapat dicetak kembali. #

        jawabanUser = input('Jawab : ').upper()
        historyUser.append (jawabanUser)

        if jawabanUser == pertanyaanBab3[i][1]:
            print ('\n~ Jawaban tepat! ~')
            scoreBenar += 1
        else:
            print ('Jawaban yang tepat adalah', *pertanyaanBab3[i][1],'bukan', jawabanUser)
            scoreSalah += 1

    ##
    selesaiTimer = time()

    # Penjumlahan nilai User berdasarkan tepatnya jawaban yang di input. #
    # Dan, mencetak kembali seluruh data yang telah disimpan dalam variable maupun list. #

    nilai = scoreBenar * 10
    totalTimer = selesaiTimer - mulaiTimer

    print ('\n')
    print ('[!]','='*72,'[!]')
    print (' '*36, 'Hasil Quiz')
    print ('   ','='*72,'   ')
    print ('    Nama : ', *usrnme)
    print ('    NIS  : ', *usrnis)
    print ('    Berikut adalah hasil Quiz yang diraih oleh siswa dengan identitas diatas')
    print ('   ','-'*72,'   ')

    # Menggunakan fungsi .join untuk mengubah Array list menjadi string saat akan dicetak. #

    print ('    Waktu mengerjakan yang diraih : ', '%.2f'% totalTimer, 'Detik!')
    print ('    History Jawaban               : ', ' '.join(historyUser))
    print ('    Jawaban tepat yang diraih     : ', scoreBenar)
    print ('    Jawaban salah yang diraih     : ', scoreSalah)
    print ('    Nilai yang diraih             : ', nilai)

    print ("\n[?] -----------------------------[ Quiz Menu ]------------------------------ [?]")
    print ("  [1] Lanjutkan Bab (Bab IV)      [2] Kembali ke Menu Bab       [3] Exit")

    mengulang = input("\nMasukan Pilihan : ")

    # Looping untuk mencegah error karena kesalahan Input User. #
    # Menggunakan fungsi break, agar mencegah terjadinya error berupa loop yang terus berulang. #

    while True:
        if mengulang == "1":
            bab4()
            break
        elif mengulang == "2":
            quizMenu()
            break
        elif mengulang == "3":
            exit
            break
        
        print ("\nTidak ada pilihan yang sesuai! Silahkan pilih kembali,")
        mengulang = input("Masukan Pilihan : ")

### Bab IV ################
# Protista                #
###########################

def bab4():

    # Mendefinisikan variable dan list untuk penyimpanan data yang diraih dari Input User. #

    historyUser = []
    scoreBenar = 0
    scoreSalah = 0
    nomor = 0

    ##
    mulaiTimer = time()

    # Menyatukan list, range dalam list pertanyaan menggunakan metode Zip, dan mendefinisikannya. #
    # List pertanyaan yang telah disatukan, kemudian di shuffle menggunakan module random. #

    # Metode Zip / Zip function digunakan untuk membentuk iterator berisi item dengan cara mendapatkan #
    # iterable (bisa satu atau lebih) yang kemudian digabungkan ke dalam tuple dan dikembalikan. #

    # Iterable berupa satu atau lebih iterator yang terdiri dari string, list tuple, dict dan lain lain. #

    order = list(range(len(pertanyaanBab4)))
    random.shuffle(order)

    os.system ('cls')
    print ("="*32)
    print ('|', "Bab IV", "                      |")
    print ('|', "Protista", '                    |')
    print ("="*32)

    # Pemanggilan pertanyaan menggunakan fungsi For untuk melakukan perulangan dalam interval suatu list #

    for i in order:
        # Memberikan nilai pada nomor untuk setiap interval yang dikeluarkan, untuk mencetak nomor soal #
        # setiap perulangan dilakukan. #

        # Menggunakan huruf " f " sebelum tanda kutip agar dapat menulis {ekspresi}. #

        # [i] disini merujuk pada interval, sedangkan [0] ataupun [1] merujuk pada urutan suatu list. #
        nomor += 1
        print (f'\nPertanyaan {nomor}')
        print ('[?]', pertanyaanBab4[i][0])
        print (' ','\n  '.join(jawabanBab4[i]))

        # Menggunakan fungsi .upper() untuk merubah string dari Input User menjadi huruf kapital, #
        # sekaligus mencegah error yang di akibatkan oleh Input User menggunakan huruf kecil. #

        # Menyimpan jawaban user menggunakan .append dalam setiap bab agar dapat dicetak kembali. #

        jawabanUser = input('Jawab : ').upper()
        historyUser.append (jawabanUser)

        if jawabanUser == pertanyaanBab4[i][1]:
            print ('\n~ Jawaban tepat! ~')
            scoreBenar += 1
        else:
            print ('Jawaban yang tepat adalah', *pertanyaanBab4[i][1],'bukan', jawabanUser)
            scoreSalah += 1

    ##
    selesaiTimer = time()

    # Penjumlahan nilai User berdasarkan tepatnya jawaban yang di input. #
    # Dan, mencetak kembali seluruh data yang telah disimpan dalam variable maupun list. #

    nilai = scoreBenar * 10
    totalTimer = selesaiTimer - mulaiTimer

    print ('\n')
    print ('[!]','='*72,'[!]')
    print (' '*36, 'Hasil Quiz')
    print ('   ','='*72,'   ')
    print ('    Nama : ', *usrnme)
    print ('    NIS  : ', *usrnis)
    print ('    Berikut adalah hasil Quiz yang diraih oleh siswa dengan identitas diatas')
    print ('   ','-'*72,'   ')

    # Menggunakan fungsi .join untuk mengubah Array list menjadi string saat akan dicetak. #

    print ('    Waktu mengerjakan yang diraih : ', '%.2f'% totalTimer, 'Detik!')
    print ('    History Jawaban               : ', ' '.join(historyUser))
    print ('    Jawaban tepat yang diraih     : ', scoreBenar)
    print ('    Jawaban salah yang diraih     : ', scoreSalah)
    print ('    Nilai yang diraih             : ', nilai)

    print ("\n[?] -----------------------------[ Quiz Menu ]------------------------------ [?]")
    print ("  [1] Lanjutkan Bab (Bab V)      [2] Kembali ke Menu Bab       [3] Exit")

    mengulang = input("\nMasukan Pilihan : ")

    # Looping untuk mencegah error karena kesalahan Input User. #
    # Menggunakan fungsi break, agar mencegah terjadinya error berupa loop yang terus berulang. #

    while True:
        if mengulang == "1":
            bab5()
            break
        elif mengulang == "2":
            quizMenu()
            break
        elif mengulang == "3":
            exit
            break

        print ("\nTidak ada pilihan yang sesuai! Silahkan pilih kembali,")
        mengulang = input("Masukan Pilihan : ")

### Bab V #################
# Fungi                   #
###########################

def bab5():

    # Mendefinisikan variable dan list untuk penyimpanan data yang diraih dari Input User. #

    historyUser = []
    scoreBenar = 0
    scoreSalah = 0
    nomor = 0

    ##
    mulaiTimer = time()

    # Menyatukan list, range dalam list pertanyaan menggunakan metode Zip, dan mendefinisikannya. #
    # List pertanyaan yang telah disatukan, kemudian di shuffle menggunakan module random. #

    # Metode Zip / Zip function digunakan untuk membentuk iterator berisi item dengan cara mendapatkan #
    # iterable (bisa satu atau lebih) yang kemudian digabungkan ke dalam tuple dan dikembalikan. #

    # Iterable berupa satu atau lebih iterator yang terdiri dari string, list tuple, dict dan lain lain. #

    order = list(range(len(pertanyaanBab5)))
    random.shuffle(order)

    os.system ('cls')
    print ("="*32)
    print ('|', "Bab V", "                      |")
    print ('|', "Fungi", '                      |')
    print ("="*32)

    # Pemanggilan pertanyaan menggunakan fungsi For untuk melakukan perulangan dalam interval suatu list #

    for i in order:
        # Memberikan nilai pada nomor untuk setiap interval yang dikeluarkan, untuk mencetak nomor soal #
        # setiap perulangan dilakukan. #

        # Menggunakan huruf " f " sebelum tanda kutip agar dapat menulis {ekspresi}. #

        # [i] disini merujuk pada interval, sedangkan [0] ataupun [1] merujuk pada urutan suatu list. #
        nomor += 1
        print (f'\nPertanyaan {nomor}')
        print ('[?]', pertanyaanBab5[i][0])
        print (' ','\n  '.join(jawabanBab5[i]))

        # Menggunakan fungsi .upper() untuk merubah string dari Input User menjadi huruf kapital, #
        # sekaligus mencegah error yang di akibatkan oleh Input User menggunakan huruf kecil. #

        # Menyimpan jawaban user menggunakan .append dalam setiap bab agar dapat dicetak kembali. #

        jawabanUser = input('Jawab : ').upper()
        historyUser.append (jawabanUser)

        if jawabanUser == pertanyaanBab5[i][1]:
            print ('\n~ Jawaban tepat! ~')
            scoreBenar += 1
        else:
            print ('Jawaban yang tepat adalah', *pertanyaanBab5[i][1],'bukan', jawabanUser)
            scoreSalah += 1

    ##
    selesaiTimer = time()

    # Penjumlahan nilai User berdasarkan tepatnya jawaban yang di input. #
    # Dan, mencetak kembali seluruh data yang telah disimpan dalam variable maupun list. #

    nilai = scoreBenar * 10
    totalTimer = selesaiTimer - mulaiTimer

    print ('\n')
    print ('[!]','='*72,'[!]')
    print (' '*36, 'Hasil Quiz')
    print ('   ','='*72,'   ')
    print ('    Nama : ', *usrnme)
    print ('    NIS  : ', *usrnis)
    print ('    Berikut adalah hasil Quiz yang diraih oleh siswa dengan identitas diatas')
    print ('   ','-'*72,'   ')

    # Menggunakan fungsi .join untuk mengubah Array list menjadi string saat akan dicetak. #

    print ('    Waktu mengerjakan yang diraih : ', '%.2f'% totalTimer, 'Detik!')
    print ('    History Jawaban               : ', ' '.join(historyUser))
    print ('    Jawaban tepat yang diraih     : ', scoreBenar)
    print ('    Jawaban salah yang diraih     : ', scoreSalah)
    print ('    Nilai yang diraih             : ', nilai)

    print ("\n[?] -----------------------------[ Quiz Menu ]------------------------------ [?]")
    print ("  [1] Lanjutkan Bab (Bab I)      [2] Kembali ke Menu Bab       [3] Exit")

    mengulang = input("\nMasukan Pilihan : ")

    # Looping untuk mencegah error karena kesalahan Input User. #
    # Menggunakan fungsi break, agar mencegah terjadinya error berupa loop yang terus berulang. #

    while True:
        if mengulang == "1":
            bab1()
            break
        elif mengulang == "2":
            quizMenu()
            break
        elif mengulang == "3":
            exit
            break
        
        print ("\nTidak ada pilihan yang sesuai! Silahkan pilih kembali,")
        mengulang = input("Masukan Pilihan : ")

# List Pertanyaan #

    # Untuk seluruh Bab berisi pertanyaan menggunakan tipe data Tuple, yang berfungsi agar #
    # selain data tidak dapat diubah (immutable) Tuple cenderung lebih cepat dalam mengolah data, #
    # tidak seperti List. #

pertanyaanBab1 = [
    ('Kumpulan dari individu satu jenis disebut...', 'A'),
    ('Upaya yang dilakukan makhluk hidup untuk menyesuaikan diri dengan lingkungannya disebut...', 'B'),
    ('Putra sedang mengelompokkan tumbuhan berdasarkan persamaan dan perbedaannya, untuk memudahkan Putra harus menguasai cabang ilmu...', 'D'),
    ('Dibawah ini yang bukan manfaat biologi dibidang pertanian adalah...', 'C'),
    ('Kelainan pada mata seperti rabun senja merupakan salah satu permasalahan biologi pada tingkat...', 'A'),
    ('Ciri berikut yang menentukan bahwa suatu benda termasuk makhluk hidup adalah....', 'A'),
    ('Flu burung dan influenza merupakan jenis penyakit yang dapat menyerang manusia. Penyebab kedua penyakit tersebut dipelajari dalam cabang ilmu biologi, yaitu....', 'A'),
    ('Struktur organisasi makhluk hidup berikut yang paling kompleks adalah....', 'C'),
    ('Variabel yang dibuat berbeda dalam percobaan dinamakan....', 'A'),
    ('Keterampilan membaca skala pada mistar merupakan keterampilan ....', 'D')
]

jawabanBab1 = [
    ('A. Populasi', 'B. Komunitas', 'C. Ekosistem', 'D. Bioma'),
    ('A. Evolusi', 'B. Adaptasi', 'C. Revolusi', 'D. Sekresi'),
    ('A. Entomologi', 'B. Ornitologi', 'C. Virologi', 'D. Taksonomi'),
    ('A. Hibridisasi', 'B. Kultur Jaringan', 'C. PEnemuan Pestisida Sintetis', 'D. Rekayasa Genetika'),
    ('A. Organ', 'B. Populasi', 'C. Sel', 'D. Jaringan'),
    ('A. Memiliki bahan genetik', 'B. Mampu pindah tempat','C. Memiliki mitokondria', 'D. Memiliki bentuk'),
    ('A. Virologi', 'B. Mikologi', 'C. Ornitologi', 'D. Orkidologi'),
    ('A. Komunitas', 'B. Ekosistem', 'C. Biosfer', 'D. Bioma'),
    ('A. Variabel bebas', 'B. Variabel terikat', 'C. Variabel terkontrol', 'D. Variabel pengganggu'),
    ('A. Inferensiasi','B. Pengamatan', 'C. Prediksi', 'D. Mengukur')
]

pertanyaanBab2 = [
    ('Berikut ini alat yang bisa dipergunakan untuk melihat wujud virus.....', 'D'),
    ('Yang dimaksud dengan inang virus adalah....', 'A'),
    ('Virus berdasarkan asam nukleatnya dibedakan menjadi....', 'D'),
    ('Tobbaco mosaic virus memiliki bentuk....', 'C'),
    ('Salah satu ciri virus sebagai makhluk hidup adalah....', 'B'),
    ('Ketika virus berada diluar tubuh inangnya maka virus akan....', 'D'),
    ('Tubuh virus dominan disusun atas senyawa organik yaitu....', 'C'),
    ('Istilah Virus pertama kali dikenalkan oleh Ilmuan....', 'D'),
    ('Virus berasal dari bahasa latin Virion yang berarti....', 'B'),
    ('Salah satu ciri virus bukan merupakan makhluk hidup adalah....', 'A')
]

jawabanBab2 = [
    ('A. Mikroskop', 'B. Jangka sorong', 'C. Mikrometer', 'D. Mikroskop elektron'),
    ('A. Makhluk hidup yang ditumpangi virus', 'B. Makhluk mati yang dihindari virus', 'C. Benda asing yang ditangkap virus', 'D. Virus yang disusupi makhluk hidup lain'),
    ('A. Virus utuh dan kapsid', 'B. Virion dan kapsid', 'C. Virus DNA dan kapsid', 'D. Virus RNA dan virus DNA'),
    ('A. Amplop', 'B. Tak beraturan', 'C. Heliks', 'D. Kompleks'),
    ('A. Virus mirip dengan sel','B. Memiliki materi genetik', 'C. Dapat mengkristal', 'D. Menyebabkan penyakit'),
    ('A. Mati', 'B. Bereproduksi', 'C. Menginfeksi', 'D. Mengkristal'),
    ('A. Karbohidrat', 'B. Lemak', 'C. Protein', 'D. Mineral'),
    ('A. Adolf Mayer', 'B. Martinus Beijerinck', 'C. Dmitri Ivanovsky', 'D. Wendell Stanley'),
    ('A. Kamar', 'B. Racun', 'C. Unit terkecil', 'D. Makhluk hidup'),
    ('A. Dapat dikristalkan', 'B. Dapat bereproduksi', 'C. Memiliki DNA', 'D. Memiliki RNA')
]

pertanyaanBab3 = [
    ('Tubuh bakteri disusun oleh sel yang bersifat prokariotik, artinya ....', 'C'),
    ('Dinding sel bakteri tersusun atas persenyawaan antara polisarida dan protein. Persenyawaan tersebut dikenal dengan....', 'D'),
    ('Morfologi bakteri berbentuk bola berkoloni disebut ....', 'C'),
    ('Bakteri yang menguntungkan bagi kita yang dinamakan Acetobacter xylinum berperan dalam pembuatan ....', 'A'),
    ('Bakteri dapat melakukan reproduksi secara seksual dengan cara ....', 'C'),
    ('Archaebacteria dan Eubacteria dibedakan berdasarkan ....', 'D'),
    ('Kelompok bakteri ada yang tidak dapat menyusun zat makanannya sendiri tetapi dengan memanfaatkan organisme lain, bakteri yang demikian disebut...', 'B'),
    ('Bakteri yang dinding selnya mengandung lapisan peptidoglikan yang tipis sehingga menyerap warna merah dengan pewarnaan Gram. Bakteri yang dimaksud adalah kelompok ....', 'A'),
    ('Bakteri berikut yang menyebabkan kerusakan pada taman anggrek adalah....', 'C'),
    ('Dodol adalah salah satu makanan yang dapat bertahan lama. Cara pengawetan makanan dodol yaitu dengan....', 'B')
]

jawabanBab3 = [
    ('A. Selnya amat kecil dan transparan', 'B. Selnya tidak memiliki sitoplasma', 'C. Tidak memiliki selaput yang membungkus intinya', 'D. Tidak memiliki selaput yang membatasi sel'),
    ('A. Hemiselulosa', 'B. Pektin', 'C. Selulosa', 'D. Peptidoglikan'),
    ('A. Streptococcus', 'B. Streptobacillus', 'C. Stafilococcus', 'D. Sarsina'),
    ('A. Nata de coco', 'B. Antibiotik', 'C. Yoghurt', 'D. Asam cuka'),
    ('A. Membentuk spora', 'B. Pembelahan biner', 'C. Konjugasi', 'D. Fragmentasi'),
    ('A. Analisis molekuler', 'B. Alat gerak', 'C. Cara memperoleh makanan', 'D. Membran sel'),
    ('A. Autotrof', 'B. Heterotrof', 'C. Anaerob', 'D. Aerob Fakultatif'),
    ('A. Bakteri gram negatif', 'B. Bakteri gram positif', 'C. Bakteri aerob', 'D. Bakteri anerob'),
    ('A. Candidatus liberibacter asiaticus', 'B. Pseudomonas solanacearum', 'C. Pseudomonas cattleyae', 'D. Bacterium papaya'),
    ('A. Pengeringan', 'B. Pemberian gula', 'C. Pendinginan', 'D. Pasteurisasi')
]

pertanyaanBab4 = [
    ('Organisme yang termasuk ke dalam Kingdom Protista memiliki ciri....', 'A'),
    ('Terdapat ganggang yang uniseluler atau mahluk hidup yang terdiri dari satu sel tunggal yaitu....', 'B'),
    ('Warna air pada sebuah kolam terdapat perubahan warna menjadi dominasi warna hijau. Hal tersebut dapat disebabkan oleh alga berjenis....', 'A'),
    ('Pada saat praktikum seorang siswa mengamati spesies air yang diambil dari dasar kolam. Dari hasil pengamatan siswa menyimpulkan bahwa mikroorganisme yang diamati berasal dari kelompok protista mirip hewan karena....', 'A'),
    ('Kelompok protozoa yang digunakan sebagai indikator/penunjuk sumber minyak bumi dan penentu umur relatif batuan sedimen laut adalah....', 'B'),
    ('Salah satu ciri ganggang hijau yang membedakan dengan ganggang yang lain adalah....', 'C'),
    ('Kelompok oomycota yang sering merugikan karena dapat merusak tanaman kentang dan tembakau yaitu....', 'A'),
    ('Pseudopodia yang terdapat pada amoeba berfungsi untuk....', 'B'),
    ('Protista memiliki sel yang bersifat....', 'C'),
    ('Di dalam ekosistem air laut/ air tawar dalam hubungannya dengan organisme lain, ganggang berkedudukan sebagai ....', 'D')
]

jawabanBab4 = [
    ('A. Uniseluler, eukariotik', 'B. Uniseluler atau multiseluler, prokariotik', 'C. Uniseluler,prokariotik, hidup sebagai parasit', 'D. Uniseluler, prokariotik dan anaerob'),
    ('A. Gonium', 'B. Euglena virdis', 'C. Chara fragilis', 'D. Ciliata'),
    ('A. Chlorophyta', 'B. Phaeophyta', 'C. Myxomycota ', 'D. Rhodophyta'),
    ('A. Memiliki alat gerak', 'B. Berklorofil', 'C. Prokariot', 'D. Multiseluler'),
    ('A. Amoeba', 'B. Foraminifera', 'C. Plamodium vivax', 'D. Radiozoa'),
    ('A. Mampu berfotosintesis', 'B. Berkembang biak dengan konjugasi', 'C. Memiliki pigmen dominan berupa klorofil', 'D. Memiliki pirenoid untuk menyimpan amilum'),
    ('A. Phytopthora infestanae', 'B. Saprolegnia', 'C. Saprolegnia australis', 'D. Pythium'),
    ('A. Membentuk vakuola makanan', 'B. Berpindah tempat', 'C. Menghindari bahan berbahaya', 'D. Menangkap mangsa'),
    ('A. Ganda', 'B. Prokariotik', 'C. eEkariotik', 'D. Tunggal'),
    ('A. Konsumen tingkat I', 'B. Konsumen tingkat II', 'C. Konsumen tingkat III', 'D. Produsen')
]

pertanyaanBab5 = [
    ('Kingdom fungi dapat dibedakan menjdai empat divisi, yaitu....', 'A'),
    ('Fungi hidup secara....', 'C'),
    ('Untuk pembuatan tempe dari kedelai dibutuhkan jamur/fungi dari divisi....', 'D'),
    ('Fungi dapat berkembang biak secara aseksual dengan membentuk....', 'A'),
    ('Salah satu cara hidup fungi yang memperoleh zat organik dari makhluk hidup yang menjadi inangnya adalah....', 'D'),
    ('Nama lain dari deuteromycotina yaitu jamur....', 'B'),
    ('Kalau kita mengkonsumsi jamur merang atau jamur kuping, sebenarnya yang kita makan adalah....', 'B'),
    ('Di bawah ini yang bukan peran jamur/fungi adalah....', 'C'),
    ('Fungi imperfekti merupakan fungi divisi....', 'D'),
    ('Kumpulan benang-benang halus pada jamur/ fungi disebut....', 'C')
]

jawabanBab5 = [
    ('A. Zygomycota, Ascomycota, Basidiomycota, dan Deuteromycota', 'B. Zygomycota, Ascomycota, Basidiomycota dan Antrophoda', 'C. Zygomycota, Ascomycota, Basidiomycota, dan Nepathelminthes', 'D. Zygomycota, Ascomycota, Basidiomycota, dan Oomycota'),
    ('A. Autotrof', 'B. Kematotrof', 'C. Heterotrof', 'D. Fotoautotrof'),
    ('A. Oomycota', 'B. Ascomycota', 'C. Basidiomycota', 'D. Zygomycota'),
    ('A. Konidium', 'B. Sporangium', 'C. Gemma', 'D. Sorus'),
    ('A. Saprofit', 'B. Mikrozoa', 'C. Mutasi', 'D. Parasit'),
    ('A. Tiram merah', 'B. Tidak sempurna', 'C. Lendir', 'D. Tiram Putih'),
    ('A. Askokarp', 'B. Badan buah (basidiokarp)', 'C. Kumpulan sporangium', 'D. Mikoriza'),
    ('A. Dibuat obat', 'B. Penambah rasa atau aroma', 'C. Indikator pencemaran air', 'D. Tumbuhan perintis'),
    ('A. Ascomycota', 'B. Zygomycota', 'C. Basidiomycota', 'D. Deuteromycota'),
    ('A. Sporangium', 'B. Askospora', 'C. Miselium', 'D. Basidiospora')
]

os.system('cls')
biodataUser()
