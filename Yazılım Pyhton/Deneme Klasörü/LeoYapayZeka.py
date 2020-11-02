print("""
*******************************************************************************************
* Leo Sesli Asistana HOŞ GELDİNİZ
*       Komut listemiz:
*           hava durumu
*           saat kaç
*           bana fıkra anlat                                                                  
*           hesap makinesini aç
*           çıkış yapmak için 'q' ya bas                                                                              
*                                                    @Powered By Oguzkaan and Ramazanİlker  v1.1 
*                                                     Yeni Özellikler Yakında...                                                                                   
*******************************************************************************************
""")


from gTTS import gTTS
import os
import time
import datetime
import speech_recognition as sr

tts = gTTS(text=' leo sesli asistana hoşgeldin senin için ne yapabilirim ', lang='tr')
tts.save("hoşgeldiniz.mp3")
os.system("hoşgeldiniz.mp3")
time.sleep(3)
tts = gTTS(text=' Welcome to leo voice assistant what can ı do for you ', lang='en-US')
tts.save("tercüme.mp3")
os.system("tercüme.mp3")

while True:
    a=input('Merhaba,Nasıl yardımcı olabilirim:')
    if (a == 'q'):
        print('Çıkış yapılıyor...')
        tts = gTTS(text='Leo sesli asistandan çıkış yapılıyor istek ve önerileriniz için discord sunucumuzdan oguzkaan ile iletişime geçebilirsiniz ', lang='tr')
        tts.save("gün.mp3")
        os.system("gün.mp3")
        time.sleep(5)
        exit()
    if(a=='bana fıkra anlat'):
        tts = gTTS(text='Adamın biri elinde büyük bir bıçakla camiye dalar ve sorar: Aranızda Müslüman olan var mı Korkudan kimse bişey diyemez. Birazdan yaşlı bir adam ayağa kalkar Ben Müslümanım der. Bıçaklı adamla yaşlı adam camiden çıkarlar. Adam dışarıdaki inek sürüsünü gösterip: Amca, şunları kurban edicem de ben beceremem yardım eder misin der. Yaşlı adam epey bir hayvanı kestikten sonra Ben yoruldum başka birini bul der. Adam bu sefer kanlı bıçakla yine camiye girer ve sorar: Aranızda başka müslüman var mı? Az önceki adamı doğradığını düşünen cemaat çok korkar ve herkes aynı anda imama bakar, imam: Ne bakıyosunuz ulan iki rekât namaz kıldırdık diye hemen müslüman mı olduk?', lang='tr')
        tts.save("fıkra.mp3")
        os.system("fıkra.mp3")

    elif(a=='bugün günlerden hangi gün'):
        tts = gTTS(text='günler artık o kadar hızlı geçiyorki ben bile günleri bilemez oldum ', lang='tr')
        tts.save("gün.mp3")
        os.system("gün.mp3")

    elif(a=='hava durumu'):
        hava=input('Şehir giriniz:')
        tts = gTTS(text='Güneşle ve mevsim değerlerinin ortalamasında ', lang='tr')
        tts.save("hava.mp3")
        os.system("hava.mp3")
    elif(a=='saat kaç'):
        tts = gTTS(text='Saat:{} '.format(datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)), lang='tr')
        tts.save("saat.mp3")
        os.system("saat.mp3")
        datetime.datetime.now()
        datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
        print(datetime.datetime.now())
    elif(a=='hesap makinesini aç'):
        tts = gTTS(text='Hesap makinesini açıyorum: ', lang='tr')
        tts.save("hesap.mp3")
        os.system("hesap.mp3")
        print("""
        ***********************************************************************************************
                                             HESAP MAKİNESİ
        1.İŞLEM TOPLAMA
        2.İŞLEM ÇIKARMA
        3.İŞLEM ÇARPMA
        4.İŞLEM BÖLME
        ÇIKIŞ YAPMAK İÇİN 'Q'YA BASINIZ
        ***********************************************************************************************
        """)
        def toplama(sayı1, sayı2):
            return sayı1 + sayı2
        def çıkarma(sayı1, sayı2):
            return sayı1 - sayı2
        def çarpma(sayı1, sayı2):
            return sayı1 * sayı2
        def bölme(sayı1, sayı2):
            return sayı1 / sayı2
        while True:
            seçim = input('Seçim Yapınız:')
            sayı1 = int(input('1.sayıyı giriniz:'))
            sayı2 = int(input('2.sayıyı giriniz'))
            if (seçim == '1'):
                tts = gTTS(text='sonuç {}: '.format(toplama(sayı1, sayı2)), lang='tr')
                tts.save("hesapt.mp3")
                os.system("hesapt.mp3")
            elif (seçim == '2'):
                tts = gTTS(text='sonuç {}: '.format(çıkarma(sayı1, sayı2)), lang='tr')
                tts.save("hesapı.mp3")
                os.system("hesapı.mp3")
            elif (seçim == '3'):
                tts = gTTS(text='sonuç {}: '.format(çarpma(sayı1, sayı2)), lang='tr')
                tts.save("hesapç.mp3")
                os.system("hesapç.mp3")
            elif (seçim == '4'):
                tts = gTTS(text='sonuç {}: '.format(bölme(sayı1, sayı2)), lang='tr')
                tts.save("hesapb.mp3")
                os.system("hesapb.mp3")
            else:
                print('Lütfen geçerli bir değer giriniz..')
                exit()









