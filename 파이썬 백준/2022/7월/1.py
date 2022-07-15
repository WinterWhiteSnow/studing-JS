import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


# for i in sys.stdin.readlines():
#     num_list = i.split()
#     for num in num_list:
#         if num == "0":
#             pass
#         else:
#             n_dict = {}
#             num = int(num)
#             for index in range(1,num//2+1):
#                 if num%index==0:
#                     n_dict[index]=1
#             answer= sum(list(n_dict.keys()))
#             if num == answer:
#                 print(num,"PERFECT")
#             else:
#                 if num > answer:
#                     print(num,"DEFICIENT")
#                 else:
#                     print(num,"ABUNDANT")

# h=one()
# t = one()
# for t in range(1,t+1):
#     answer = (-6)*t**4+h*(t**3)+2*(t**2)+t
#     if answer <= 0:
#         print(f"The balloon first touches ground at hour: {t}")
#         exit()
# print("The balloon does not touch ground in the given time.")

# n_list = [one() for _ in range(2)]
# while n_list[-2]>=n_list[-1]:
#     n_list.append(n_list[-2]-n_list[-1])
# print(len(n_list))

# n = one()
# cnt = 0
# if n <= 5:
#     cnt+=1
# if n%2 == 0:
#     cnt+=1
# n_dict = {}
# for a in range(1,6):
#     for b in range(a+1,6):
#         if a+b == n:
#             cnt+=1
# print(cnt)
# time = inputing()
# time = f"{time:0>4}"
# h,m = int(time[:2]),time[2:]
# ottawa_hour = h if 1<=h<=23 else ""
# print(str(ottawa_hour)+m,"in Ottawa")
# victoria = str(h-3) if 1<=h-3<=23 else str(h-3+24) if 1<=h-3+24<=23 else ""
# print(victoria+str(m),"in Victoria")
# Edmonton = str(h-2) if 1<=h-2<=23 else str(h-2+24) if 1<=h-2+24<=23 else ""
# print(Edmonton+str(m),"in Edmonton")
# Winnipeg = str(h-1) if 1<=h-1<=23 else str(h-1+24) if 1<=h-1+24<=23 else ""
# print(Winnipeg+str(m),"in Winnipeg")
# print(str(ottawa_hour)+m,"in Toronto")
# Halifax = str(h+1) if 1<=h+1<=23 else str(h+1-24) if 1<=h+1-24<=23 else ""
# print(Halifax+str(m),"in Halifax")
# john = int(m)+30 if int(m)+30<=59 else int(m)+30-60
# john_time = h+1
# if int(m)+30 >= 60:
#     john_time+=1
# if john_time >= 24:
#     john_time-=24
# john_time = str(john_time) if 1<=john_time<=23 else ""
# print(f"{john_time}{john:0>2}","in St. John's")

# for i in range(one()):
#     a = int(inputing())
#     b = int(inputing())
#     if i != 0:
#         print()
#     print(a//b)
#     print(a%b)   
            
# for index in range(one()):
#     a = one()
#     n_dict = {}
#     for i in range(1,a//2+1):
#         if a%i == 0:
#             n_dict[i]=1
#     cnt = sum(list(n_dict.keys()))
#     if index != 0:
#         print()
#     if cnt == a:
#         print(a,"is a perfect number.")
#     else:
#         if cnt > a:
#             print(a,"is an abundant number.")
#         else:
#             print(a,"is a deficient number.")

# while True:
#     a = one()
#     if a == 0:
#         break
#     for i in range(1,a+1):
#         print("*"*i)

# while True:
#     a,b,c,d = wow()
#     if a==b==c==d==0:
#         break
#     if a == 0:
#         a = d//(b*c)
#     if b == 0:
#         b = d//(a*c)
#     if c == 0:
#         c = d//(a*b)
#     if d == 0:
#         d = a*b*c
#     print(a,b,c,d)

# for i in range(1,one()+1):
#     a,b = wow()
#     if a < 0:
#         if b<0:
#             a,b = abs(a),abs(b)-1
#             cnt = (a*(a+1)//2)-(b*(b+1)//2)
#             cnt*=-1
#         else:
#             if abs(a)>abs(b):
#                 a = abs(a)
#                 b = abs(b)
#                 cnt = (a*(a+1)//2) - (b*(b+1)//2)
#                 cnt*=-1
#             else:
#                 a = abs(a)
#                 cnt = (b*(b+1)//2) - (a*(a+1)//2)
#     else:
#         a = a-1 
#         cnt = (b*(b+1)//2) - (a*(a+1)//2) 
#     if i != 1:
#         print()
#     print(f"Scenario #{i}:")
#     print(cnt)
        
        















