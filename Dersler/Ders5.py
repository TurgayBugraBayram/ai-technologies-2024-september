# bakiye = 100
# sifre = "1234"
# hak = 0
#
# print("""
# 1. para yatırma
# 2. para çekme
# 3. bakiye sorgula
# 4. çıkış
# """)
#
#
# while hak < 3:
#     kullacı_sifre = input("Şifrenizi Girin : ")
#     if kullacı_sifre == sifre:
#         hak = 0
#         while True:
#
#             secim = input("secimiz : ")
#
#             if secim == "1":
#                  yatırılacak_tutar = int(input("miktar : "))
#                  bakiye += yatırılacak_tutar
#
#             elif secim == "2":
#                 cekilecek_miktar = int(input("miktar : "))
#
#                 if cekilecek_miktar <= bakiye:
#                     bakiye -= cekilecek_miktar
#
#                 else:
#                     print("yetersiz bakiye")
#
#             elif secim == "3":
#                 print(f"Bakiyeniz : {bakiye}")
#
#             elif secim == "4":
#                 print("güle güle...")
#                 break
#
#             else:
#
#                 print("yanlış seçim 1-3")
#     else:
#         hak+=1
#         print(f"Yanlış şifre {3-hak} deneme hakkınız kaldı")
#
# if hak == 3:
#     print("şifre girişi başarısız. program sonlanıyor")


def kahve_yap():
    print("makine çalışıyor")
    print("su ısıtlıyor")
    print("kahveniz hazır")


kahve_yap()


def pizza_siparis(adet, fiyat, biberliMİ):

    # if biberliMİ:
    #     print(f"{adet} dilim pizza sipariş edildi ve biberli")
    # else:
    #     print(f"{adet} dilim pizza sipariş edildi ve bibersiz")

    print(f"{adet} dilim pizza sipariş edildi ve biberli") if biberliMİ else print(f"{adet} dilim pizza sipariş edildi ve bibersiz")


    print(f"Toplam Tutar : {adet * fiyat}")

pizza_siparis(2, 10, True)

pizza_siparis(4, 20, False)


def toplam_fiyat(fiyat1,fiyat2):

    return fiyat1+fiyat2

def vergi(fiyat):
    return fiyat *1.2

fiyatım = toplam_fiyat(10,5)
print(vergi(fiyatım))
vergi(toplam_fiyat(20,2))



def bilgileri_göster(isim = "bilgi yok",yaş = "bilgi yok ",dil = "bilgi yok"):
    print(f"ismi {isim}, yaşı {yaş}, bildiği diller {dil}")

bilgileri_göster("ahmet", 20, "java")
bilgileri_göster()
bilgileri_göster(isim = "mehmet")
bilgileri_göster(yaş = 25)
bilgileri_göster("ayşe",27)
