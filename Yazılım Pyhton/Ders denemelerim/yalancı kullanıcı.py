

print("KAYIT YAPMA KISMINA HOŞGELDİNİZ LÜTFEN KAYIDINIZI OLUNUZ")
kullanıcı=input("E-postanız:")
with open("veri.txt","a",encoding="utf-8") as dosya:
    dosya.write("{}\n".format(kullanıcı))


şifre=input("Şifreniz:")
with open("veri.txt","a",encoding="utf-8") as dosya2:
    dosya2.write("{}\n".format(şifre))


şifre2=input("Şifrenizi tekrar yazınız:")
with open("veri.txt","a",encoding="utf-8") as dosya3:
    dosya3.write("{}\n".format(şifre2))


doğum=input("Doğum tarihiniz:")
with open("veri.txt","a",encoding="utf-8") as dosya4:
    dosya4.write("{}\n".format(doğum))



















