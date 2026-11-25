#1-topshiriq
# malumot = {"Ism" : "Ali",
#            "Yosh": 17,
#            "Guruh": "11-B"}
# print(malumot["Ism"])
# print(malumot["Yosh"])
# print(malumot["Guruh"])
#---------------------------------------
#2-topshiriq
# mevalar = {"olma": 5000,
#            "banan": 12000,
#            "uzum": 15000}
# a = input("Nima xarid qilmoqchisiz? ")
# if a == "olma":
#     print(mevalar["olma"])
# elif a == "banan":
#     print(mevalar["banan"])
# elif a == "uzum":
#     print(f"Bizning do'konda {a} mahsulot narxi {mevalar["uzum"]}")
# else:
#     print(f"Bizning do'konda {a} mahsulot turi mavjud emas!")
#----------------------------------------------------------------------------
#3-topshiriq
# ballar = {"Ali": 85,
#           "Vali": 92,
#           "Sardor": 78,
#           "Madina": 95}
# print(ballar["Ali"]+ballar["Vali"]+ballar["Sardor"]+ballar["Madina"])
# print((ballar["Ali"]+ballar["Vali"]+ballar["Sardor"]+ballar["Madina"])/4)
#4-topshiriq
# telefon = {"Ali": "901234567"}
# telefon["Ali"] = 997777777
# print(telefon)
#------------------------------------------------------------------------------------------------
#5-topshiriq
# talaba = {
#     "ism": "Ali",
#     "yosh": 20,
#     "kurs": 2,
#     "shahar": "Toshkent"
# }
# kalitlar = list(talaba.keys())
# qiymatlar = list(talaba.values())

# print("Kalitlar:", kalitlar)
# print("Qiymatlar:", qiymatlar)
# --------------------------------------------------
# 6-topshiriq

# soz = input("so'z kiriting: ")
# harflar={}
# for h in soz:
#     if h in harflar:
#         harflar[h] += 1
#     else:
#         harflar[h] = 1
# print(harflar)
# ------------------------------------------------------------------------------------------------------
#7-topshiriq
# matn = (input("Matnni kiriting: ").split())
# takror = {}
# for j in matn:
#     if j in takror:
#         takror[j]+=1
#     else:
#         takror[j] = 1
# print(takror)
# ------------------------------------------------------------------------------------------------------
# 8-topshiriq
# ballar = {"Ali": 85, "Vali": 92, "Sardor": 78, "Madina": 95}
# maksimal = max(ballar.values())
# minimal = min(ballar.values())
# print(maksimal)
# print(minimal)
#----------------------------------------------------------------------------------------------------------
# 9-topshiriq
# ismlar = ["Ali", "Vali", "Sardor"]
# yoshlar = [17, 18, 16]
# d = {}
# print(dict(zip(ismlar,yoshlar)))
#------------------------------------------------------------------------------------
#10-topshiriq
# a = {"a": 1, "b": 2, "c": 3}
# b = {a["a"]: "a",a["b"]: "b", a["c"]: "c"} 
# print(b)
#---------------------------------------------------------------------------------------
# 11-topshiriq
# kirish = {"Ali": 92, "Vali": 74, "Sardor": 50}
# yakuniy = {}
# for ism,ball in kirish.items():
#     if 86 <= ball <= 100:
#         yakuniy[ism] = 5
#     elif 71 <= ball <= 85:
#         yakuniy[ism] = 4
#     elif 56 <= ball <= 70:
#         yakuniy[ism] = 3
#     else:
#         yakuniy[ism] = 2

# print(yakuniy)
#------------------------------------------------------------------------------------------
#12-topshiriq
# jurnal = {
#     "Ali":    {"matematika": 5, "fizika": 4, "ingliz": 5},
#     "Vali":   {"matematika": 3, "fizika": 4, "ingliz": 4},
#     "Madina": {"matematika": 5, "fizika": 5, "ingliz": 5},
# }
#a)
# print((sum(jurnal["Ali"].values()))/3)
# print(((sum(jurnal["Vali"].values()))/3))
# print((sum(jurnal["Madina"].values()))/3)
#b)
# a = jurnal["Ali"]["matematika"]
# b = jurnal["Vali"]["matematika"]
# # c = jurnal["Madina"]["matematika"]
# print(((jurnal["Ali"]["matematika"])+(jurnal["Vali"]["matematika"])+(jurnal["Madina"]["matematika"]))/3)
# a = jurnal["Ali"]["fizika"]
# b = jurnal["Vali"]["fizika"]
# c = jurnal["Madina"]["fizika"]
# print(((jurnal["Ali"]["fizika"])+(jurnal["Vali"]["fizika"])+(jurnal["Madina"]["fizika"]))/3)
# a = jurnal["Ali"]["ingliz"]
# b = jurnal["Vali"]["ingliz"]
# c = jurnal["Madina"]["ingliz"]
# print(((jurnal["Ali"]["ingliz"])+(jurnal["Vali"]["ingliz"])+(jurnal["Madina"]["ingliz"]))/3)
#c)
# print(jurnal["Madina"])
#-----------------------------------------------------------------------------------------------------
