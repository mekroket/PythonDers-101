import time
import _sqlite3
class Spotfy2():
    def __init__(self):
        self.baglantı_olustur()

    def baglantı_olustur(self):
        self.baglantı= _sqlite3.connect("spotfy2.db")
        self.cursor=self.baglantı.cursor()
        sorgu="Create Table If not exists spotfy2(Müzikler BLOB)"
        self.cursor.execute(sorgu)
        self.baglantı.commit()


    def müzik_ekle(self,müzik):
        sorgu="Insert into spotfy2 Values(?)"
        self.cursor.execute(sorgu,(müzik,))
        self.baglantı.commit()
        self.cursor.close()

spotfy2=Spotfy2()

giriş=input("giriş yap:")


spotfy2.müzik_ekle(giriş)

import pyglet
music = pyglet.resource.media("C:/Users/oguz9/Desktop/Sqlite Databese/limonata.mp3")
music.play()
pyglet.app.run()

