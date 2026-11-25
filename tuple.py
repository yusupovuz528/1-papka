#1-topshiriq
# koordinat = (41.2, 69.2)
# print(koordinat,type(koordinat))

#--------------------------------------------

#2-topshiriq
# talaba = ("Ali", 20, "Toshkent")
# print(talaba[-1],talaba[0])

#--------------------------------------------

#3-topshiriq

# a = (42,)
# b = (42)
# print(type(a),type(b))

#--------------------------------------------

#4-topshiriq
# a = [1, 2, 3, 4, 5]
# b = tuple(a)
# print(len(b))

#--------------------------------------------

#5-topshiriq
# mevalar = ("olma", "banan", "gilos")
# (mevalar[0] = "nok")  # This will raise an error because tuples are immutable

#--------------------------------------------

#6-topshiriq
# ism = "Hasan"
# yosh = 19
# shahar = "Samarqand"
# talaba = ism, yosh, shahar
# print(talaba)

#--------------------------------------------

#7-topshiriq
# sana = (2024, 12, 31)
# yil,oy,kuni = sana
# print(f"Yil: {yil}, Oy: {oy}, Kuni: {kuni}")

#---------------------------------------------

#8=topshiriq
# a = 5 
# b = 10
# a, b = b, a
# print("a:", a)
# print("b:", b)

#---------------------------------------------

#9-topshiriq
# sonlar = (1, 3, 2, 3, 4, 3, 5)
# print(sonlar.count(3))  # 3 raqami necha marta takrorlanishini chiqaradi

#---------------------------------------------

#10-topshiriq
# mevalar = ("olma", "banan", "gilos", "olma") 
# if "nok" in mevalar:
#     print("Ha, nok mevalar orasida mavjud.")
# print(mevalar.index("gilos"))

#---------------------------------------------

# 11-topshiriq
# baholar = (5, 2, 8, 1, 9)
# birinchi, *orta , oxirgi = baholar
# print(birinchi)
# print(*orta)
# print(oxirgi)


#---------------------------------------------

#12-topshiriq
# narxlar = (12000, 8500, 23000, 5000)
# print(min(narxlar),max(narxlar),sum(narxlar))

#---------------------------------------------

#13-topshiriq
#Chiqmadi 

#---------------------------------------------

#14-topshiriq
# talabalar = [("Ali", 85), ("Vali", 70), ("Hasan", 92)]
# for i in talabalar:
#     ism1, ism2, ism3 = talabalar
#     print(f"{ism1}ning bahosi: {ism2}, {ism3}")
# print(max(talabalar, key=lambda x: x[1]))

#---------------------------------------------

#15-topshiriq
# t = (1, 2, [3, 4])
# a = list(t)
# a[2].append(5) 
# a.append(10)
# print(a)