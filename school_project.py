import random

class okul():                       #okul sınıfını oluşturuyoruz. İsmini belirlemek için init fonksiyonunu çağırırız
    def __init__(self,isim):
        self.isim=isim

    class ogrenci():                                                       #öğrenci okula bağlı olsa bile öğrenciyi yeni bir sınıf olarak oluşturmalıyız.
        def __init__(self,isim,soyisim,okul_no,sinif,disiplin_puani,ders={"Türkçe":0,"Matematik":0}):      #disiplin puanı 100(temiz), 0(postalanacak). ders: öğrencimizin notları (sözlük gibi olacak)
            self.isim=isim          #öğrencinin değerlerini atarız.
            self.soyisim=soyisim
            self.okul_no=okul_no
            self.sinif=sinif
            self.disiplin_puani=disiplin_puani
            self.ders=ders

        def disiplin (self):                                          #öğrencimizin disiplin puanını kontrol edelim. init fonksiyonun içindeki disiplin puanına erişmek için (self) yazdık.
            disiplin=input("Öğrenci Disiplin Durumu (Evet/Hayır):")   #aksi halde self.disiplin_puani kullanmamış olsaydık bu satırdaki (self) i parametre olarak algılardı. değer girmemizi beklerdi.
            if (disiplin=="Evet"):                                    #Öğrenci disipline giderse disiplin puanını 10 azaltırız.
                self.disiplin_puani-=10
                if(self.disiplin_puani<=0):                             #öğrencinin puanı 0 veya 0 dan küçükse öğrenciyi postala
                    print("Öğrencinin Kaydı Silindi.")
                    self.isim = None
                    self.soyisim = None
                    self.okul_no = None
                    self.sinif = None
                    self.disiplin_puani = None
                else:
                    print("Öğrencinin Disiplin Puanı 10 Puan Azaldı. Öğrencinin Yeni Disiplin Puanı:", self.disiplin_puani)
            elif (disiplin != "Evet" or disiplin == "Hayır"):
                print("Lütfen Sistemi Meşgul Etmeyin!")

        def goruntule (self):                       #öğrencinin bilgilerini görüntüleme.
            print("""
                İsim: {}
                Soyisim: {}
                Okul No: {}
                Sınıf: {}
                Disiplin Puanı: {}
            """.format(self.isim,self.soyisim,self.okul_no,self.sinif,self.disiplin_puani))

        def puan_degis (self):                  #öğrencinin türkçe ve matematik notları üzerinde puan değiştirme işlemi
            girdi=input("Lütfen Puanı Değiştirmek İstediğiniz Dersi Giriniz (Türkçe/Matematik):")
            if girdi == "Türkçe":
                self.ders["Türkçe"]=int(input("Lütfen Puanı Giriniz:"))    #girdi türkçeye eşitse anahtarıma bir değer atasın
                if 0 <= self.ders["Türkçe"] <= 100:                         #atanan değer 0-100 arasındaysa puanımı değiştirsin ve atama işlemi gerçekleşsin
                    print("Başarılı Bir Şekilde Puan Değişti. Türkçe Puanınız:",self.ders["Türkçe"])
                else:
                    print("Puan Değişemedi!")
                    self.ders["Türkçe"]=0                                   #Puan atayamadığı için varsayılan olarak 0 değerini atayacak
            elif girdi == "Matematik":
                self.ders["Matematik"]=int(input("Lütfen Puanı Giriniz:"))
                if 0 <= self.ders["Matematik"] <= 100:
                    print("Başarılı Bir Şekilde Puan Değişti. Matematik Puanınız:",self.ders["Matematik"])
                else:
                    print("Puan Değişemedi!")
                    self.ders["Matematik"] = 0
            else:
                print("Böyle Bir Ders Yoktur!")

        def puan_goruntule (self):                                  #öğrencinin türkçe matematik notlarını görüntüleme
            print("""
                Türkçe Notunuz: {}
                Matematik Notunuz: {}
            """.format(self.ders["Türkçe"],self.ders["Matematik"]))

        def hoca_yakalama (self):                               #hoca öğrenciyi suç üstü yakalarsa disiplin puanı 2 azalsın
            sayi=random.randint(1,2)                        #sayi değişkenini oluşturalım. rasgele 1 yada 2 değerini döndürecek
            if sayi ==  1:
                print("Öğrenci Hocaya Yakalandı!")
                self.disiplin_puani -= 2
            elif sayi == 2:
                print("Yanlış Alarm!")

    class ogretmen():                                       #öğretmen sınıfı oluştururuz.öğrenciyi disipline vermeye yetkili biri
        def __init__(self,isim,soyisim,sifre=123456):
            self.isim=isim
            self.soyisim=soyisim
            self.sifre=sifre

        def ogretmen_bilgi (self):
            print("""
                ÖĞRETMEN
                İsim: {}
                Soyisim: {}
            """.format(self.isim, self.soyisim))




