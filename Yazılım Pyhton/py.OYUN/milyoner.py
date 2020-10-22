print("""
                                Kim Milyoner Olmak İster Oyunumuza HOŞ GELDİNİZ
    Kurallar:                                                       
    Size sorulan 12 sorudan 6. soruya kadar süreniz olacaktır
    2 baraj sorunuz vardır ; 2. ve 7. sorular baraj sorularınızdır.
    6.soruya kadar 3 joker hakkınız olacaktır ve sonra yeni joker hakkınız gelicektir, joker haklarınız;
                                                1.Çoğunluk Oylaması(oylama istemek için oylama yazınız)
                                                2.Googldan bakma(bakma istemek için bakma)
                                                3.Yanlış şıkları silme(silme istemek için silme)
    ilk 2 soru 10, 6. soruya kadar sorulan soruların süresi 20 saniyedir.
            Puan Skalası:
                    
                    12   1.000.000TL
                    11     250.000TL
                    10     125.000TL
                    9       60.000TL
                    8       30.000TL
                    7       15.000TL
                    6        7.500TL
                    5        5.000TL
                    4        3.0000TL
                    2        2.0000TL
                    1           500TL
    Başarılar Dileriz...
                                                                                    @Powered By OguzKaanEkin v1.1
                                                                


""")
import time
import sys

oylama=1
bakma=1
silme=1

if(oylama<=0):
    print('Joker hakkınız kalmamıştır.....')

print('Oyunumuza Başlamadan Önce Lütfen Kuralları Okuyunuz...')
time.sleep(1)
print('Oyunumuz Başlıyor...........')
time.sleep(1)
print('Hazırsanız İlk Sorunuz geliyor.')

print('\nBir işin uygun ve kolay olduğunu belirtmek için hangisi söylenir?')
print('A:Burnuma göre    B:Kaşıma göre    C:Bıyığıma Göre    D:Dişime göre')
soru1=input('Cevabınız:')

for i in range(10 , 0 ,-1):
    time.sleep(1)
    sys.stdout.write(str(i) + ' ')
    sys.stdout.flush()

if(soru1=='d'):
    print('Tebrikler 500TL Kazanmaya Hak Kazandınız..')
    print('Sıradaki Sorunuz Geliyor...')

elif(soru1=='oylama'):
    print('Oylama Yapılıyor....')
    oylama-=1
    if (oylama <= 0):
        print('Joker hakkınız kalmamıştır.....')
    time.sleep(4)
    print('Oylama sonuçlarına göre D şıkkı çoğunluktadır.')

    cevap1 = input('Cevabınız:')
    if (cevap1 == 'd'):
        print('Tebrikler 500TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')
    else:
        print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
        time.sleep(4)
        exit()
elif(soru1=='bakma'):
    print('Googldan bakabilirsiniz...')
    if (bakma <= 0):
        print('Joker hakkınız kalmamıştır.....')
    bakma-=1
    cevap1 = input('Cevabınız:')
    if (cevap1 == 'd'):
        print('Tebrikler 500TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

elif(soru1=='silme'):
    print('Yanlış Şıklar siliniyor...')
    if (silme <= 0):
        print('Joker hakkınız kalmamıştır.....')
    silme-=1
    time.sleep(3)
    print('A:Burnuma göre      D:Dişime göre')
    cevap1 = input('Cevabınız:')
    if (cevap1 == 'd'):
        print('Tebrikler 500TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

else:
    print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
    time.sleep(4)
    exit()

###########################################################################################






print('Hazırsanız İkinci Sorunuz geliyor.')
time.sleep(2)
print('\nAtasözüne göre gönülden de ırak olan kimdir ?')
print('A:Arabası tamircide olan    B:Evi uzak olan    C:Gözden ırak olan    D:İş yeri karşıda olan')
soru2=input('Cevabınız:')

for i in range(10 , 0 ,-1):
    time.sleep(1)
    sys.stdout.write(str(i) + ' ')
    sys.stdout.flush()

if(soru2=='c'):
    print('Tebrikler 1000TL Kazanmaya Hak Kazandınız..')
    print('Sıradaki Sorunuz Geliyor...')

elif(soru2=='oylama'):
    print('Oylama Yapılıyor....')
    oylama-=1
    if (oylama <= 0):
        print('Joker hakkınız kalmamıştır.....')
    time.sleep(4)
    print('Oylama sonuçlarına göre c şıkkı çoğunluktadır.')

    cevap2 = input('Cevabınız:')
    if (cevap2 == 'c'):
        print('Tebrikler 1000tl Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')
    else:
        print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
        time.sleep(4)
        exit()
elif(soru2=='bakma'):
    print('Googledan bakabilirsiniz.')
    if (bakma <= 0):
        print('Joker hakkınız kalmamıştır.....')
    bakma-=1
    cevap2 = input('Cevabınız:')
    if (cevap1 == 'c'):
        print('Tebrikler 1000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

elif(soru2=='silme'):
    print('Yanlış Şıklar siliniyor...')
    if (silme <= 0):
        print('Joker hakkınız kalmamıştır.....')
    silme-=1
    time.sleep(3)
    print('B:Evi uzak olan    C:Gözden ırak olan')
    cevap2 = input('Cevabınız:')
    if (cevap2 == 'c'):
        print('Tebrikler 1000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

else:
    print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
    time.sleep(4)
    exit()

#############################################################################################





print('Hazırsanız Üçüncü Sorunuz geliyor.')
time.sleep(2)
print('\nHangisi bazı futbol takımlarının taraftarları için kullandıkları ifadedir ?')
print('A:12.adam    B:Yardımcı eleman    C:Canlı destek    D:Yedek kuvvet')
soru3=input('Cevabınız:')

for i in range(20 , 0 ,-1):
    time.sleep(1)
    sys.stdout.write(str(i) + ' ')
    sys.stdout.flush()

if(soru3=='a'):
    print('Tebrikler 2000TL Kazanmaya Hak Kazandınız..')
    print('Sıradaki Sorunuz Geliyor...')

elif(soru3=='oylama'):
    print('Oylama Yapılıyor....')
    oylama-=1
    if (oylama <= 0):
        print('Joker hakkınız kalmamıştır.....')
    time.sleep(4)
    print('Oylama sonuçlarına göre a şıkkı çoğunluktadır.')

    cevap3 = input('Cevabınız:')
    if (cevap3 == 'a'):
        print('Tebrikler 2000tl Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')
    else:
        print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
        time.sleep(4)
        exit()
elif(soru3=='bakma'):
    print('Googledan bakabilirsiniz.')
    if (bakma <= 0):
        print('Joker hakkınız kalmamıştır.....')
    bakma-=1
    cevap3 = input('Cevabınız:')
    if (cevap3 == 'a'):
        print('Tebrikler 2000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

elif(soru3=='silme'):
    print('Yanlış Şıklar siliniyor...')
    if (silme <= 0):
        print('Joker hakkınız kalmamıştır.....')
    silme-=1
    time.sleep(3)
    print('A:12.adam    B:Yardımcı eleman')
    cevap3 = input('Cevabınız:')
    if (cevap3 == 'a'):
        print('Tebrikler 2000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

else:
    print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
    time.sleep(4)
    exit()



######################################################################################3


print('Hazırsanız Dördüncü Sorunuz geliyor.')
time.sleep(2)
print('\nHorozu çok olan köyde- şeklindeki gibi başlayan atasözünün devamı nasıldır ?')
print('A:Sabah erken olur    B:Akşam geç olur    C:Akşam erken olur    D:Sabah geç olur')
soru4=input('Cevabınız:')

for i in range(20 , 0 ,-1):
    time.sleep(1)
    sys.stdout.write(str(i) + ' ')
    sys.stdout.flush()

if(soru4=='d'):
    print('Tebrikler 3000TL Kazanmaya Hak Kazandınız..')
    print('Sıradaki Sorunuz Geliyor...')

elif(soru4=='oylama'):
    print('Oylama Yapılıyor....')
    oylama-=1
    if (oylama <= 0):
        print('Joker hakkınız kalmamıştır.....')
    time.sleep(4)
    print('Oylama sonuçlarına göre d şıkkı çoğunluktadır.')

    cevap4 = input('Cevabınız:')
    if (cevap4 == 'd'):
        print('Tebrikler 3000tl Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')
    else:
        print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
        time.sleep(4)
        exit()
elif(soru4=='bakma'):
    print('Googledan bakabilirsiniz.')
    if (bakma <= 0):
        print('Joker hakkınız kalmamıştır.....')
    bakma-=1
    cevap4 = input('Cevabınız:')
    if (cevap4 == 'd'):
        print('Tebrikler 3000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

elif(soru4=='silme'):
    print('Yanlış Şıklar siliniyor...')
    if (silme <= 0):
        print('Joker hakkınız kalmamıştır.....')
    silme-=1
    time.sleep(3)
    print('B:Akşam geç olur   D:Sabah geç olur')
    cevap4 = input('Cevabınız:')
    if (cevap4 == 'd'):
        print('Tebrikler 3000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

else:
    print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
    time.sleep(4)
    exit()




################################################################################################


print('Hazırsanız Beşinci Sorunuz geliyor.')
time.sleep(2)
print('\nGövdesi sarı veya kirli sarı; yelesi,kuyruğu ve bacağının alt kısmındaki kılları koyu renkte olan atlar için kullanılan ifade hangisidir ?')
print('A:Doru    B:Kula    C:Yağız    D:Seki')
soru5=input('Cevabınız:')

for i in range(20 , 0 ,-1):
    time.sleep(1)
    sys.stdout.write(str(i) + ' ')
    sys.stdout.flush()

if(soru5=='b'):
    print('Tebrikler 5000TL Kazanmaya Hak Kazandınız..')
    print('Sıradaki Sorunuz Geliyor...')

elif(soru5=='oylama'):
    print('Oylama Yapılıyor....')
    oylama-=1
    if (oylama <= 0):
        print('Joker hakkınız kalmamıştır.....')
    time.sleep(4)
    print('Oylama sonuçlarına göre b şıkkı çoğunluktadır.')

    cevap5 = input('Cevabınız:')
    if (cevap5 == 'b'):
        print('Tebrikler 5000tl Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')
    else:
        print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
        time.sleep(4)
        exit()
elif(soru5=='bakma'):
    print('Googledan bakabilirsiniz.')
    if (bakma <= 0):
        print('Joker hakkınız kalmamıştır.....')
    bakma-=1
    cevap5 = input('Cevabınız:')
    if (cevap5 == 'b'):
        print('Tebrikler 5000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

elif(soru5=='silme'):
    print('Yanlış Şıklar siliniyor...')
    if (silme <= 0):
        print('Joker hakkınız kalmamıştır.....')
    silme-=1
    time.sleep(3)
    print('B:Akşam geç olur   D:Sabah geç olur')
    cevap5 = input('Cevabınız:')
    if (cevap5 == 'b'):
        print('Tebrikler 5000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

else:
    print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
    time.sleep(4)
    exit()


#######################################################################################


print('Hazırsanız Altıncı Sorunuz geliyor.')
time.sleep(2)
print('\nKlasik bir çengel bulmacada,bir kutucukta en fazla kaç farklı soru sorulur ?')
print('A:1    B:2    C:3    D:4')
soru6=input('Cevabınız:')



if(soru6=='b'):
    print('Tebrikler 7.500TL Kazanmaya Hak Kazandınız..')
    print('Sıradaki Sorunuz Geliyor...')

elif(soru6=='oylama'):
    print('Oylama Yapılıyor....')
    oylama-=1
    if (oylama <= 0):
        print('Joker hakkınız kalmamıştır.....')
    time.sleep(4)
    print('Oylama sonuçlarına göre b şıkkı çoğunluktadır.')

    cevap6 = input('Cevabınız:')
    if (cevap6 == 'b'):
        print('Tebrikler 7.500tl Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')
    else:
        print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
        time.sleep(4)
        exit()
elif(soru6=='bakma'):
    print('Googledan bakabilirsiniz.')
    if (bakma <= 0):
        print('Joker hakkınız kalmamıştır.....')
    bakma-=1
    cevap6 = input('Cevabınız:')
    if (cevap6 == 'b'):
        print('Tebrikler 7.500TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

elif(soru6=='silme'):
    print('Yanlış Şıklar siliniyor...')
    if (silme <= 0):
        print('Joker hakkınız kalmamıştır.....')
    silme-=1
    time.sleep(3)
    print('B:2   D:4')
    cevap6 = input('Cevabınız:')
    if (cevap6 == 'b'):
        print('Tebrikler 7.500TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

else:
    print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
    time.sleep(4)
    exit()


############################################################


print('Hazırsanız Yedinci Sorunuz geliyor.')
time.sleep(2)
print('\nİki dirhem bir çekirdek ifadesi kimler için kullanılır ?')
print('A:Güzel ve özenle giyinenler    B:Az ve seyrek giyinenler    C:Boylu ve kilolu olanlar    D:Güçlü ve kaslı olanlar')
soru7=input('Cevabınız:')



if(soru7=='a'):
    print('Tebrikler 15.000TL Kazanmaya Hak Kazandınız..')
    print('Sıradaki Sorunuz Geliyor...')

elif(soru7=='oylama'):
    print('Oylama Yapılıyor....')
    oylama-=1
    if (oylama <= 0):
        print('Joker hakkınız kalmamıştır.....')
    time.sleep(4)
    print('Oylama sonuçlarına göre a şıkkı çoğunluktadır.')

    cevap7 = input('Cevabınız:')
    if (cevap7 == 'a'):
        print('Tebrikler 15.000tl Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')
    else:
        print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
        time.sleep(4)
        exit()
elif(soru7=='bakma'):
    print('Googledan bakabilirsiniz.')
    if (bakma <= 0):
        print('Joker hakkınız kalmamıştır.....')
    bakma-=1
    cevap7 = input('Cevabınız:')
    if (cevap7 == 'a'):
        print('Tebrikler 15.000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

elif(soru7=='silme'):
    print('Yanlış Şıklar siliniyor...')
    if (silme <= 0):
        print('Joker hakkınız kalmamıştır.....')
    silme-=1
    time.sleep(3)
    print('A:Güzel ve özenle giyinenler   C:Boylu ve kilolu olanlar')
    cevap7 = input('Cevabınız:')
    if (cevap7 == 'a'):
        print('Tebrikler 15.000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

else:
    print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
    time.sleep(4)
    exit()

##############################################################################

print('Hazırsanız Sekizinci Sorunuz geliyor.')
time.sleep(2)
print('\n333 le hangi sayının toplamı 1000 dir ?')
print('A:667    B:677   C:767    D:777')
soru8=input('Cevabınız:')



if(soru8=='a'):
    print('Tebrikler 30.000TL Kazanmaya Hak Kazandınız..')
    print('Sıradaki Sorunuz Geliyor...')

elif(soru8=='oylama'):
    print('Oylama Yapılıyor....')
    oylama-=1
    if (oylama <= 0):
        print('Joker hakkınız kalmamıştır.....')
    time.sleep(4)
    print('Oylama sonuçlarına göre a şıkkı çoğunluktadır.')

    cevap8 = input('Cevabınız:')
    if (cevap8 == 'a'):
        print('Tebrikler 30.000tl Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')
    else:
        print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
        time.sleep(4)
        exit()
elif(soru8=='bakma'):
    print('Googledan bakabilirsiniz.')
    if (bakma <= 0):
        print('Joker hakkınız kalmamıştır.....')
    bakma-=1
    cevap8 = input('Cevabınız:')
    if (cevap8 == 'a'):
        print('Tebrikler 30.000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

elif(soru8=='silme'):
    print('Yanlış Şıklar siliniyor...')
    if (silme <= 0):
        print('Joker hakkınız kalmamıştır.....')
    silme-=1
    time.sleep(3)
    print('A:667   D:777')
    cevap8 = input('Cevabınız:')
    if (cevap8 == 'a'):
        print('Tebrikler 30.000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

else:
    print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
    time.sleep(4)
    exit()

###########################################################################


print('Hazırsanız Dokuzuncu Sorunuz geliyor.')
time.sleep(2)
print('\nTatar yayı olarak bilinen ve Orta Çağda yaygın olarak kullanılan uzak mesafe silahı hangisidir ?')
print('A:Topuz    B:Kama   C:Tüfek    D:Arbalet')
soru9=input('Cevabınız:')


if(soru9=='d'):
    print('Tebrikler 60.000TL Kazanmaya Hak Kazandınız..')
    print('Sıradaki Sorunuz Geliyor...')

elif(soru9=='oylama'):
    print('Oylama Yapılıyor....')
    oylama-=1
    if (oylama <= 0):
        print('Joker hakkınız kalmamıştır.....')
    time.sleep(4)
    print('Oylama sonuçlarına göre d şıkkı çoğunluktadır.')

    cevap9 = input('Cevabınız:')
    if (cevap9 == 'd'):
        print('Tebrikler 60.000tl Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')
    else:
        print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
        time.sleep(4)
        exit()
elif(soru9=='bakma'):
    print('Googledan bakabilirsiniz.')
    if (bakma <= 0):
        print('Joker hakkınız kalmamıştır.....')
    bakma-=1
    cevap9 = input('Cevabınız:')
    if (cevap9 == 'd'):
        print('Tebrikler 60.000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

elif(soru9=='silme'):
    print('Yanlış Şıklar siliniyor...')
    if (silme <= 0):
        print('Joker hakkınız kalmamıştır.....')
    silme-=1
    time.sleep(3)
    print('B:Kama   D:Arbalet')
    cevap9 = input('Cevabınız:')
    if (cevap9 == 'd'):
        print('Tebrikler 60.000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

else:
    print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
    time.sleep(4)
    exit()


##################################################


print('Hazırsanız Onuncu Sorunuz geliyor.')
time.sleep(2)
print('\n999.999.999.999.999 a 1 eklersek hangi sayıya ulaşırız ??')
print('A:1 trilyar    B:1 katrilyon   C:1 sentilyon    D:1 oktilyon')
soru10=input('Cevabınız:')



if(soru10=='b'):
    print('Tebrikler 125.000TL Kazanmaya Hak Kazandınız..')
    print('Sıradaki Sorunuz Geliyor...')

elif(soru10=='oylama'):
    print('Oylama Yapılıyor....')
    oylama-=1
    if (oylama <= 0):
        print('Joker hakkınız kalmamıştır.....')
    time.sleep(4)
    print('Oylama sonuçlarına göre b şıkkı çoğunluktadır.')

    cevap10 = input('Cevabınız:')
    if (cevap10 == 'b'):
        print('Tebrikler 125.000tl Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')
    else:
        print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
        time.sleep(4)
        exit()
elif(soru10=='bakma'):
    print('Googledan bakabilirsiniz.')
    if (bakma <= 0):
        print('Joker hakkınız kalmamıştır.....')
    bakma-=1
    cevap10 = input('Cevabınız:')
    if (cevap10 == 'b'):
        print('Tebrikler 125.000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

elif(soru10=='silme'):
    print('Yanlış Şıklar siliniyor...')
    if (silme <= 0):
        print('Joker hakkınız kalmamıştır.....')
    silme-=1
    time.sleep(3)
    print('B:1 katrilyon   C:1 sentilyon')
    cevap10 = input('Cevabınız:')
    if (cevap10 == 'b'):
        print('Tebrikler 125.000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

else:
    print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
    time.sleep(4)
    exit()

#################################################################3

print('Hazırsanız Onbirinci Sorunuz geliyor.')
time.sleep(2)
print('\nEski türk toplumunda düğünden önce erkek tarafından  gelinin ailesine hangi adla bilinen bir para veya hediye verilirdi ?')
print('A:İnce    B:Kalın   C:Dar    D:Geniş')
soru11=input('Cevabınız:')



if(soru11=='b'):
    print('Tebrikler 250.000TL Kazanmaya Hak Kazandınız..')
    print('Sıradaki Sorunuz Geliyor...')

elif(soru11=='oylama'):
    print('Oylama Yapılıyor....')
    oylama-=1
    if (oylama <= 0):
        print('Joker hakkınız kalmamıştır.....')
    time.sleep(4)
    print('Oylama sonuçlarına göre b şıkkı çoğunluktadır.')

    cevap11 = input('Cevabınız:')
    if (cevap11 == 'b'):
        print('Tebrikler 250.000tl Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')
    else:
        print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
        time.sleep(4)
        exit()
elif(soru11=='bakma'):
    print('Googledan bakabilirsiniz.')
    if (bakma <= 0):
        print('Joker hakkınız kalmamıştır.....')
    bakma-=1
    cevap11 = input('Cevabınız:')
    if (cevap11 == 'b'):
        print('Tebrikler 250.000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

elif(soru11=='silme'):
    print('Yanlış Şıklar siliniyor...')
    if (silme <= 0):
        print('Joker hakkınız kalmamıştır.....')
    silme-=1
    time.sleep(3)
    print('B:Kalın   D:Geniş')
    cevap11 = input('Cevabınız:')
    if (cevap11 == 'b'):
        print('Tebrikler 250.000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

else:
    print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
    time.sleep(4)
    exit()

#####################################################################333

print('Hazırsanız MİLYONLUK Sorunuz geliyor.')
time.sleep(2)
print('\nKuranı Kerimde hangisinin üzerine yemin edilmemiştir ?')
print('A:Deniz    B:Güneş   C:Arı    D:Kalem')
soru12=input('Cevabınız:')


if(soru12=='c'):
    print('Tebrikler 1.000.000TL Kazanmaya Hak Kazandınız..')
    print('Sıradaki Sorunuz Geliyor...')

elif(soru12=='oylama'):
    print('Oylama Yapılıyor....')
    oylama-=1
    if (oylama <= 0):
        print('Joker hakkınız kalmamıştır.....')
    time.sleep(4)
    print('Oylama sonuçlarına göre c şıkkı çoğunluktadır.')

    cevap12 = input('Cevabınız:')
    if (cevap12 == 'c'):
        print('Tebrikler 250.000tl Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')
    else:
        print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
        time.sleep(4)
        exit()
elif(soru12=='bakma'):
    print('Googledan bakabilirsiniz.')
    if (bakma <= 0):
        print('Joker hakkınız kalmamıştır.....')
    bakma-=1
    cevap12 = input('Cevabınız:')
    if (cevap12 == 'c'):
        print('Tebrikler 250.000TL Kazanmaya Hak Kazandınız..')
        print('Sıradaki Sorunuz Geliyor...')

elif(soru12=='silme'):
    print('Yanlış Şıklar siliniyor...')
    if (silme <= 0):
        print('Joker hakkınız kalmamıştır.....')
    silme-=1
    time.sleep(3)
    print('A:Deniz   C:Arı')
    cevap12 = input('Cevabınız:')
    if (cevap12 == 'c'):
        print('Tebrikler 1.000.000 Kazanmaya Hak Kazandınız..')
        print('TEBRİKLER MİLYONERSİNİZ..............')
        time.sleep(5)
        exit()

else:
    print('Maalesef yanlış cevapladınız belki birdahaki sefere görüşmek üzere...')
    time.sleep(4)
    exit()

