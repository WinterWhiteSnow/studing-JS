# a,b = map(int,input().split())
# wow = a-b
# print(abs(wow))

# a,b,c = map(int,input().split())
# wow = [a,b,c]
# wow.sort()
# if a==b==c:
#     print(10000+wow[0]*1000)
# elif a==b or b==c or a==c:
#     print(1000+wow[1]*100)
# else:
#     print(wow[-1]*100)

# hour,minute = map(int,input().split())
# wait_minute = int(input())
# wow = minute+wait_minute
# if wow >= 60:
#     count = wow//60
#     hour+=count
#     wow-=60*count
#     if hour >= 24:
#         hour-=24
# print(hour,wow)

# hour,minute,second = map(int,input().split())
# wait_second = int(input())
# total_second = second+wait_second
# if total_second >= 60:
#     count = total_second//60
#     minute+=count
#     total_second = total_second%60
#     if minute >= 60:
#         m_count = minute//60
#         hour+=m_count
#         minute=minute%60
#         if hour >=24:
#             hour = hour%24
# print(hour,minute,total_second)

# plus,minus = map(int,input().split())
# wow = plus+minus
# a = wow/2
# b = plus-a
# yes = [a,b]
# yes.sort()
# if minus>plus:
#     print(-1)
# else:
#     if int(a) == a:
#         print(int(yes[-1]),int(yes[0]))
#     else:
#         print(-1)


# a_list = []
# for _ in range(5):
#     wow = int(input())
#     a_list.append(wow)
# a = a_list[1]/a_list[3]
# b = a_list[2]/a_list[4]
# ss = [a,b]
# ss.sort()
# if int(ss[-1]) < ss[-1]:
#     print(a_list[0]-(int(ss[-1])+1))
# else:
#     print(a_list[0]-int(ss[-1]))

# a_list = []
# for _ in range(5):
#     a = int(input())
#     a_list.append(a)
# a = a_list[:3]
# b = a_list[3:]
# a.sort()
# b.sort()
# print(min(a)+min(b)-50)

# for _ in range(3):
#     a,b,c,d,e,f = map(int,input().split())
#     hour = d-a
#     minute = e-b
#     second = f-c
#     if minute < 0:
#         hour-=1
#         minute+=60
#     if second < 0 :
#         minute-=1
#         second+=60
#         if minute < 0:
#             hour-=1
#             minute+=60
#     print(hour,minute,second)
# a_list = []
# for _ in range(5):
#     a = int(input())
#     if a < 40:
#         a = 40
#     a_list.append(a)
# print(sum(a_list)//5)

# a_list = []
# for _ in range(3):
#     a = int(input())
#     a_list.append(a)
# settt = set(a_list)
# wow = sum(a_list)
# if wow == 180:
#     if len(settt) == 1 :
#         print("Equilateral")
#     elif len(settt) == 2 :
#         print("Isosceles")
#     else:
#         print("Scalene")
# else:
#     print("Error")

# a,b,c = map(int,input().split())
# wow = a*b
# money = c-wow
# if money > 0:
#     print(0)
# else:
#     print(money*(-1))

# a = input()
# if a[-1] == "0":
#     a = int(a)
#     five = a//300
#     one = (a-five*300)//60
#     second = (a-five*300-60*one)//10
#     print(five,one,second)
# else:
#     print(-1)

# num = int(input())
# for _ in range(num):
#     a = float(input())
#     wow = round(a*0.8,2)
#     print(f"${wow:.2f}".format(wow=wow))

# a_list = []

# for _ in range(5):
#     a = int(input())
#     a_list.append(a)

# a = a_list[0]
# b = a_list[1]
# b_limit = a_list[2]
# b_plus = a_list[3]
# use = a_list[-1]
# a_price = a*use
# if b_limit < use:
#     b_price = b+(use-b_limit)*b_plus
# else:
#     b_price = b
# if a_price > b_price:
#     print(b_price)
# else:
#     print(a_price)

# month = int(input())
# day = int(input())
# if month <= 2:
#     if month == 2 and day == 18:
#         print("Special")
#     else:
#         if month < 2 or day <= 17 :
#             print("Before")
#         else:
#             print("After")
# else:
#     print("After")

# a = input()
# a_list = input().split()
# print(a_list.count(a))

# a_list = []

# for _ in range(2):
#     a = list(map(int,input().split()))
#     a_list.append(sum(a))
# a_list.sort()
# print(a_list[-1])

# a = "0b"+input()
# wow = int(a,2)*17 #base 진수값
# print(bin(wow)[2:])
# num = ord("가") - 1
# a = int(input())
# print(chr(a+num))

# a_list = []
# for _ in range(2):
#     apple,orange = map(int,input().split())
#     a_list.append([apple,orange])
# wow = a_list[0][0]+a_list[1][1]
# why = a_list[0][1]+a_list[1][0]
# aa = [wow,why]
# aa.sort()
# print(aa[0])

# a_list = list(map(int,input().split()))
# a_list.sort()
# wow = a_list[0]+a_list[-1]
# why = a_list[1]+a_list[2]
# print(abs(wow-why))
# a = []
# for _ in range(6):
#     b = int(input())
#     a.append(b)
# four = a[:4]
# two = a[4:]
# four.sort()
# two.sort()
# print(sum(four[1:])+two[-1])

# total = int(input())
# difference = int(input())
# wow = total-difference
# person = wow//2
# print(person+difference)
# print(person)

# a_list = []
# for _ in range(5):
#     a = int(input())
#     a_list.append(a)
# a = a_list[0] 
# b = a_list[1]
# c = a_list[2]
# d = a_list[3]
# e = a_list[4]
# wait = 0
# if a < 0 :
#     wait += abs(a)*c
#     wait+=d
# elif a == 0:
#     wait+=d
# else:
#     b = b-a
# wait+=b*e
# print(wait)

# a = "0b"+input()
# b = "0b"+input()
# a = int(a,2)
# b = int(b,2)
# wow = a*b
# print(bin(wow)[2:])

# speed,insect,total = map(int,input().split())
# print(total//speed//2*insect)

# n = input()
# if n == "0":
#     print("YONSEI")
# else:
#     print("Leading the Way to the Future")    

# a,b = map(int,input().split())
# print(a*b//2)

a,b,c = map(int,input().split())
if a>b>c:
    print(int(a*b/c))