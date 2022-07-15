import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n_list = sorted(list(wow()))
# cnt = 1
# if sum(n_list) == 0:
#     print("Impossible")
# else:
#     while True:
#         count = cnt+1
#         if count%2 == 1:
#             a = count**2//2
#             b = count**2//2+1
#             # print(a,b,cnt)
#             if n_list[0]>=a and n_list[1]>=b:
#                 if n_list[0] ==a:
#                     cnt+=1
#                     break
#                 else:
#                     cnt+=1
#             else:
#                 break
#         else:
#             a = count**2//2
#             # print(a)
#             if n_list[0]>=a:
#                 if n_list[0]==a:
#                     cnt+=1
#                     break
#                 else:
#                     cnt+=1
#             else:
#                 break
#     print(cnt)

# while True:
#     a,b,c,d = wow()
#     if a==b==c==d==0:
#         break
#     cnt = 0
#     while len(set([a,b,c,d])) != 1:
#         a,b,c,d=abs(a-b),abs(b-c),abs(c-d),abs(d-a)
#         # print(a,b,c,d)
#         cnt+=1
#     print(cnt)
# for _ in range(one()):
#     a,b = wow()
#     if a>=b:
#         print("MMM BRAINS")
#     else:
#         print("NO BRAINS")
# print("Gnomes:")
# for _ in range(one()):
#     n_list = list(wow())
#     list_list=sorted(n_list)
#     if n_list==list_list or n_list==sorted(n_list,reverse=True):
#         print("Ordered")
#     else:
#         print("Unordered")

# while True:
#     a,b,c,d=  wow()
#     if a==b==c==d==0:
#         break
#     if (c>=a and d>=b) or (c>=b and d>=a):
#         print("100%")
#     else:
#         print(str(max(min(int(d/a*100),int(c/b*100)),min(int(c/a*100),int(d/b*100))))+"%")

         






















