import time
print("""
**************************************************
        ATM MAKİNESİNE HOŞGELDİNİZ
        İŞLEMLERİMİZ:
    1-PARA EKLE
    2-PARA ÇEK
    4-ÇIKIŞ YAPMAK İÇİN Q YA BASINIZ
*************************************************
""")

para=2500

sys_kullanıcı="oguz"
sys_şifre="1234"

kullanıcı=input("KULLANICI ADNIZI GİRİNİZ: ")
şifre=input("Şifrenizi giriniz: ")
if(sys_kullanıcı==kullanıcı and sys_şifre==şifre):
    time.sleep(3)
    print("giriş yapıldı,sisteme yönlendiriliyorsunuz........")
    while True:

        işlem1=input("Yapmak istediğiniz işlemi seçiniz: ")
        if(işlem1=="1"):
            ekle=int(input("ne kafar para eklemek istiyorsunuz: "))
            para+=ekle
            print("En son para durumunuz: ",para)
        elif (işlem1 == "2"):
            ekle = int(input("ne kafar para çıkarmak istiyorsunuz: "))
            para -= ekle
            print("En son para durumunuz: ", para)
        else:
            print("çıkış yapılıyor.....")
            exit()

elif(sys_kullanıcı==kullanıcı and sys_şifre!=şifre):
    time.sleep(3)
    print("şifreniz hatalı")
elif(sys_kullanıcı!=kullanıcı and sys_şifre==şifre):
    time.sleep(3)
    print("kullanıcı adınız hatalı")
else:
    print("iki durumda hatalı")






















