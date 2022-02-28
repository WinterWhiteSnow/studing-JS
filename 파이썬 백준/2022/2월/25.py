# r = lambda : input()
# for _ in range(int(r())):
#     start = int(input())
#     if start == 6174:
#         print(0)
#     else:
#         a = int("".join(i for i in sorted(list(str(start)),reverse=True)))
#         cnt = 0
#         while True:
#             if len(str(a)) < 4:
#                 a = int(str(a)+"0"*(4-len(str(a))))
#             b = int("".join(sorted(list(str(a)))))
#             c = a-b
#             # print(start,a,b,c)
#             cnt+=1
#             if c == 6174:
#                 break
#             start = c
#             a=int("".join(i for i in sorted(list(str(c)),reverse=True)))
#         print(cnt)

# cnt = 1
# while True:
#     wow = input()
#     if wow == "0":
#         break
#     while len(wow)%2 != 1:
#         a= list(wow)
#         b = ""
#         for i in range(0,len(a),2):
#             b+=int(a[i])*a[i+1]
#         # print(wow,a,b)
#         if wow ==b:
#             break
#         wow=b
#     print(f"Test {cnt}: {wow}")
#     cnt+=1

# r = lambda : int(input())
# for _ in range(r()):
#     sugangsang = r()
#     sugangsang_list = input().split()
#     s_dict = {}
#     for i in range(sugangsang):
#         s_dict[sugangsang_list[i]]=82800+3540
#     participant = r()
#     for _ in range(participant):
#         a = input().split()
#         number = a[0]
#         time = a[1:]
#         if number in s_dict:
#             h = int(time[0])
#             m = int(time[1])
#             if h==m==-1:
#                 pass
#             else:
#                 time = h*3600+m*60
#                 s_dict[number]=time
#     best = min(s_dict.values())
#     print([i[0] for i in s_dict.items() if i[1] == best][0],len([i for i in s_dict.values() if i<=21600]))        
# r = lambda : int(input())
# for i in range(r()):
#     l = r()
#     a = list(map(int,input().split()))
#     while len(a) != 2:
#         list_list= []
#         index = 0
#         for _ in range(len(a)//2+1):
#             list_list.append(a[index]+a[(len(a)-1)-index])
#             index+=1
#         a = list_list
#     if a[0] > a[1]:
#         print(f"Case #{i+1}: Alice")
#     else:
#         print(f"Case #{i+1}: Bob")

# r = lambda : int(input())
# for _ in range(r()):
#     ruyl,hang = map(int,input().split())
#     a_dict = {}
#     for _ in range(ruyl):
#         a = input().split()
#         for i in range(len(a)):
#             if i not in a_dict:
#                 a_dict[i]=[a[i]]
#             else:
#                 a_dict[i].append(a[i])
#     cnt = 0
#     for i in range(len(a_dict)):
#         a_list=a_dict[i][::-1]
#         black = 0
#         for i in range(len(a_list)):
#             if a_list[i] == "1":
#                 cnt+=i-black
#                 black+=1    
#     print(cnt)
# r = lambda : int(input())
# while True:
#     a = r()
#     if a == -1:
#         break
#     num = 1
#     a_list = []
#     for i in range(1,a//2+1):
#         if a%i == 0:
#             if i**2 != a:
#                 a_list.extend([i,a//i])
#             else:
#                 a_list.append(i)
#     a_list = list(set(a_list))
#     a_list.sort()
#     a_list=a_list[:-1]
#     if sum(a_list) == a:
#         print(f"{a} =",end="")
#         for i in range(len(a_list)):
#             wow = a_list[i]
#             if i == 0:
#                 print(f" {wow} ",end="")
#             else:
#                 if i == len(a_list)-1:
#                     print(f"+ {wow} ")
#                 else:
#                     print(f"+ {wow} ",end="")
#     else:
#         print(f"{a} is NOT perfect.")

# r = lambda : int(input())
# a_list = []
# for _ in range(r()):
#     a = input()
#     a_list.append(a)
# wow = [i for i in a_list if i[::-1] in a_list]
# print(len(wow[0]), wow[0][len(wow[0])//2])
# r = lambda:input()
# cnt = 1
# while True:
#     a = r()
#     b = r()
#     if a==b=="END":
#         break
#     a_set = set(a)
#     b_set = set(b)
#     is_same = "true"
#     for i in a_set:
#         if a.count(i) != b.count(i):
#             is_same = "false"
#             break
#     if is_same == "true":
#         print(f"Case {cnt}: same")
#     else:
#         print(f"Case {cnt}: different")
#     cnt+=1

# from datetime import timedelta,datetime,date
# today,days = input().split()
# days=int(days)-1
# today = date.fromisoformat(today)
# print(today+timedelta(days=days))

# import string
# a_list = list(string.ascii_uppercase)
# a_dict = {}
# for i in range(10,10+len(a_list)):
#     a_dict[i]=a_list[i-10]
# n,b = map(int,input().split())
# a_str = ""
# while n != 0:
#     wow = n%b
#     if wow>=10:
#         a_str+=a_dict[wow]
#     else:
#         a_str+=str(wow)
#     n=n//b
# print(a_str[::-1])

# r = lambda : input().split()
# a = int(input())
# for _ in range(a):
#     start,end = r()
#     count = start.count(end)
#     start = start.replace(end,"")
#     print(count+len(start))
# import sys
# a = sys.stdin.readline().rstrip()
# l = len(a)//2
# while True:
#     ll = l*2
#     r = len(a)-ll
#     for i in range((len(a)-ll)+1):
#         wow = a[i:i+ll]
#         start = sum([int(i) for i in wow[:l]])
#         end = sum([int(i) for i in wow[l:]])
#         # print(wow,start,end,ll)
#         if start==end:
#             print(len(wow))
#             exit()
#     l-=1
# import string
# a_list = list(string.ascii_lowercase)
# string_dict = {}
# for _ in range(int(input())):
#     a = input().replace(" ","")
#     for i in [".",",","?","!","'",'"']:
#         a.replace(i,"")
#     a = a.lower()
#     string = ""
#     for i in a_list:
#         if i not in a:
#             string+=i
#     if len(string) > 0:
#         print("missing",string)
#     else:
#         print("pangram")
# for _ in range(int(input())):
#     maxi = 0
#     n = ""
#     l = int(input())
#     for _ in range(l):
#         price,name = input().split()
#         price = int(price)
#         if maxi<price:
#             maxi=price
#             n = name
#     print(n)

# n = int(input())
# a = bin(n)[2:][::-1]
# print(int(a,2))
# a_list = []
# for _ in range(int(input())):
#     a = input()
#     a_list.append(a)
# order = input()
# if order == "1":
#     for i in a_list:
#         print(i)
# elif order =="2":
#     for i in a_list:
#         print(i[::-1])
# else:
#     a_list = a_list[::-1]
#     for i in a_list:
#         print(i)
# r,l = map(int,input().split())
# count = r*2
# cnt = 0
# a = ""
# b = ""
# for _ in range(r*2):
#     cnt+=1
#     if cnt <= r:
#         a+=input()
#     else:
#         b+=input()
# cnt = 0
# for i in range(0,len(b),2):
#     # print(set(a[cnt]),set(b[i:i+2]))
#     if set(a[cnt]) == set(b[i:i+2]):
#         pass
#     else:
#         print("Not Eyfa")
#         exit()
#     cnt+=1
# print("Eyfa")   

    
    
        
    