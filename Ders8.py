class UserAccount:
    def __init__(self, account_no, password, balances, sec_question, sec_answer, is_locked=False):
        self.account_no = account_no
        self.password = password
        self.balances = balances
        self.sec_question = sec_question
        self.sec_answer = sec_answer
        self.işlem_geçmişi = []
        self.is_locked = is_locked

    def deposit(self, amount, currency):
        if currency in self.balances:
            self.balances[currency] += amount
            self.işlem_geçmişi.append(f"{amount} {currency} yatırıldı")
            print(f"{amount} {currency} yatırıldı.")
        else:
            print(f"Geçersiz para birimi: {currency}")

    def withdraw(self, amount, currency):
        if currency in self.balances and self.balances[currency] >= amount:
            self.balances[currency] -= amount
            self.işlem_geçmişi.append(f"{amount} {currency} çekildi")
            print(f"{amount} {currency} çekildi.")
        else:
            print(f"Yetersiz bakiye veya geçersiz para birimi")

    def check_balance(self):
        print("Bakiyeleriniz: ")
        for currency, balance in self.balances.items():
            print(f"{currency}: {balance}")

    def hesap_geçmişi(self):
        print("İşlem geçmişiniz: ")
        for işlem in self.işlem_geçmişi:
            print(işlem)

    def transfer(self, target_account, amount, currency):
        if currency in self.balances and amount <= self.balances[currency]:
            self.balances[currency] -= amount
            target_account.balances[currency] += amount
            self.işlem_geçmişi.append(f"{amount} {currency} transfer edildi -> Hesap No: {target_account.account_no}")
            target_account.işlem_geçmişi.append(f"{amount} {currency} transfer alındı <- Hesap No: {self.account_no}")
            print(f"{amount} {currency} başarıyla Hesap No {target_account.account_no}'ya transfer edildi.")
        else:
            print("Yetersiz bakiye veya geçersiz para birimi, transfer başarısız")

    def password_recovery(self):
        print(f"Güvenlik sorusu: {self.sec_question}")
        answer = input("Cevap: ").lower()
        if answer == self.sec_answer.lower():
            new_pass = input("Yeni şifre: ")
            self.password = new_pass
            print("Şifre başarıyla değiştirildi.")
        else:
            print("Güvenlik sorusu cevabı yanlış. Hesap kilitlendi.")
            self.is_locked = True


class BankSystem:
    def __init__(self):
        self.users = {}
        self.next_account_no = 1001
        self.exchange_rates = {
            "TL_TO_USD": 0.036,
            "USD_TO_TL": 28.0,
            "TL_TO_EUR": 0.031,
            "EUR_TO_TL": 32.5,
            "USD_TO_EUR": 0.86,
            "EUR_TO_USD": 1.16
        }
        self.admin_account_no = "9999"
        self.admin_pass = "admin123"
        self.hak = 0

    def generate_account_number(self):
        account_no = str(self.next_account_no)
        self.next_account_no += 1
        return account_no

    def register(self):
        print("Kayıt Olun:")
        account_no = self.generate_account_number()
        print(f"Hesap numaranız: {account_no}")

        password = input("Şifre: ")
        sec_question = input("Güvenlik Sorusu: ")
        sec_answer = input("Güvenlik Cevabı: ")
        balances = {"TL": 0, "USD": 0, "EUR": 0}
        new_user = UserAccount(str(account_no), password, balances, sec_question, sec_answer)
        self.users[account_no] = new_user
        print(f"{account_no} hesap numarasıyla başarılı bir şekilde kayıt oldunuz.")

    def login(self):
        account_no = input("Hesap No: ")
        sifre = input("Şifre: ")

        if account_no in self.users and self.users[account_no].is_locked:
            print("Bu hesap kilitlenmiştir. Lütfen yöneticiyle iletişime geçin.")
            return

        if account_no == self.admin_account_no and sifre == self.admin_pass:
            self.admin_panel()
            self.hak = 0
        elif account_no in self.users and sifre == self.users[account_no].password:
            self.user_panel(self.users[account_no])
            self.hak = 0
        else:
            self.hak += 1
            print(f"Yanlış şifre {3 - self.hak} deneme hakkınız kaldı")

            if self.hak == 3:
                print("3 kez yanlış girildi. Şifreyi mi unuttunuz?")
                sifremi_unuttum = input("Evet (E) / Hayır (H): ").lower()
                if sifremi_unuttum == 'e' and account_no in self.users:
                    self.users[account_no].password_recovery()
                elif sifremi_unuttum == 'h' and account_no in self.users:
                    print("Hesap kilitlendi.")
                    self.users[account_no].is_locked = True
                self.hak = 0

    def currency_conversion(self, user):
        print("Döviz dönüştürme işlemi:")
        from_currency = input("Hangi para biriminden dönüştürmek istiyorsunuz (TL, USD, EUR): ").upper()
        to_currency = input("Hangi para birimine dönüştürmek istiyorsunuz (TL, USD, EUR): ").upper()
        amount = float(input(f"Dönüştürmek istediğiniz miktar ({from_currency}): "))

        conversion_key = f"{from_currency}_TO_{to_currency}"

        if from_currency in user.balances and user.balances[from_currency] >= amount:
            if conversion_key in self.exchange_rates:
                converted_amount = amount * self.exchange_rates[conversion_key]
                user.balances[from_currency] -= amount
                user.balances[to_currency] += converted_amount
                user.işlem_geçmişi.append(f"{amount} {from_currency} -> {converted_amount:.2f} {to_currency} dönüştürüldü")
                print(f"{amount} {from_currency} -> {converted_amount:.2f} {to_currency} dönüştürüldü.")
            else:
                print("Geçersiz dönüşüm")
        else:
            print("Yetersiz bakiye veya geçersiz para birimi")

    def update_exchange_rates(self):
        print("Mevcut döviz kurlarını güncelleyin:")
        for rate in self.exchange_rates:
            new_rate = float(input(f"{rate} güncel değeri girin: "))
            self.exchange_rates[rate] = new_rate
        print("Döviz kurları başarıyla güncellendi.")

    def monthly_account_summary(self, user):
        print(f"Hesap No: {user.account_no} işlem geçmişi:")
        for işlem in user.işlem_geçmişi:
            print(işlem)

    def admin_panel(self):
        print("Yönetici paneli")
        while True:
            print("""
            1. Tüm kullanıcıların bakiyesini gör
            2. Tüm işlem geçmişini görüntüle
            3. Döviz kurlarını güncelle
            4. Hesap bloke kaldır
            5. Kullanıcı ekle
            6. Kullanıcı sil
            7. Çıkış
            """)

            secim = input("Seçiminiz: ")

            if secim == "1":
                for acc_no, user in self.users.items():
                    print(f"Hesap No: {acc_no}, Bakiyeler: {user.balances}, Kilit Durumu: {'Kilitli' if user.is_locked else 'Açık'}")
            elif secim == "2":
                for acc_no, user in self.users.items():
                    self.monthly_account_summary(user)
            elif secim == "3":
                self.update_exchange_rates()
            elif secim == "4":
                acc_no = input("Hesap numarasını girin: ")
                if acc_no in self.users:
                    self.users[acc_no].is_locked = False
                    print(f"Hesap {acc_no} bloke kaldırıldı.")
                else:
                    print("Geçersiz hesap numarası.")
            elif secim == "5":
                self.register()
            elif secim == "6":
                acc_no = input("Silmek istediğiniz hesap numarasını girin: ")
                if acc_no in self.users:
                    del self.users[acc_no]
                    print(f"Hesap {acc_no} başarıyla silindi.")
                else:
                    print("Geçersiz hesap numarası.")
            elif secim == "7":
                break
            else:
                print("Geçersiz seçim.")

    def user_panel(self, user):
        print("Kullanıcı paneli")
        while True:
            print("""
            1. Bakiye kontrolü
            2. Para yatır
            3. Para çek
            4. Havale yap
            5. İşlem geçmişi
            6. Döviz dönüştür
            7. Çıkış
            """)

            secim = input("Seçiminiz: ")

            if secim == "1":
                user.check_balance()
            elif secim == "2":
                amount = float(input("Yatırmak istediğiniz miktar: "))
                currency = input("Hangi para birimi (TL, USD, EUR): ").upper()
                user.deposit(amount, currency)
            elif secim == "3":
                amount = float(input("Çekmek istediğiniz miktar: "))
                currency = input("Hangi para birimi (TL, USD, EUR): ").upper()
                user.withdraw(amount, currency)
            elif secim == "4":
                target_acc_no = input("Havale yapmak istediğiniz hesap numarası: ")
                if target_acc_no in self.users:
                    target_account = self.users[target_acc_no]
                    amount = float(input("Havale etmek istediğiniz miktar: "))
                    currency = input("Hangi para birimi (TL, USD, EUR): ").upper()
                    user.transfer(target_account, amount, currency)
                else:
                    print("Geçersiz hesap numarası.")
            elif secim == "5":
                user.hesap_geçmişi()
            elif secim == "6":
                self.currency_conversion(user)
            elif secim == "7":
                break
            else:
                print("Geçersiz seçim.")


bank = BankSystem()

while True:
    print("""
    1. Giriş Yap
    2. Kayıt Ol
    3. Çıkış
    """)

    secim = input("Seçiminiz: ")

    if secim == "1":
        bank.login()
    elif secim == "2":
        bank.register()
    elif secim == "3":
        break
    else:
        print("Geçersiz seçim.")
