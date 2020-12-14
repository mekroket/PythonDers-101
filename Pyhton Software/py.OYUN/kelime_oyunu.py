print("""
***************************************************************************************************
*
*                            -KELİME OYUNUNA HOŞGELDİNİZ-
*   Oyunumuz Nasıl Oynanır:
*            Oyunumuza başlamak için 'Başla' yazınız. Yanlış girdiğiniz halde oyun kapatılacaktır.
*
*            Sorulan soruların sadece 1 cevabı vardır o yüzden cevaplarınızı iyi düşününüz.
*
*            Verdiğimiz anahtar kelimelerle bizim sizden istediğimiz kelimeyi bulmaya çalışınız.
*            
*            Oyunda kelimeleri bulmanız için belirli bir hakkınız vardır.
*            
*            Genel oyundaki kelime bulma hakkınız 5'tür.
*
*            2. Bölümde her ipucu alındığında hakkınızdan -1 gidecektir.
*            
*            Oyundan çıkış yapmak isterseniz 'q' ya basarak çıkabilirsiniz.
*            
*            Kelimelerimiz güncel hayattan olup rastgele seçilmiştir ayrıca;
*           sizi zorlayacak herhangi bir kelime gelirse araştırıp anlamına bakabilirsiniz.    
*
*                                                                    @Powered By OguzKaanEkin v1.3
*                                                      
******************************************************************************************************
""")
#veritabanı
kelime1='klavye'
kelime2='lamba'
kelime3='masa'
kelime4='fare'
kelime5='elbise'
kelime6='araba farı'
kelime7='futbol topu'
kelime8='voyegr'


hak=5

#modüller
import random
import time

#başlangıç
print('LÜTFEN OYUNA BAŞLAMADAN ÖNCE KURALLARI İYİ OKUYUNUZ')
başla=input('Oyunumuza Hoşgeldiniz Başlamak için Komudu Giriniz:')
if(başla=='q'):
    print('Çıkış Yapılıyor... Tekrar Bekleriz....')
    time.sleep(3)
    exit()

if(başla=='BAŞLA'):
    while (hak>= 0):
        print('Genelde bilgisayar ve telefondalarda yazı yazmak için kullanılan araçtır.')
        giriş1=input('Cevabınız:')
        if(giriş1=='klavye'):
            print('Tebrikler Doğru bildiniz')
            print('Sıradaki sorunuz geliyor....')
            time.sleep(3)
        else:
            print('Tekrar Deneyiniz...')
            hak-=1
            print('Kalan hakkkınız',hak)
            continue

            giriş1 = input('Cevap:')
            if (giriş1 == 'klavye'):
                print('Tebrikler Doğru bildiniz ')
                print('Sıradaki sorunuz geliyor....')
                time.sleep(3)
        if(hak=='0'):
            print('Hakkınız Kalmamıştır....')
            time.sleep(3)
            exit()
#############################################################################################
        while (hak >= 0):
            print('Edison tarafından bulunan heryerde aydınlatma için kullanılan araçtır.')
            cevap=input('Cevap Giriniz:')
            if(cevap=='ampul'):
                print('Tebrikler Doğru bildiniz ')
                print('Sıradaki sorunuz geliyor....')
                time.sleep(3)
            else:
                print('Tekrar Deneyiniz...')
                hak-=1
                print('Kalan hakkkınız', hak)
                continue

                cevap = input('Cevap:')
                if (cevap ==  'ampul'):
                    print('Tebrikler Doğru bildiniz ')
                    print('Sıradaki sorunuz geliyor....')
                    time.sleep(3)
            if (hak == '0'):
                print('Hakkınız Kalmamıştır....')
                time.sleep(3)
                exit()

#############################################################################################
            while (hak >= 0):
                print('Eşyalarımız ve genelikle bilgisayar ve üzerinde ders çalıştığımız eşya.')
                cevap1=input('Cevap Giriniz:')
                if(cevap1=='masa'):
                    print('Tebrikler Doğru bildiniz ')
                    print('Sıradaki sorunuz geliyor....')
                    time.sleep(3)
                else:
                    print('Tekrar Deneyiniz...')
                    hak-=1
                    print('Kalan hakkınız',hak)

                    cevap1 = input('Cevap:')
                    if (cevap1 == 'masa'):
                        print('Tebrikler Doğru bildiniz ')
                        print('Sıradaki sorunuz geliyor....')
                        time.sleep(3)

                if (hak == '0'):
                    print('Hakkınız Kalmamıştır....')
                    time.sleep(3)
                    exit()
##################################################################################################
                while (hak >= 0):
                    print('Bilgisayarda imleci hareket ettirmemizi sağlayan eşya.')
                    cevap2 = input('Cevap Giriniz:')
                    if (cevap2 == 'mause'):
                        print('Tebrikler Doğru bildiniz ')
                        print('Sıradaki sorunuz geliyor....')
                        time.sleep(3)
                    else:
                        print('Tekrar Deneyiniz...')
                        hak -= 1
                        print('Kalan hakkınız', hak)

                        cevap2 = input('Cevap:')
                        if (cevap2 == 'mause'):
                            print('Tebrikler Doğru bildiniz ')
                            print('Sıradaki sorunuz geliyor....')
                            time.sleep(3)

                    if (hak == '0'):
                        print('Hakkınız Kalmamıştır....')
                        time.sleep(3)
                        exit()


#############################################################################################
                    while (hak >= 0):
                        print('İnsanların yaşamında üstüne giydikleri eşya.')
                        cevap3 = input('Cevap Giriniz:')
                        if (cevap3 == 'kıyafet'):
                            print('Tebrikler Doğru bildiniz ')
                            print('Sıradaki sorunuz geliyor....')
                            time.sleep(3)
                        else:
                            print('Tekrar Deneyiniz...')
                            hak -= 1
                            print('Kalan hakkınız', hak)


                            cevap3 = input('Cevap:')
                            if (cevap3 == 'kıyafet'):
                                print('Tebrikler Doğru bildiniz ')
                                print('Sıradaki sorunuz geliyor....')
                                time.sleep(3)

                        if (hak == '0'):
                            print('Hakkınız Kalmamıştır....')
                            time.sleep(3)
                            exit()
#################################################################ikinci aşama
                        print('Bu zamana kadar 1.aşamayı geçtiniz tebrikler')
                        time.sleep(2)
                        print('Şimdi ise 2. aşamaya geçme zamanı...')
                        time.sleep(3)
                        print('2.Aşamada size artık anahtar açıklama verilmiycek kelimeler random olarak verilip sizden bulmanızı isticez')
                        time.sleep(4)
                        print('İlk kelime geliyor hazırmısınız ?')
                        time.sleep(3)
#######################################################################################

                        while (hak >= 0):
                            list1 = ['a','f','r']
                            print(list1)
                            cevap4=input('Cevap:')
                            if(cevap4=='far'):
                                print('Tebrikler Doğru bildiniz ')
                                print('Sıradaki sorunuz geliyor....')
                                time.sleep(3)

                            elif(cevap4=='ipucu'):
                                print('İpucu geliyor....')
                                print('Taşıtlarda aydınlatmaya yarayan cisim')
                                time.sleep(2)
                                hak-=1

                                cevapa=input('Cevap:')
                                if(cevapa == 'far'):
                                    print('Tebrikler Doğru bildiniz ')
                                    print('Sıradaki sorunuz geliyor....')
                                    time.sleep(3)
                            else:
                                print('Tekrar Deneyiniz...')
                                hak -= 1
                                print('Kalan hakkınız', hak)

                                cevapb = input('Cevap:')
                                if (cevapb == 'far'):
                                    print('Tebrikler Doğru bildiniz ')
                                    print('Sıradaki sorunuz geliyor....')
                                    time.sleep(3)

                                elif (cevapb == 'ipucu'):
                                    print('İpucu geliyor....')
                                    print('Taşıtlarda aydınlatmaya yarayan cisim')
                                    time.sleep(2)
                                    hak -= 1

                                    cevap_ = input('Cevap:')
                                    if (cevap_== 'far'):
                                        print('Tebrikler Doğru bildiniz ')
                                        print('Sıradaki sorunuz geliyor....')
                                        time.sleep(3)

                            if (hak == '0'):
                                print('Hakkınız Kalmamıştır....')
                                time.sleep(3)
                                exit()
#############################################################################################
                            while (hak >= 0):
                                list2 = ['f','o','u','b','p','l','t','t','o','u']
                                print(list2)
                                cevap5 = input('Cevap:')
                                if (cevap5 == 'futbol topu'):
                                    print('Tebrikler Doğru bildiniz ')
                                    print('Sıradaki sorunuz geliyor....')
                                    time.sleep(3)

                                elif (cevap5 == 'ipucu'):
                                    print('İpucu geliyor....')
                                    print('Dünyada en çok oynanan ve izlenen oyundaki bir cisim.')
                                    time.sleep(2)
                                    hak -= 1

                                    cevapg = input('Cevap:')
                                    if (cevapg == 'futbol topu'):
                                        print('Tebrikler Doğru bildiniz ')
                                        print('Sıradaki sorunuz geliyor....')
                                        time.sleep(3)

                                else:
                                    print('Tekrar Deneyiniz...')
                                    hak -= 1
                                    print('Kalan hakkınız', hak)

                                    cevapl = input('Cevap:')
                                    if (cevapl == 'futbol topu'):
                                        print('Tebrikler Doğru bildiniz ')
                                        print('Sıradaki sorunuz geliyor....')
                                        time.sleep(3)

                                    elif (cevapl == 'ipucu'):
                                        print('İpucu geliyor....')
                                        print('Taşıtlarda aydınlatmaya yarayan cisim')
                                        time.sleep(2)
                                        hak -= 1

                                        cevapç = input('Cevap:')
                                        if (cevapç== 'futbol topu'):
                                            print('Tebrikler Doğru bildiniz ')
                                            print('Sıradaki sorunuz geliyor....')
                                            time.sleep(3)

                                if (hak == '0'):
                                    print('Hakkınız Kalmamıştır....')
                                    time.sleep(3)
                                    exit()
################################################################################################
                                while (hak >= 0):
                                    list3 = ['g','v','y','o','e','r']
                                    print(list3)
                                    cevap6 = input('Cevap:')
                                    if (cevap6 == 'voyegr'):
                                        print('Tebrikler Doğru bildiniz ')
                                        print('Sıradaki sorunuz geliyor....')
                                        time.sleep(3)

                                    elif(cevap6 == 'ipucu'):
                                        print('İpucu geliyor....')
                                        print('Uzaya gönderilen ve uzayda şuana kadar en uzağa giden uzay aracı. ')
                                        time.sleep(2)
                                        hak -= 1

                                        cevapı = input('Cevap:')
                                        if (cevapı == 'voyegr'):
                                            print('Tebrikler Doğru bildiniz ')
                                            time.sleep(3)
                                    else:
                                        print('Tekrar Deneyiniz...')
                                        hak -= 1
                                        print('Kalan hakkınız', hak)

                                        cevapv = input('Cevap:')
                                        if (cevapv == 'voyegr'):
                                            print('Tebrikler Doğru bildiniz ')
                                            print('Sıradaki sorunuz geliyor....')
                                            time.sleep(3)

                                        elif (cevapb == 'ipucu'):
                                            print('İpucu geliyor....')
                                            print('Taşıtlarda aydınlatmaya yarayan cisim')
                                            time.sleep(2)
                                            hak -= 1

                                            cevapp = input('Cevap:')
                                            if (cevapp == 'voyegr'):
                                                print('Tebrikler Doğru bildiniz ')
                                                time.sleep(3)

                                    print('TEBRİKLER OYUNUMUZU TAMAMLADINIZ....')
                                    time.sleep(2)
                                    print('ÇIKACAK OLAN YENİ OYUNLARIMIZDA GÖRÜŞMEK ÜZERE.....')
                                    exit()
                                    time.sleep(4)

















