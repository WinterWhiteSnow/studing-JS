# from math import gcd
# def solution(arr):
#     def lcm(x, y):
#         return x * y // gcd(x, y)

#     while True:
#         arr.append(lcm(arr.pop(), arr.pop()))
#         if len(arr) == 1:
#             return arr[0]
# a = list(map(int,input().split()))
# list_list = []
# for i in range(len(a)):
#     for x in range(i+1,len(a)):
#         for y in range(x+1,len(a)):
#             list_list.append(solution([a[i],a[x],a[y]]))
# print(min(list_list))

# a =input()
# if len(a)>1:
#     for i in range(len(a)):
#         b= list(map(int,list(a[i:])))
#         c = list(map(int,list(a[:i])))
#         b_cnt = 1
#         c_cnt = 1
#         for bb in b:
#             b_cnt*=bb
#         for cc in c:
#             c_cnt*=cc
#         if b_cnt==c_cnt:
#             print("YES")
#             exit()
#     print("NO")
# else:
#     print("NO")

# a,b = input().split()
# a = int(a[::-1])
# b = int(b[::-1])
# c = int(str(a+b)[::-1])    
# print(c)
# cnt = 0
# while True:
#     r = int(input())
#     name_list = []
#     answer_list = []
#     cnt+=1
#     if r == 0:
#         break
#     for i in range(r):
#         a = input().split()
#         name = a[0]
#         write =a[1:]
#         name_list.append(name)
#         answer_list.append(write)
#     print(f"Group {cnt}")
#     is_bully = "false"
#     for i in range(len(name_list)):
#         wow = answer_list[i]
#         count = 0
#         for h in wow:
#             count+=1
#             if h == "N":
#                 bully = i-count
#                 if bully < 0:
#                     bully+=r
#                 elif bully <r-1:
#                     bully-=r
#                 print(name_list[bully],"was nasty about",name_list[i])
#                 is_bully = "true"
#     if is_bully == "false":
#         print("Nobody was nasty")
#     print()
# n = int(input())
# for i in range(n,0,-1):
#     if set(str(i)) == {"7","4"} or set(str(i)) == {"7"} or set(str(i))=={"4"}:
#         print(i)
#         exit()

# r = int(input())
# sero_dict = {}
# garo = []
# sero = []
# for _ in range(r):
#     a = list(input())
#     aa = [len(aaa) for aaa in "".join(a).split("X")]
#     aa = [i for i in aa if i >=2]
#     garo.extend(aa)
#     for i in range(1,len(a)+1):
#         if i not in sero_dict:
#             sero_dict[i]=[a[i-1]]
#         else:
#             sero_dict[i].append(a[i-1])
# for i in sero_dict.values():
#     wow = [len(b) for b in "".join(i).split("X")]
#     wow = [i for i in wow if i>=2]
#     sero.extend(wow)
# print(len(garo),len(sero))

# n = int(input())
# print((n+1)*((n*(n-1))//2)) 

# import datetime
# a,b = map(int,input().split())
# wow= datetime.date(2007,a,b).weekday()
# cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
# print(cssclasses[wow].upper())
# import math
# start = int(input())
# end = int(input())
# start_start = math.ceil(start**(1/2))
# end_end = int(end**(1/2))
# list_list = []
# for i in range(start_start,end_end+1):
#     list_list.append(i*i)
# if len(list_list)==0:
#     print(-1)
# else:
#     print(sum(list_list))
#     print(min(list_list))
cnt = -1
count = 0
n = input()
l = len(n)
print(l,(-1)*l)
while cnt >= l*(-1):
    num = int(n)
    a = int(n[cnt])
    print(n,num,a,cnt)
    if a >= 5:
        num+=(10-a)*10*(count)
    cnt-=1
    count+=1
    n=str(num)

            

    

    
    
    
    

    