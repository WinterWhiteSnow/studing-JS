# repeat = int(input())
# for _ in range(repeat):
#     l = int(input())
#     wow = list(map(int,input().split()))
#     if len(wow) == l :
#         print(min(wow),max(wow))

# n = int(input())
# print(n*(n-1))

# a,b = map(int,input().split())
# start = 1
# for _ in range(a):
#     for i in range(start,start+b):
#         if i == start+b-1:
#             print(i)
#         else:
#             print(i, end=" ")
#     start+=b

# n = int(input())
# cnt=0
# wow = ["3","6","9"]
# for i in range(1,n+1):
#     i = str(i)
#     for a in wow:
#         cnt+=i.count(a)
# print(cnt)

# stress,work,minus,maxi = map(int,input().split())
# cnt_stress = 0
# cnt_work = 0        
# if stress > maxi:
#     print(0)
# else:
#     for _ in range(24):
#         if cnt_stress <= maxi:
#             if cnt_stress+stress <= maxi:
#                 cnt_stress+=stress
#                 cnt_work+=work
#             else:
#                 cnt_stress-=minus
#                 if cnt_stress<0:
#                     cnt_stress=0
#         # print("cnt_stress",cnt_stress)
#     print(cnt_work)    

# a,b,r1 = map(int,input().split())
# x,y,r2 = map(int,input().split())
# if (x-a)*(x-a)+(y-b)*(y-b) < (r1+r2)*(r1+r2):
#     print("YES")
# else:
#     print("NO")

# wow = list(map(int,list(input())))
# if len(wow) == 5:
#     cnt = 0
#     for i in wow:
#         cnt+=i*i*i*i*i
#     print(cnt)

    