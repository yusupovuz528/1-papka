# while True:
#     a = input("Sonni kiriting (tugatish uchun 'tugatish'): ")

#     if a == "tugatish":
#         break

#     try:
#         a = int(a)
#     except ValueError:
#         print("Faqat son kiriting!")
#         continue

#     with open("sonlar.txt", "a") as file:
#         file.write(str(a) + "\n")

# # Faylni qayta ochamiz
# with open("sonlar.txt", "r") as file:
#     sonlar = file.read().splitlines()

# sonlar = [int(i) for i in sonlar]

# if len(sonlar) > 0:
#     katta = sonlar[0]
#     kichik = sonlar[0]
#     jami = 0

#     for i in sonlar:
#         if i > katta:
#             katta = i

#         if i < kichik:
#             kichik = i

#         jami += i

#     ortacha = jami / len(sonlar)

#     print("Eng katta son:", katta)
#     print("Eng kichik son:", kichik)
#     print("O'rtacha qiymat:", ortacha)

# else:
#     print("Hech qanday son kiritilmadi!")


#--------------------------------------------------------------------

## 2-topshiriq
# matn = "INFO Bot ishga tushdi\nINFO Foydalanuvchi tizimga kirdi\nWARNING Internet tezligi pasaydi\nINFO Ma'lumotlar yuklandi\nERROR Baza bilan aloqa uzildi\nINFO Bot qayta ishga tushdi\nWARNING Xotira hajmi kamaymoqda\nINFO Yangi foydalanuvchi qo'shildi\nERROR Faylni ochishda xatolik yuz berdi\nINFO Ma'lumotlar saqlandi\nWARNING Server yuklamasi oshdi\nINFO Tizim tekshiruvi boshlandi\nERROR Noto'g'ri parol kiritildi\nINFO Tekshiruv muvaffaqiyatli yakunlandi\nWARNING Tizim yangilanishi mavjud"

# with open("log.txt", "w") as file:
#     file.write(matn)

# with open("log.txt", "r", encoding="utf-8") as file:
#     with open("xatolar.txt", "w", encoding="utf-8") as xato_fayl, \
#          open("xatolar.txt", "w", encoding="utf-8") as warn_fayl, \
#          open("xatolar.txt", "w", encoding="utf-8") as info_fayl:

#         for i in file:
#             qator = i.strip()
#             katta = qator.upper()

#             if "ERROR" in katta:
#                 xato_fayl.write(f"{qator}\n")
#             elif "WARNING" in katta:
#                 warn_fayl.write(f"{qator}\n")
#             elif "INFO" in katta:
#                 info_fayl.write(f"{qator}\n")

#-------------------------------------------------]

# 3-topshiriq
# while True:
#     parol = input("Parol kiriting: ")

#     if (len(parol) >= 8 and
#         any(i.isdigit() for i in parol) and
#         any(i.isupper() for i in parol)):

#         print("Parol to'g'ri!")
#         break
#     else:
#         print("Parol talabga javob bermaydi!")

#--------------------------------------------------]

# 4-topshiriq
