# l = int(input())
# a_list = list(map(int,input().split()))
# max_list = [i for i in range(1,max(a_list)+1)]
# wow = list(set(max_list)-set(a_list))
# # print(wow)
# if len(wow) == 0:
#     print(max(a_list)+1)
# else:
#     print(min(wow))
# import string
# a_list = list(string.ascii_uppercase)
# n = list(input())
# a_dict = {}
# for i in range(len(a_list)):
#     a_dict[a_list[i]]=i+1
# cnt = 0
# l = len(n)
# for i in range(len(n)):
#     cnt+=(26*l)*a_dict[a_list[i]]
#     l-=1
#     print(l)
# print(cnt)
    
# a = list(map(int,list(input())))
# gap = "what"
# for i in range(1,len(a)):
#     if gap == "what":
#         gap = a[i]-a[i-1]
#     else:
#         if gap != a[i]-a[i-1]:
#             print("흥칫뿡!! <(￣ ﹌ ￣)>")
#             exit()
# print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
# l = int(input())
# a_list = list(map(int,input().split()))
# a_list.append(max(a_list))
# start = 0
# cnt = 0
# cnt_list = []
# for i in range(l+1):
#     if start == 0:
#         start = a_list[i]
#     else:
#         if start > a_list[i]:
#             cnt+=1
#         else:
#             start = a_list[i]
#             cnt_list.append(cnt)
#             cnt=0
# print(max(cnt_list))
# import string
# a_a_list = list(string.ascii_lowercase)
# a_list = list(input())
# start = "what"
# cnt = 0
# for i in range(len(a_list)):
#     if start == "what":
#         start = a_a_list.index(a_list[i])
#         cnt+=1
#     else:
#         if start >= a_a_list.index(a_list[i]):
#             cnt+=1
#         start = a_a_list.index(a_list[i])
# print(cnt)
# print('"'+"C:\\Download\\'hello'.py"+'"')
# print("\"!@#$%^&*()\'")
# print('print("Hello\\nWorld")')
# print((input()+" ")*3)
# a = list(input())
# for i in range(0,len(a),2):
#     print("".join(a[i:i+2]),end=" ")
# a = bool(int(input()))
# print(not a)
# a,b = input().split()
# print(bool(int(a))==False and bool(int(b))==False)
# a,b = map(int,input().split())             
# print(a | b)

# n = int(input())
# if n in [12, 1, 2]:
#     print("winter")
# elif n in [3, 4, 5]:
#     print("spring")
# elif n in [6, 7, 8]:
#     print("summer")
# else:
#     print("fall")
# a = 5
# while True:
#     n = input()
#     if n == "0":
#         a= "0"
#     if a != "0":
#         print(n)
# n = int(input())
# while n > 0:
#     n-=1
#     print(n)
# a = ord(input())
# b = ord("a")
# for i in range(b,a+1):
#     print(chr(i),end=" ")
# n = int(input())
# for i in range(n+1):
#     print(i)
# n = int(input())
# s = 0
# for i in range(1, n+1) :
#     if i%2==0:
#         s+= i
# print(s)
# ok = "ok"
# while True:
#     a = input()
#     if ok == "ok":
#         print(a)
#     if a =="q":
#         ok = "no"
# n = int(input())
# result = 0
# cnt = 1
# while result < n:
#     result+=cnt
#     cnt+=1
# print(cnt-1)
# a,b = map(int,input().split())
# for i in range(1,a+1):
#     for index in range(1,b+1):
#         print(i,index)

# for i in range(1,int(input())+1):
#     if i%10 != 0:
#         if i%10%3 ==0:
#             print("X",end=" ")
#         else:
#             print(i,end=" ")
#     else:
#         print(i,end=" ")
# a,b,c = map(int,input().split())
# for i in range(a):
#     for index in range(b):
#         for ind in range(c):
#             print(i,index,ind)
# print(a*b*c)
# h,b,c = map(int,input().split())
# wow = h*b*c/8/1024/1024
# print(format(wow,".2f"),"MB")
# num = int(input())
# result = 0
# cnt=1
# while result < num:
#     result+=cnt
#     cnt+=1
# print(result)
# for i in range(1,int(input())+1):
#     if i%3 == 0:
#         pass
#     else:
#         print(i,end=" ")
# start,gap,times = map(int,input().split())
# print(start+gap*(times-1))
# start,gap,plus,times = map(int,input().split())
# for _ in range(times-1):
#     start=start*gap+plus
# print(start)    
        