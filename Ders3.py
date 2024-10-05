# mySet = {"elma","armut","üzüm","armut",False,0}
#
# print(type(mySet))
# print(mySet)
#
# print(len(mySet))
#
# mySet.add("python")
# print(mySet)
#
# mySet.remove("elma")
# print(mySet)
#
# mySet.remove("karpuz")
#
# mySet.discard("karpuz")
#
# mySet.pop()
# print(mySet)
#
# mySet.clear()
# print(mySet)
#
# del mySet

# arabamız = {
#     "marka" : "toyota",
#     "model" : "supra",
#     "yıl" : 2013,
#     "renkler" : ["beyaz","siyah","kırmızı","gri"]
# }
#
# print(arabamız)
#
# print(arabamız["marka"])
#
# arabamız["model"] = "corolla"
# print(arabamız)
#
# print(len(arabamız))
#
# arabamız.get("model")
# arabamız.keys()
# arabamız.values()
# arabamız.items()
#
# arabamız.update({"model" : "supra"})
#
# arabamız.update({"motor" : 1.6})
#
# print(arabamız)
#
# arabamız.pop("renkler")
# arabamız.popitem()
# arabamız.clear()
# print(arabamız)
# del arabamız
#
#

# ailem = {
#     "cocuk1" : {
#         "isim" : "ahmet",
#         "yıl" : 2009
#     },
#
#     "cocuk2" : {
#         "isim" : "mehmet"
#     }
# }
#
#
# print(ailem["cocuk1"]["yıl"])
#
#
# manav = ["elma","üzüm","armut","kavun","elma","havuç",["lahana","salatılık"]]
#
# print(manav[-1])
# print(manav[-1][0])
# print(manav[-1][0][2])


# print(10 > 4)
# print(10 < 4)
# print(10 == 4)
# print(10 >= 4)
# print(10 <= 4)
# print(10 != 10)
#
# print(10>54 and 25<100)
# print(10>54 or 25<100)
#
# x = "merhaba dünya"
# print("a" in x)
# print("z" in x)
# print("Merhaba" in x)


# yas = 21
#
# if yas > 18:
#
#     if  (yas % 3) == 0:
#         print("yaşa 3de bölünür")
#
#     print("18 yasından büyük")
#
# elif yas == 18:
#     print("18e eşittir")
# else:
#     print("18 yaşıdna küçüktür")
#
# if yas > 18:
#     print("18 yasından büyük")
#
# if (yas % 3) == 0:
#     print("3 bölünüyor")
#
# print("ifin dışı")


işlem = input("işlem : ")

sayi1 = int(input("1. sayi : "))
sayi2 = int(input("2. sayi : "))

if işlem == "+":
    print(sayi1 + sayi2)

elif işlem == "-":
    print(sayi1 - sayi2)

elif işlem == "*":
    print(sayi1 * sayi2)

elif işlem == "/":
    if sayi2 == 0:
        print("hatalı işlem")
    else:
        print(sayi1 / sayi2)

else:
    print("hatalı işlem")
