import _sqlite3
from time import sleep
import sys


class müziklerim():
    def __init__(self,isim,sanatcı,albüm,şirket,süre):
        self.isim=isim
        self.sanatcı=sanatcı
        self.albüm=albüm
        self.şirket=şirket
        self.süre=süre

    def __str__(self):
        return "İsim: {}\nSanatçı: {}\nAlbüm: {}\nŞirket: {}\nSüre: {}".format(self.isim,self.sanatcı,self.albüm,self.şirket,self.süre)

class Spotfy():
    def __init__(self):
        self.baglantı_olustur()

    def baglantı_olustur(self):
        self.baglantı=_sqlite3.connect("../spotfy.db")
        self.cursor=self.baglantı.cursor()
        sorgu="Create Table If not Exists spotfy (isim TEXT,sanatcı TEXT,Albüm TEXT,Şirket TEXT,Süre TEXT)"
        self.cursor.execute(sorgu)
        self.baglantı.commit()

    def baglantıyı_kes(self):
        self.baglantı.close()

    def müzik_ekle(self,müzik):
        sorgu="Insert into spotfy Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(müzik.isim,müzik.sanatcı,müzik.albüm,müzik.şirket,müzik.süre))
        self.baglantı.commit()

    def müzik_sorgula(self,isim):
        sorgu="Select * From spotfy where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        müzikler =self.cursor.fetchall()

        if(len(müzikler)==0):
            print("Kitaplığınızda Müzik Bulunmuyor......")
        else:
            müzik = Müzik(müzikler[0][0], müzikler[0][1], müzikler[0][2], müzikler[0][3], müzikler[0][4])
        print(müzik)

    def müzik_sil(self,isim):
        sorgu="Delete From spotfy where isim=?"
        self.cursor.execute(sorgu,(isim,))
        self.baglantı.commit()

    def müzikleri_göster(self):
        sorgu="Select*From spotfy"
        self.cursor.execute(sorgu)
        müzikler=self.cursor.fetchall()
        if(len(müzikler)==0):
            print("Kitaplığınızda Müzik Bulunmuyor....")
        else:
            for i in müzikler:
               müzik=müziklerim(i[0],i[1],[2],i[3],i[4])
               print(müzik)


class sözler():
    def sözlerim(self):
        with open("sözler.txt", "r", encoding="utf-8")as file:
            for i in file:
                print(i)

    def rise(self):
        with open("rise.txt", "r", encoding="utf-8")as file2:
            for i in file2:
                print(i)

    def mode(self):
        with open("mode.txt", "r", encoding="utf-8")as file3:
            for i in file3:
                print(i)

    def never(self):
        with open("never.txt", "r", encoding="utf-8")as file4:
            for i in file4:
                print(i)

    def anka(self):
        with open("anka.txt", "r", encoding="utf-8")as file5:
            for i in file5:
                print(i)




















