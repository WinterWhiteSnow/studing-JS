# l = int(input())
# n = input()
# if len(n)==l:
#     n = n.replace("S","1").replace("LL","2")
#     cup= len(n)+1
#     print(min(l,cup))

# num = int(input())
# a = list(map(int,input().split()))
# maxi = 1
# a_list = []
# if len(a) == num:
#     start = a[0]
#     for i in range(1,len(a)):
#         if a[i]>maxi:
#             maxi=a[i]
#         else:
#             a_list.append(maxi-start)
#             start=a[i]
#             maxi=a[i]
#     a_list.append(maxi-start)
#     if len(a_list)>0:
#         if max(a_list)>0:
#             print(max(a_list))
#         else:
#             print(0)
#     else:
#         print(0)
# import string
# wow = list(string.ascii_lowercase)
# a_list = []
# for x in range(1,6):
#     a = input()
#     if len(a) <= 10:
#         if "FBI" in a:
#             a_list.append(x)
# if len(a_list)>0:
#     print(*a_list)
# else:
#     print('HE GOT AWAY!')
# import sys
# red,brown=map(int,sys.stdin.readline().rstrip().split())
# for a in range(1,red):
#     for b in range(1,red):
#         if a*b == red+brown:
#             if (a-2)*(b-2)==brown:
#                 print(b,a)
#                 exit()

# a,b = input().split()
# a = a.replace("6","5")
# b = b.replace("6","5")
# mini = int(a)+int(b)
# a = a.replace("5","6")
# b = b.replace("5","6")
# maxi = int(a)+int(b)
# print(mini,maxi)
                
# a = input().split("-")
# for i in range(len(a)):
#     print(a[i][0],end="")

# price,won = input().split()
# if int(price) == 0:
#     print(0)
# elif int(won) == 0:
#     print(price)
# else:
#     won = int(won)
#     if len(price) <won:
#         print(0)
#     else:
#         a = int(price[-won:])
#         b = int(price[-won])
#         c = "1"+"0"*won
#         if b >=5:
#             print(int(price)+(int(c)-int(a)))
#         else:
#             print(int(price)-int(a))

# import calendar
# d,m = map(int,input().split())
# print(calendar.day_name[calendar.weekday(2009,m,d)]) 

# a = ["A","B","C"]
# b = ["B","A","B","C"]
# c = ["C","C","A","A","B","B"]
# n = int(input())
# answer = list(input())
# a_cnt = 0
# b_cnt = 0
# c_cnt = 0
# name = ["Adrian","Bruno","Goran"]
# for i in range(len(answer)):
#     a_index = a[i%len(a)]
#     b_index = b[i%len(b)]
#     c_index = c[i%len(c)]
#     if answer[i] == a_index:
#         a_cnt+=1
#     if answer[i] == b_index:
#         b_cnt+=1
#     if answer[i] == c_index:
#         c_cnt+=1
# cnt = [a_cnt,b_cnt,c_cnt]

# print(max(cnt))
# for i in range(len(cnt)):
#     if cnt[i] == max(cnt):
#         print(name[i])

# n = input()
# print(oct(int(n,2))[2:])

# wow = []
# for _ in range(9):
#     a = int(input())
#     wow.append(a)
# minus = sum(wow)-100
# for i in wow:
#     if minus-i in wow:
#         if minus-i != i:
#             wow.remove(i)
#             wow.remove(minus-i)
#             break
# for i in wow:
#     print(i)

# aa = list(map(int,input().split()))
# aa.sort()
# a = aa[0]
# b = aa[1]
# c = aa[2]
# s = []
# wow = list(input().lower())
# for i in range(len(wow)):
#     if wow[i] == "a":
#         s.append(a)
#     elif wow[i] == "b":
#         s.append(b)
#     else:
#         s.append(c)
# print(*s)
# import string
# a_list = list(string.ascii_uppercase)
# repeat = int(input())
# for i in range(repeat):
#     cnt = 0
#     a = list(input())
#     oo = set(a_list)-set(a)
#     for i in oo:
#         cnt+=ord(i)
#     print(cnt)

# repeat = int(input())
# for _ in range(repeat):
#     a = int(input())
#     b = int(str(a)[::-1])
#     c = str(a+b)
#     if len(c) <3:
#         x = c[0]
#         y = c[1]
#         if x == y:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         if len(c)%2==1:
#             x = str(c)[:len(c)//2+1]
#             y = str(c)[len(c)//2:][::-1]
#         else:
#             x = str(c)[:len(c)//2]
#             y = str(c)[len(c)//2:][::-1]
#         # print(c,x,y)
#         if x == y:
#             print("YES")
#         else:
#             print("NO")

    


    
    
 
                
                
            
                
                
        