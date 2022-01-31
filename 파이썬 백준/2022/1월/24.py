# repeat = int(input())
# for _ in range(repeat):
#     a = int(input())
#     print("="*a)

# repeat = int(input())
# cnt = 0
# for _ in range(1,repeat+1):
#     n,num = input().split()
#     print(n,end=" ")
#     while True:
#         if cnt==3:
#             break
#         else:
#             try:           
#                 if cnt == 0:
#                     print(int(num,8),end=" ")
#                 elif cnt ==1:
#                     print(int(num),end=" ")
#                 elif cnt ==2:
#                     print(int(num,16))
#             except:
#                 print(0,end=" ")
#             cnt+=1
#     cnt=0

# wow = input().split()

# a,x,b,y,c = map(str,wow)
# # first = ["(",a,x,b,")",y,c]
# one = [a,x,b]
# one = eval("".join(one))
# if one < 0:
#     one = str((int(one*(-1)))*(-1))
# else:
#     one = str(int(one))

# two = [one,y,c]
# two = eval("".join(two))
# if two <0:
#     two = int(str((int(two*(-1)))*(-1)))
# else:
#     two = int(str(int(two)))
# # second = [a,x,"(",b,y,c,")"]
# three = [b,y,c]
# three = eval("".join(three))
# if three < 0:
#     three = str((int(three*(-1)))*(-1))
# else:
#     three = str(int(three))
# four = [a,x,three]
# four = eval("".join(four))
# if four < 0:
#     four = int(str((int(four*(-1)))*(-1)))
# else:
#     four = int(str(int(four)))

# print(min(two,four))
# print(max(two,four))

# a,b = map(int,input().split())
# c = int(input())
# if a+b >= c*2:
#     print((a+b)-(2*c))
# else:
#     print(a+b)

# wow = int(input())
# a_list = []
# while wow>0:
#     wow,jinsu = divmod(wow,9)
#     a_list.append(str(jinsu))
# print("".join(i for i in a_list[::-1]))

# n = int(input())
# cnt = 0
# for a in range(2,n,2):#택희
#     for b in range(1,n):#영훈
#         for c in range(3,n):#남규
#             if a+b+c ==n:
#                 if a%2==0 and c>=b+2:
#                     # print(a,b,c)
#                     cnt+=1
# print(cnt)

repeat = int(input())
wow = []
for i in range(1,repeat+1):
    score,sumit_times,upload_time=map(int,input().split())
    wow.append([i,score,sumit_times,upload_time])
wow.sort(key=lambda x : x[1],reverse=True)
if repeat > 1:
    if wow[0][1] == wow[1][1]:
        wow.sort(key=lambda x : (x[2],x[3]))

print(wow[0][0])
    