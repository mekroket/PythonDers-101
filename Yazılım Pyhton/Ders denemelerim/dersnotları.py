print("""
KULLANICI GİRİŞ EKRANI

KULLANICI ADINIZ
ŞİFRENİZ


""")
import time

sys_kullanıcı="oguz"
sys_şifre="1234"

kullanıcı=input("KULLANICI ADNIZI GİRİNİZ: ")
şifre=input("Şifrenizi giriniz: ")
if(sys_kullanıcı==kullanıcı and sys_şifre==şifre):
    time.sleep(3)
    print("giriş yapıldı")
elif(sys_kullanıcı==kullanıcı and sys_şifre!=şifre):
    time.sleep(3)
    print("şifreniz hatalı")
elif(sys_kullanıcı!=kullanıcı and sys_şifre==şifre):
    time.sleep(3)
    print("kullanıcı adınız hatalı")
else:
    print("iki durumda hatalı")
















