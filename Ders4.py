# bakiye = 100
#
# print("""
# 1. para yatırma
# 2. para çekme
# 3. bakiye sorgula
# 4. çıkış
# """)
#
# secim = input("secimiz : ")
#

# if secim == "1":
#      yatırılacak_tutar = int(input("miktar : "))
#      bakiye += yatırılacak_tutar
#
# elif secim == "2":
#     cekilecek_miktar = int(input("miktar : "))
#
#     if cekilecek_miktar <= bakiye:
#         bakiye -= cekilecek_miktar
#
#     else:
#         print("yetersiz bakiye")
#
# elif secim == "3":
#     print(f"Bakiyeniz : {bakiye}")
#
# else:
#     print("yanlış seçim 1-3")


# while döngüleri

# i = 0
# while i < 10:
#     print(i,"merhaba")
#     i+=1
#     if i == 3:
#         break

j = 0

# while j < 7:
#
#     j+=1
#
#     if j == 4:
#         continue
#
#     print(j)


# for döngüleri


manav = ["elma","üzüm","armut","kavun","elma","havuç"]

# for boran in manav:
#     if meyve == "kavun":
#         break
#
#     print(meyve)

for harf in "elma":
    print(harf)


# for meyve in manav:
#
#     print("")
#
#     if meyve == "kavun":
#         continue
#
#     print(meyve)
#

# print("*******************************")
#
# for i in range(7):
#     print(i)
#
# print("*******************************")
#
# for i in range(2,10):
#     print(i)
#
# print("*******************************")
#

# for i in range(3,15,4):
#     print(i)
# else:
#     print("sonunda bitti")
#
#
for i in range(3):
    for j in range(3):
        print(i,j)


print("merhaba")
x = 5

var = None

if x>5:
    pass

elif x ==100:
    print()


print("ifin dışı")


while True:
    pass

for x in range(1):
    pass