# 1-topshiriq

try:
    son = int(input("Son kiriting: "))
    print(son ** 2)
except ValueError:
    print("Butun son kiriting!")
# 2-topshiriq
# try:
#     a =int(input("Son kiriting: "))
#     b = int(input("Son kiriting: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Sonni nolga bolib bolmaydi !")
# except ValueError:
#     print("Faqat butun son kiriting!")

# # 3-topshiriq

# try:
#     mevalar = ["olma","anor","uzum","banan","gilos"]
#     a = int(input("Indeks kiriting: "))
#     print(mevalar[a])
# except IndexError:
#     print("Indeksni togri kiriting!")
# except ValueError:
#     print("Faqat butun son kiriting! ")

# # 4-topshiriq

# while True:
#     try:
#         yosh = int(input("Yoshni kiriting: "))
#         print("Yoshingiz qabul qilindi !")
#         break
#     except ValueError:
#         print("TRY AGAIN")

# # 5-topshiriq

# while True:
#     try:
#         mahsulotlar = {"non": 3000, 
#                "sut": 12000,
#                 "choy":18000,}
#         mahsulot_kiritish = input("Mahsulot nomini kiriting: ")
#         print(mahsulotlar[mahsulot_kiritish])
#     except KeyError:
#         print("Bunday mahsulot mavjud emas!")
# print("Dastur davom etadi!")