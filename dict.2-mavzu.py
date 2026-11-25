#1-topshiriq
# narxlar = {"olma": 12000, "banan": 22000, "nok": 18000, "uzum": 9000} 
# for k,v in narxlar.items():
#     if v>1500:
#         print(f"{k} - {v} : qimmat!")
#     else:
#         print(f"{k} - {v} : arzon!")
#-----------------------------------------------------------------------
#2-topshriq
# kontaktlar = {"Ali": "+998901112233", "Vali": "+998935554466"}
# yangilar = {"Sardor": "+998977778899", "Laylo": "+998991234567"}
# a = input("Ismni kiriting: ")
# kontaktlar.update(yangilar)
# if a in kontaktlar:
#     print(kontaktlar[a])
# else:
#     print("Bunday foydalanuvchi mavjud emas!")
#----------------------------------------------------------------------
#3-topshiriq
# ballar = {"Aziz": 92, "Madina": 74, "Jasur": 58, "Nodira": 41, "Otabek": 86}
# yakuniy = {}
# for ism,ball in ballar.items():
#     if 86 <= ball <= 100:
#         yakuniy[ism] = 5
#     elif 71 <= ball <=85:
#         yakuniy[ism] = 4
#     elif 56<= ball <= 70:
#         yakuniy[ism] = 3
#     else:
#         yakuniy[ism] = 2
# print(yakuniy)
#----------------------------------------------------------------------------------
#4-topshiriq
# ombor = {"daftar": 40, "ruchka": 0, "qalam": 15, "o'chirg'ich": 0, "chizg'ich": 7}
# for k,v in list(ombor.items()):
#     if v == 0:
#         print(f"o'chirildi :{k}")
#         del ombor[k]
# print(f"Qoldi : {ombor}")
#--------------------------------------------------------------------------------------
#5-topshiriq
# a = input().split()
# takror = {}
# for j in a:
#     if j in takror:
#         takror[j] += 1
#     else:
#         takror[j] = 1
# print(takror)
#----------------------------------------------------------------------------------
#6-topshiriq
# savat = {"non": 4000, "sut": 11000 , "tuxum": 18000, "pishloq": 35000}
# O = input("Nimani olib tashlamoqchisiz: ")
# print(f"{O} olib tashlandi, -{savat.pop(O,{})} so'm")
# s = savat.values()
# print(f"Jami: {sum(s)}")
#-----------------------------------------------------------------------------------
#7-topshiriq
# oylik = {
#     "Bobur": 3500000,
#     "Dilnoza": 5200000,
#     "Kamol": 2800000,
#     "Zuhra": 4000000
# }

# oshirish = {}

# for ism, maosh in oylik.items():
#     if maosh < 4000000:
#         oshirish[ism] = int(maosh * 1.15)

# oylik.update(oshirish)

# for ism, maosh in oylik.items():
#     print(f"{ism}: {maosh}")
#---------------------------------------------------------------------------------------
# 8-topshiriq
# O'tmagan mavzuimiz bor ekan shuning uchun ishlamagan edim.
#----------------------------------------------------------------------------------------
#9-topshiriq
# lugat = {"men": "I", "kitob": "book", "o'qiyman": "read", "olma": "apple", "yeyman": "eat"}
# Gap = "men olma yeyman tez"
# print(f"{"I"} {"eat"} {"olma"}")
# print("Tarjima qilindi 3 ta so'z")
#----------------------------------------------------------------------------------------
#10-topshiriq
 