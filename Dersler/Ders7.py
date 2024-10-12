# # class Kitap:
# #     def __init__(self,isim,yazar,sayfa_sayısı):
# #         print("Kitapınz oluşturuluyor")
# #         self.isim = isim
# #         self.yazar = yazar
# #         self.sayfa_sayısı = sayfa_sayısı
# #
# #     def __str__(self):
# #         return f"İsim {self.isim}, Yazar : {self.yazar}, Sayfa Sayısı: {self.sayfa_sayısı}"
# #
# #     def __len__(self):
# #         return self.sayfa_sayısı
# #
# #     def __del__(self):
# #         print("kitap objesi siliniyor")
# #
# #
# # kitap1 = Kitap("python","kesifplus",200) #__init__ func çağrılıyor
# # kitap2 = Kitap("java","bugra",150)
# # print(len(kitap1))
# # print(len(kitap2))
# # print(kitap1) #__str__
# # print(kitap2)
# #
# # del kitap1 # __del__
# from pprint import pprint
#
#
# # class Yazılımcı:
# #     def __init__(self):
# #         pass
# #
# #     def bilgileri_göster(self):
# #         self.maas_zam()
# #         self.A = 5
# #
# #     def dil_Ekle(self):
# #         print(self.A)
# #
# #     def maas_zam(self):
# #         pass
#
# class Animal:
#     def eat(self):
#         print("yemek yer")
#
#     def sleep(self):
#         print("uyudu")
#
#     def ses_Cıkar(self):
#         print("ses cıkardı")
#
#
# class Cat(Animal):
#     def kedi(self):
#         print("ben kedi")
#
#     def ses_Cıkar(self):
#         super().ses_Cıkar()
#         print("miyav")
#
# class Tekir(Cat):
#     def tekir(self):
#         print("ben tekir")
#
# class Dog(Animal):
#     def Köpek(self):
#         print("ben köpek")
#
#
# hayvan  = Animal()
# hayvan.eat()
# hayvan.sleep()
# hayvan.ses_Cıkar()
# print("************")
#
# maviş = Cat()
# maviş.kedi()
# maviş.sleep()
# maviş.eat()
# maviş.ses_Cıkar()
# print("************")
#
# karabaş = Dog()
# karabaş.Köpek()
# karabaş.eat()
# karabaş.ses_Cıkar()
# print("************")
#
# yaramaz = Tekir()
# yaramaz.tekir()
# yaramaz.kedi()
# yaramaz.eat()
# yaramaz.sleep()

class UserAccount:
    def __init__(self, account_no, password, balance, sec_quesiton, sec_answer):
        self.account_no = account_no
        self.password = password
        self.balance = balance
        self.sec_quesiton = sec_quesiton
        self.sec_answer = sec_answer
        self.işlem_gecmisi = []

    def deposit(self, amount):
        self.balance += amount
        self.işlem_gecmisi.append(f"{amount} yatırıldı")
        print(f"{amount} yatırıldı")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.işlem_gecmisi.append(f"{amount} çekildi")
            print(f"{amount} çekildi")
        else:
            print("yetersiz bakiye")

    def check_balance(self):
        print(f"Bakiyeniz {self.balance}")

    def hesap_geçmişi(self):
        print("İşlem geçmişiniz : ")
        for işlem in self.işlem_gecmisi:
            print(işlem)

    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self.işlem_gecmisi.append(f"{amount} TL transfer edildi -> Hesap No: {target_account.account_no}")
            target_account.işlem_gecmisi.append(f"{amount} TL transfer alındı <- Hesap No: {self.account_no}")
            print(f"{amount} TL başarıyla Hesap No {target_account.account_no}'ya transfer edildi.")
        else:
            print("Yetersiz Bakiye, transfer başarısız")

    def password_recorvy(self):
        print(f"Güvenlik sorusu: {self.sec_quesiton}")
        answer = input("CevaP : ").lower()
        if answer == self.sec_answer.lower():
            new_pass = input("yeni şifre: ")
            self.password = new_pass
            print("başarılı")
        else:
            print("cevap yanlış")


class BankSystem:
    def __init__(self):
        self.users = {
            "1001": UserAccount("1001", "1234", 1000, "Dogum Yeri", "Ankara"),
            "1002": UserAccount("1002", "5678", 750, "ilk öğrendiğin kodlama dili nedir", "python")
        }
        self.admin_account_no = "9999"
        self.admin_pass = "admin123"
        self.hak = 0

    def user_panel(self, user):
        while True:
            print("""
                1. Para yatırma
                2. Para çekme
                3. Bakiye sorgula
                4. İşlem geçmişi
                5. Para transferi
                6. Çıkış
            """)

            secim = input("Secminiz: ")

            if secim == "1":
                miktar = int(input("Tutar : "))
                user.deposit(miktar)
            elif secim == "2":
                miktar = int(input("Tutar : "))
                user.withdraw(miktar)
            elif secim == "3":
                user.check_balance()
            elif secim == "4":
                user.hesap_geçmişi()
            elif secim == "5":
                target_account_no = input("Transfer edilecek hesap numarsını lütfen giriniz : ")
                if target_account_no in self.users:
                    miktar = int(input("Tutar: "))
                    target_account = self.users[target_account_no]
                    user.transfer(target_account, miktar)
                else:
                    print("geçersiz hesap numarası")

            elif secim == "6":
                print("güle güle.....")
                break
            else:
                print("yanlış secim, 1-6")

    def admin_panel(self):
        print("yönetici paneli")
        while True:
            print("""
            1. Tüm kullanıcıların bakiyesini gör
            2. Tüm işlem geçmişini görüntüle
            3. Çıkış
            """)

            secim = input("Secminiz : ")

            if secim == "1":
                for acc_no, user in self.users.items():
                    print("Hesap No: ", acc_no, "Bakiye: ", user.balance)

            elif secim == "2":
                for acc_no, user in self.users.items():
                    print("Hesap No: ", acc_no, "İşlem Geçmişi: ", user.işlem_gecmisi)

            elif secim == "3":
                print("güle güle.....")
                break

            else:
                print("yanlış secim, 1-3")

    def run(self):
        while True:
            acc_no = input("Hesap No: ")
            sifre = input("Şifre: ")

            if (acc_no == self.admin_account_no) and (sifre == self.admin_pass):
                self.admin_panel()
                self.hak = 0
            elif (acc_no in self.users) and (sifre == self.users[acc_no].password):
                self.user_panel(self.users[acc_no])
                self.hak = 0

            else:
                self.hak += 1
                print(f"Yanlış şifre {3 - self.hak} deneme hakkınız kaldı")

                if self.hak == 3:
                    print("3kez yanlış girildi. şifreyi mi unutunuz")
                    sifremi_unuttum = input("şifremi unutum işlemei yapmak istermisiniz? (E/H): ").lower()

                    if sifremi_unuttum == "e":
                        acc_no = input("Hesap No: ")
                        if acc_no in self.users:
                            self.users[acc_no].password_recorvy()
                        else:
                            print("hesao no yanlış")
                    else:
                        print("program sonlanıyor")
                        break


kesifplus_bankası = BankSystem()
kesifplus_bankası.run()
