from spotfyv1 import *
import time
import pyglet
print("""
----------------------------------------------------------------------
                 Spotfy Kullanıcı Arayüzüne Hoşgeldiniz
Arayüzümüzün Yapabildikleri:
        1-Şarkı Ekle
        2-Şarkıları Göster
        3-Şarkıları Sorgula
        4-Şarkı Sil
------------------------------------------------------------------------
Şarkılar ve Sözleri:
        5-Determinete
        6-Rise
        7-Sick Mode
        8-Legends Never Die
        9-Phoneix
        
        Uygulamadan Çıkış Yapmak İçin 'q' ya Basınız
                                    İyi Dinlemeler Dİleriz
------------------------------------------------------------------------
""")

sözler=sözler()
spotfy=Spotfy()

while True:

    giriş=input("İşlem seçiniz:")
    if(giriş=="q"):
        print("Çıkış Yapılıyor.....")
        break
    elif(giriş=="1"):
        isim=input("İsim giriniz:")
        sanatcı=input("Sanatçı giriniz:")
        albüm=input("Albüm giriniz:")
        şirket=input("Şirket Giriniz:")
        süre=input("Süre giriniz:")
        yeni_müzik=müziklerim(isim,sanatcı,albüm,şirket,süre)
        spotfy.müzik_ekle(yeni_müzik)

    elif (giriş == "2"):
        spotfy.müzikleri_göster()

    elif (giriş == "3"):
        isim=input("Hangi müziği istiyorsunuz:")
        print("Müzik Sorgulanıyor.....")
        time.sleep(3)
        spotfy.müzik_sorgula(isim)

    elif (giriş == "4"):
        isim=input("Hangi kitabı silmek istiyorsunuz:")
        cevap=input("Eminmisiniz:E/H")
        if(cevap=="E"):
            print("Müzik siliniyor...")
            spotfy.müzik_sil(isim)

    elif(giriş=="5"):
        sözler.sözlerim()
        music = pyglet.resource.media('limonata.mp3')
        music.play()
        pyglet.app.run()

    elif (giriş == "6"):
        sözler.rise()
        music = pyglet.resource.media('rise.mp3')
        music.play()
        pyglet.app.run()

    elif (giriş == "7"):
        sözler.mode()
        music = pyglet.resource.media('mode.mp3')
        music.play()
        pyglet.app.run()

    elif (giriş == "8"):
        sözler.never()
        music = pyglet.resource.media('never.mp3')
        music.play()
        pyglet.app.run()

    elif (giriş == "9"):
        sözler.anka()
        music = pyglet.resource.media('anka.mp3')
        music.play()
        pyglet.app.run()


    else:
        print("geçersiz işlem")










