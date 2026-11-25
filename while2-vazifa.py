#1.1-topshiriq
# i = 0
# a = []
# while i < 10:
#     i = i + 1 
#     a.append(i)
# print(a)

#-----------------------------------

# 2.1-topshiriq
# n = int(input("Son kiriting: "))
# i = 0 
# s = 0
# while i < n:
#     i = i + 1
#     s = s + i
# print(s)

#-------------------------------------

#3-topshiriq
# n = int(input("Son kiriting: "))
# i = 0 
# while i < n-1:
#     i = i + 2
#     print(i)

#-------------------------------------

# 3-topshiriq
#Menyu yaratish 
# while True:
#     a = int(input("Raqamni tanlang: "))
#     if a == 1:
#         print("1. Salomlashish")
#     elif a == 2:
#         print("2.Ismlarni chiqarish")
#     elif a == 0 :
#         print("Bunday buyruq mavjud emas")
#         break

#-------------------------------------------

# 3-topshiriq
#Tahmin qilish oyini 

# a = "Hello"
# while True:
#     soz = input("Soz kiriting:")
#     if a == soz:
#         print("Urra soz topildi")
#     else:
#         print("Try again")

#-------------------------------------------

#4-topshiriq
#Login va parol
# login = "Yusupov.dev"
# parol = "Jahongiry12345"
# while True:
#     a = input("Login kiriting: ")
#     b = input("Parol kiriting: ")
#     if a == login and b == parol:
#         print("Muvaffaqiyatli kirdingiz! ")
#     else:
#         print("Login yoki parol xato! ")

#---------------------------------------------

#5-topshiriq
#Xaridlar royxati
# while True:
#     n = int(input("Raqam tanlang:"))
#     a = {"1" : "Olma",
#          "2" : "Banan",
#          "3" : "Xurmo",
#          "4" : "Shaftoli", 
#          "5" : "Anor",
#          "6" : "Nok", 
#          "7" : "Behi",
#          "8" : "Gilos",
#          "9" : "Uzum",
#          "10" : "O'rik"}
#     if n == 1 :
#         print(a["1"])
#     elif n == 2 :
#         print(a["2"])
#     elif n == 3 :
#         print(a["3"])
#     elif n == 4 :
#         print(a["4"])
#     elif n == 5 :
#         print(a["5"])
#     elif n == 6 :
#         print(a["6"])
#     elif n == 7 :
#         print(a["7"])
#     elif n == 8 :
#         print(a["8"])
#     elif n == 9 :
#         print(a["9"])
#     elif n == 10 :
#         print(a["10"])
#     else:
#         print("Bunday mahsulot mavjud emas")

#------------------------------------------------------------

#6-topshiriq
#Parolni topish
# a = "Paroliyoq"
# while True:
#     n = input("Parolni kiriting: ")
#     if a == n :
#         print("To'g'ri Parol")
#     else:
#         print("Noto'g'ri Parol")