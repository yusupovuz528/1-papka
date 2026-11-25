# # 1-topshiriq
# def juft_toq(n):
#     if n % 2 == 0 :
#         return "Juft"
#     else:
#         return "Toq"
# print(juft_toq(4)) # 4 soni juft bo'lgani uchun ekranga Juft chiqaradi
# print(juft_toq(7)) # 7 soni toq bo'lgani uchun ekranga Toq chiqaradi

# # -----------------------------------

# # 2-topshiriq
# def kvadrat(n):
#     return n ** 2
# print(kvadrat(5)) # 5 sonini 2-darajaga ko'taradi, natija 25
# print(kvadrat(7)) # 7 sonini 2-darajaga ko'taradi, natija 49

# # -----------------------------------

# # 3-topshiriq
# def teskari(n):
#     return n[::-1]
# print(teskari("Salom")) # Salom so'zini teskarisiga aylantiradi, natija molaS
# print(teskari("Qalesan")) # Qalesan so'zini teskarisiga aylantiradi, natija naselaQ

# # -----------------------------------

# # 4-topshiriq
# def polindrom(p):
#     if p[::-1] == p[::1]:
#         return True
#     else:
#         return False
# print(polindrom("anna")) # anna so'zi teskari o'qilganda ham bir xil, shuning uchun True
# print(polindrom("hello")) # hello so'zi teskari o'qilganda o'zgaradi, shuning uchun False

# # -----------------------------------

# # 5-topshiriq
# def yigindi(lst):
#     return sum(lst)
# print(yigindi([1,2,3,4])) # List ichidagi barcha sonlarni qo'shadi: 1+2+3+4 = 10
# print(yigindi([2,4,1,5])) # List ichidagi barcha sonlarni qo'shadi: 2+4+1+5 = 12

# # -----------------------------------

# # 6-topshiriq
# def eng_katta(lst):
#     return max(lst)
# print(eng_katta([3,9,2,7])) # List ichidagi eng katta sonni topadi, natija 9
# print(eng_katta([5,1,3,7])) # List ichidagi eng katta sonni topadi, natija 7

# # -----------------------------------

# # 7-topshiriq
# def unli_sanash(n):
#     a = n.count("a")
#     b = n.count("e")
#     c = n.count("i")
#     d = n.count("o")
#     e = n.count("u")
#     return a+b+c+d+e
# print(unli_sanash("kitobxon")) # So'z ichidagi unli harflarni sanaydi: i, o, o = 3
# print(unli_sanash("Hello World")) # Gap ichidagi unli harflarni sanaydi: e, o, o = 3

# # -----------------------------------

# # 8-topshiriq
# def tub_son(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(tub_son(7)) # 7 faqat 1 ga va o'ziga bo'linadi, shuning uchun True
# print(tub_son(2498)) # 2498 boshqa sonlarga ham bo'linadi, shuning uchun False

# # -----------------------------------

# # 9-topshiriq
# def juftlar(lst):
#     natija = []
#     for i in lst:
#         if i % 2 == 0:
#             natija.append(i)
#     return natija
# print(juftlar([1,2,3,4,5,6])) # List ichidan juft sonlarni ajratib oladi, natija [2, 4, 6]
# print(juftlar([1,6,2,7,4,0])) # List ichidan juft sonlarni ajratib oladi, natija [6, 2, 4, 0]

# # -----------------------------------

# # 10-topshiriq
# def bosh_harf(gap):
#     return gap.title()
# print(bosh_harf("salom dunyo")) # Har bir so'zning birinchi harfini katta qiladi, natija Salom Dunyo
# print(bosh_harf("hElLo woRld")) # Har bir so'zni chiroyli formatga keltiradi, natija Hello World

# # -----------------------------------

# # 11-topshiriq
# def faktorial(s):
#     b = 1
#     for i in range(1,s):
#         i = i + 1
#         b = i * b
#     return b
# print(faktorial(5)) # 5 sonining faktorialini hisoblaydi: 5*4*3*2*1 = 120
# print(faktorial(7)) # 7 sonining faktorialini hisoblaydi: 7*6*5*4*3*2*1 = 5040

# # -----------------------------------

# # 12-topshiriq
# def eng_uzun(lst):
#     return max(lst,key=len)
# print(eng_uzun(["it", "mushuk", "ot"])) # List ichidagi eng uzun so'zni topadi, natija mushuk
# print(eng_uzun(["Shovla","Osh","Palov","Somsa","Makkajoxori"])) # List ichidagi eng uzun so'zni topadi, natija Makkajoxori

# # -----------------------------------

# # 13-topshiriq
# def Baho(ball):
#     if ball >= 90 :
#         return "A"
#     elif  80 <= ball <= 89:
#         return "B"
#     elif 70 <= ball <= 79:
#         return "C"
#     else:
#         return "F"
# print(Baho(85)) # 85 ball 80 va 89 oralig'ida, shuning uchun B bahosini qaytaradi
# print(Baho(60)) # 60 ball 70 dan kichik, shuning uchun F bahosini qaytaradi

# # -----------------------------------

# # 14-topshiriq
# def takrorlanmas(lst):
#     return set(lst)
# print(takrorlanmas([1,2,2,3,3,3])) # Takrorlangan sonlarni olib tashlaydi, natijada {1, 2, 3} qoladi
# print(takrorlanmas([2,3,4,5,5,5,6,6,7,7])) # Takrorlangan sonlarni olib tashlaydi, natijada {2, 3, 4, 5, 6, 7} qoladi

# # -----------------------------------

# # 15-topshiriq
# def raqamlar_yigindisi(s):
#     yigindi = 0
#     for i in s:
#         if i.isdigit():
#             yigindi += int(i)
#     return yigindi
# print(raqamlar_yigindisi("a1b2c3c4")) # Matn ichidagi raqamlarni topib qo'shadi: 1+2+3+4 = 10
# print(raqamlar_yigindisi("Hello World 6789")) # Matn ichidagi raqamlarni topib qo'shadi: 6+7+8+9 = 30

# # # -----------------------------------

# # Rasmdagi 15-topshiriq
# import statistics
# def baho_tahlil(baholar):
#     return f" En yuqori baho: {max(baholar)}\n Eng past baho: {min(baholar)}\n O'rtacha: {statistics.mean(baholar)}\n"
#     s = 0
#     for katta in baholar:
#         if baholar >= 4:
#             s = s + 1
#     return s
# print(baho_tahlil([5,4,3,2,5,4]))