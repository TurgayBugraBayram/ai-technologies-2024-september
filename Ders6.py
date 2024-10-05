users = {
    "1001": {"şifre": "1234",
             "bakiye": 100,
             "işlemler": [],
             "güvenlik_sorusu": "dogum yeriniz",
             "güvenlik_cevap": "ankara"},
    "1002": {"şifre": "2435",
             "bakiye": 150,
             "işlemler": [],
             "güvenlik_sorusu": "en sevdiği kodlama dili",
             "güvenlik_cevap": "python"
             }
}

admin_hesap_no = "9999"
admin_password = "admin123"

hak = 0


def şifre_sıfırla(hesap_no):
    if hesap_no in users:
        print("Güvenlik sorusu", users[hesap_no]["güvenlik_sorusu"])
        answer = input("Cevapınız girin : ")
        if answer == users[hesap_no]["güvenlik_cevap"]:
            new_pass = input("Yeni şifreyi giriniz")
            users[hesap_no]["şifre"] = new_pass
            print("başarıyla güncellendi")
        else:
            print("güvenlik cevabı yanlış")
    else:
        print("hesap numarası bulunamadı")


def user_panel(hesap_no):
    while True:
        print("""
              1. Para yatırma
              2. Para çekme
              3. Bakiye sorgula
              4. İşlem geçmişi
              5. Çıkış
              """)

        secim = input("Seçimiz: ")

        if secim == "1":
            miktar = int(input("Tutar: "))
            users[hesap_no]["bakiye"] += miktar
            users[hesap_no]["işlemler"].append(f"{miktar} yatırıldı")
            print(f"{miktar} yatırıldı")

        elif secim == "2":
            miktar = int(input("Tutar: "))
            if miktar <= users[hesap_no]["bakiye"]:
                users[hesap_no]["bakiye"] -= miktar
                users[hesap_no]["işlemler"].append(f"{miktar} çekildi")
                print(f"{miktar} çekildi")
            else:
                print("Yetersiz bakiye")

        elif secim == "3":
            print("Bakiyeniz: ", users[hesap_no]["bakiye"])

        elif secim == "4":
            print("İşlem Geçmişiniz: ")
            for işlem in users[hesap_no]["işlemler"]:
                print(işlem)

        elif secim == "5":
            print("güle güle.....")
            break

        else:
            print("Yanlış seçim,1-5")

def admin_panel():
    print("yönetici paneline hoşgeldiniz")
    while True:
        print("""
           1. Tüm kullanıcıların bakiyesini gör
           2. Tüm işlem geçmişini görüntüle
           3. Çıkış
           """)

        secim = input("seçimiz: ")

        if secim == "1":
            for hesap_no,bilgi in users.items():
                print("Hesap No :" ,hesap_no, " Bakiye:", bilgi["bakiye"])

        elif secim == "2":
            for hesap_no,bilgi in users.items():
                print("Hesap No :" ,hesap_no, " İşlemler:", bilgi["işlemler"])

        elif secim == "3":
            print("güle güle......")
            break

        else:
            print("yanlış secim, 1-3")

while 1:
    hesap_no = input("Hesap numarınız girin: ")
    sifre = input("Şifrenizi Girin: ")

    if (hesap_no == admin_hesap_no) and (sifre == admin_password):
        admin_panel()
        hak=0
    elif (hesap_no in users) and (sifre == users[hesap_no]["şifre"]):
        hak= 0
        user_panel(hesap_no)
    else:
        hak+=1
        kalan_hak = 3-hak
        print("yanlış şifre", kalan_hak , "kalan hakkınız")

        if hak == 3:
            print("3kez yanlış girildi. şifreyi mi unutunuz")
            sifremi_unuttum = input("şifremi unutum işlemei yapmak istermisiniz? (E/H): ").lower()

            if sifremi_unuttum == "e":
                hesap_no = input("Heesap numarınız girin: ")
                şifre_sıfırla(hesap_no)
            else:
                print("program sonlanıyor")
                break
#

mySet = {}
myDict = {}
print(type(mySet))

class Araba:
    def __init__(self,model="bilgi yok",marka="bilgi yok",beygirgücü="bilgi yok"):
        print("init çalıştı")
        self.model = model
        self.marka = marka
        self.beygirgücü = beygirgücü
        self.renk = "beyaz"


    def modifiye(self):
        self.beygirgücü += 50



araba1 = Araba("supra","toyata",300)
araba2 = Araba("megane","Ranult",110)
araba3 = Araba()

araba4 = Araba()


print(araba1.model)
print(araba1.beygirgücü)
araba1.modifiye()
print(araba1.beygirgücü)
print(araba2.model)


metin = "mehrba python"
print(type(metin))
metin.lower()
metin.isalpha()
print(type(araba1))
araba1.modifiye()