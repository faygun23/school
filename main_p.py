import school           #schoolu oluşturduğumuz modüle dahil edelim.

ogrenci=school.okul.ogrenci("Fatih","Aygün",23,"11-B",1)
ogretmen=school.okul.ogretmen("Tuğçe","Aygün",200320)
okul=school.okul("Ada Okulu")                           #okul zaten ana sınıfın içinde o yüzden tekrar yazmaya gerek yoktur.
while True:                                             #Program şeklinde kullanacağımız için döngüye sokarız.
    print("\nSevgili {} Sakinleri. Okulumuza Hoşgeldiniz!".format(okul.isim))
    islem=input("Öğrenci İşlemleri İçin 1'e Basın.\nÖğretmen İşlemleri İçin 2'ye Basın.\nÇıkmak İçin '*'a Basın.")
    if islem=="1":
        print("\nÖğrenci Bilgi Sistemine Hoşgeldiniz!")
        islem2=input("Puan Görüntülemek İçin 1'e Basın.\nÖğrenci Bilginizi Görüntülemek İçin 2'ye Basın.")
        if islem2=="1":
            if ogrenci.disiplin_puani==None:
                pass
            else:
                ogrenci.puan_goruntule()
        elif islem2=="2":
            ogrenci.goruntule()
        else:
            print("Yanlış Değer Girdiniz. Görevli Öğretmene Bildirildi!")
            ogrenci.hoca_yakalama()
    elif islem=="2":
        print("\nÖğretmen Bilgi Sistemine Hoşgeldiniz!")
        islem3=input("Disiplin İçin 1'e Basın.\nDers Notu İçin 2'ye Basın.\nÖğretmen Bilgisi İçin 3'e Basın.")
        if islem3=="1":
            sifre=int(input("Lütfen Öğretmen Şifrenizi Giriniz:"))
            if sifre==ogretmen.sifre:
                ogrenci.disiplin()
            elif sifre!=ogretmen.sifre:
                print("Yanlış Şifre Girdiniz. Görevli Öğretmene Bildirildi!")
                ogrenci.hoca_yakalama()
        elif islem3=="2":
            sifre=int(input("Lütfen Öğretmen Şifrenizi Giriniz:"))
            if sifre == ogretmen.sifre:
                if ogrenci.disiplin_puani==None:
                    pass
                else:
                    ogrenci.puan_degis()
            elif sifre != ogretmen.sifre:
                print("Yanlış Şifre Girdiniz. Görevli Öğretmene Bildirildi!")
                ogrenci.hoca_yakalama()
        elif islem3=="3":
            ogretmen.ogretmen_bilgi()
    elif islem=="*":
        break



"""ogrenci1=school.okul.ogrenci("Fatih","AYGÜN",23,"11-FEN-B", 20)  #bir tane öğrenci objesi oluşturalım.
ogretmen=school.okul.ogretmen("Tuğçe", "AYGÜN", 200320)
sifre=int(input("Lütfen Şifrenizi Giriniz:"))
if sifre == ogretmen.sifre:
    ogrenci1.disiplin()
else:
    print("Yetkiniz Yoktur!")
ogretmen.ogretmen_bilgi()"""
#ogrenci1.puan_degis()
#ogrenci1.puan_degis()
#ogrenci1.puan_goruntule()
#ogrenci1.hoca_yakalama()
#ogrenci1.goruntule()     #disiplin metotunu çağıralım.
#ogrenci1.disiplin()
#ogrenci1.goruntule()
#print(ogrenci1.goruntule())    #öğrencinin ismini de göstersin