#1-topshiriq
# for i in range(1,11):
#     print(i)
#2-topshiriq
# ism = input("Ism kiritilsin: ")
# for iism in range(6):
#     print(ism)
#3-Topshiriq
# juft_sonlar = []
# for i in range(0,21):
#     if i % 2 ==0 :
#         juft_sonlar.append(i)
# print(juft_sonlar)
#4-topshiriq
# for i in range(11,0,-1):
#     print(i)
#     if i == 1:
#         print("Start!")
#5-topshiriq
# N = int(input("Sonni kiriting: "))
# for i in range(0,N):
#     print(sum(N))
#6-topshiriq
# for i in range(1,11):
#     for j in range(1,11):
#         print(i, "x" ,j, "=",i*j)
#     print("============")
#7-topshiriq
# for i in range(0,11):
#     print(f"{i}ning kvadrati - {i**2}")
#8-topshiriq
# soz  = input()
# for harf in soz:
#     print(harf)
#9-topshiriq
# bosh = []
# for i in range(1,51):
#     if i % 3 == 0:
#         bosh.append(i)
# print(bosh)
# #10-topshiriq
# mevalar = ["olma", "nok", "uzum", "anor"]
# for alohida in mevalar:
#     print(mevalarnumeralized())
def g(x,a=[]):
    a.append(x)
    return sum(a)
print(g(2), g(3), g(4,[1]))