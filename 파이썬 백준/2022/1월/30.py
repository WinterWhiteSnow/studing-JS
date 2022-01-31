# now = list(map(int,input().split(":")))
# now = now[0]*3600+now[1]*60+now[2]
# after = list(map(int,input().split(":")))
# after = after[0]*3600+after[1]*60+after[2]
# wait = after-now
# wait = wait % 86400
# h = wait//3600
# m = (wait-(3600*h))//60
# # s = (wait-(3600*h)-(60*m))
# s = wait%60
# if h <10:
#     h = f"0{h}"
# if m <10:
#     m = f"0{m}"
# if s < 10:
#     s = f"0{s}"
# print(f"{h}:{m}:{s}")

# box,book = map(int,input().split())
# boxes = list(map(int,input().split()))
# books = list(map(int,input().split()))
# index = 0
# a = 0
# books
# while index < len(boxes) and a < len(books):
#     if boxes[index] >= books[a]:
#         boxes[index]-=books[a]
#         a+=1
#         if boxes[index] == 0:
#             index+=1
#     else:
#         index+=1
# print(sum(boxes))

# h,m,s = map(int,input().split(":"))
# hs = [i for i in range(1,13)]
# ms = [i for i in range(60)]
# ss = [i for i in range(60)]
# wow = [hs,ms,ss]

# cnt = 0

# for a in range(len(wow)):
#     for b in range(len(wow)):
#         for c in range(len(wow)):
#             if a==b or b==c or c==a:
#                 pass
#             else:
#                 if min(wow[a]) <= h <= max(wow[a]):
#                     if min(wow[b]) <= m <= max(wow[b]):
#                         if min(wow[c]) <= s <= max(wow[c]):
#                             cnt+=1
# print(cnt)

# l = int(input())
# wow = list(map(int,input().split()))
# set_wow = set(wow)
# print(len(wow)-set(wow))

# l,repeat = map(int,input().split())
# wow = list(map(int,input().split(",")))
# temporary = []
# if len(wow) == l:
#     for _ in range(repeat):
#         for i in range(1,len(wow)):
#             a = wow[i]
#             b = wow[i-1]
#             temporary.append(a-b)
#         wow=temporary
#         temporary= []
# for i in wow[:-1]:
#     print(str(i)+",",end="")
# print(wow[-1])

# n = int(input())
# cnt = 1
# count=0
# while n != 0:
#     if n >= cnt:
#         n-=cnt
#         cnt+=1
#         count+=1
#     else:
#         cnt=1
# print(count)

# person,limit,location = map(int,input().split())
# people = [i for i in range(1,person+1)]
# people_dict = {}

# for i in people:
#     people_dict[i]=0
# people_dict[1]=1
# cnt = 1
# count = 0
# while max(list(people_dict.values())) != limit:       
#     if people_dict[cnt]%2 == 1:
#         cnt+=location
#         if cnt > person:
#             cnt = cnt-person
#         people_dict[cnt]+=1
#         count+=1
#     else:
#         cnt-=location
#         if cnt <= 0:
#             cnt = cnt%person
#             if cnt == 0:
#                 cnt=person
#         people_dict[cnt]+=1
#         count+=1
# print(count)
#3581 -> 3567
# repeat = int(input())
# wow = []
# for _ in range(repeat):
#     a = int(input())
#     wow.append(a)

# def see(wow):
#     maxi = 0
#     cnt = 0
#     for i in wow:
#         if i > maxi:
#             cnt+=1
#             maxi=i
#     return cnt
# print(see(wow))
# print(see(wow[::-1]))

dict_list = {"AA":"A","AG":"C","GA":"C","AC":"A","CA":"A","AT":"G","TA":"G","GG":"G","GC":"T","CG":"T","GT":"A","TG":"A","CC":"C","CT":"G","TC":"G","TT":"T"}
l = int(input())
wow = input()
if len(wow) == l:
    while len(wow) != 1:
        a = wow[-2:]
        # print(dict_list[a])
        wow = wow[:-2]+dict_list[a]
    print(wow)

    
        
        

