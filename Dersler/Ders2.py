mylist1 = ["AHMET","MEHTMET",10,7.5,True]
mylist2 = list()
# print(type(mylist1))
# print(type(mylist2))
# print(mylist1)


manav = ["elma","üzüm","armut","kavun","elma","havuç"]
# print(manav)
# manav[1] = "karpuz"
# print(manav)
# print(manav[-1])
# print(manav[2:5])

manav.append("salatalık")
# print(manav)
# manav.insert(2,"dometes")
# print(manav)
# # manav.extend(a_manav)
# manav.remove("kavun")
# print(manav)
# manav.pop(1)
# manav.pop()
# manav.clear()
# print(manav)
#
# del manav[1]
# del manav
#
# print(manav)
#

# tuple

myTuple = (10.5,"abc",4,False,"boran")

print(type(myTuple))
print(myTuple)
print(myTuple[1])


tuplım_listhali = list(myTuple)
print(tuplım_listhali)
tuplım_listhali[1] = "asd"
print(tuplım_listhali)
myTuple = tuple(tuplım_listhali)
print(myTuple)

