# import math
# repeat = int(input())
# A = [9.23076,1.84523,56.0211,4.99087,0.188807,15.9803,0.11193]
# B = [26.7,75,1.5,42.5,210,3.8,254]
# C = [1.835,1.348,1.05,1.81,1.41,1.04,1.88]
            
# for _ in range(repeat):
#     score = 0
#     wow = list(map(int,input().split()))
#     for i in range(len(wow)):
#         if i == 0 or i== 3 or i==6:
#             e = B[i]-wow[i]
#         else:
#             e = wow[i]-B[i]
#         score+=int((math.pow(e,C[i]))*A[i])
#     print(score)

# repeat = int(input())
# x_list = []
# y_list = []
# for _ in range(repeat):
#     x,y = map(int,input().split())
#     x_list.append(x)
#     y_list.append(y)
# x = max(x_list)-min(x_list)
# y = max(y_list)-min(y_list)
# print(x*y)   

# repeat = int(input())
# for _ in range(repeat):
#     l = int(input())
#     d = list(map(int,input().split()))
#     if len(d) == l:
#         print(sum(d))

# repeat = int(input())
# for _ in range(repeat):
#     cnt = 0
#     uju,distance = map(int,input().split())
#     for _ in range(uju):
#         best_speed,fuel,using_fuel = map(int,input().split())
#         move = distance/best_speed
#         use = fuel/using_fuel
#         if move <= use:
#             cnt+=1
#     print(cnt)
        
# repeat = int(input())
# for _ in range(repeat):
#     sort,eat = map(int,input().split())
#     wow = list(map(int,input().split()))
#     cnt=0
#     if len(wow) == sort:
#         for i in wow:
#             cnt+=i//eat
#     print(cnt)

# repeat = int(input())
# qq = 0
# q1=0
# q2=0
# q3=0
# q4=0
# for _ in range(repeat):
#     x,y = map(int,input().split())
#     if x == 0 or y ==0:
#         qq+=1
#     else:
#         if x>0 and y>0:
#             q1+=1
#         elif x>0 and y<0:
#             q4+=1
#         elif x<0 and y>0:
#             q2+=1
#         else:
#             q3+=1
# print(f"Q1: {q1}")
# print(f"Q2: {q2}")
# print(f"Q3: {q3}")
# print(f"Q4: {q4}")
# print(f"AXIS: {qq}")  

# repeat = int(input())
# a = 100
# b = 100
# for _ in range(repeat):
#     x,y=map(int,input().split())
#     if x>y:
#         b-=x
#     elif x<y:
#         a-=y
# print(a)
# print(b)

# repeat = int(input())
# for _ in range(repeat):
#     a,b = map(int,input().split())
#     x = a//b
#     y = a%b
#     print(f"You get {x} piece(s) and your dad gets {y} piece(s).") 

# l,time = map(int,input().split())
# times = list(map(int,input().split()))
# cnt = 0
# t = 0
# if len(times) == l:
#     for i in times:
#         t+=i
#         if t>time:
#             break
#         else:
#             cnt+=1
# print(cnt)


