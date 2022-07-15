import sys


inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# while True:
#     r = one()
#     time = 0
#     cnt = 0
#     if r ==-1:
#         break
#     for _ in range(r):
#         a,b = wow()
#         if time == 0:
#             cnt+=a*b
#         else:
#             cnt+=(b-time)*a
#         time=b
#     print(cnt,"miles")

# while True:
#     a = float(inputing())
#     if a == 0:
#         break
#     cnt = 0
#     index = 2
#     while cnt <a:
#         cnt+=1/index
#         index+=1
#     print(index-2,"card(s)")

# while True:
#     a = float(inputing())
#     if a <= 0:
#         break
#     b = a*0.167
#     print(f"Objects weighing {a:.2f} on Earth will weigh {b:.2f} on the moon.")

# for i in sys.stdin.readlines():
#     r,w,d,total = map(int,i.split())
#     cnt = (r*(r-1)//2)*w
#     if cnt == total:
#         print(r)
#     else:
#         print((cnt-total)//d)

# while True:
#     n_list = sorted(list(wow()))
#     if sum(n_list)== 0:
#         break
#     answer = sum(n_list[1:-1])/4
#     if answer == int(answer):
#         print(int(answer))
#     else:
#         print(answer)

# while True:
#     a = one()
#     if a == 0:
#         break
#     b = 1
#     for i in range(1,a):
#         b+=2*i
#     print(f"{a} => {b}")

# while True:
#     a,b = inputing().split()
#     x,y = map(int,a.split(":"))
#     a_time = 60*60*x+60*y
#     x,y = map(int,b.split(":"))
#     b_time = 60*60*x+60*y
#     if a_time==b_time==0:
#         break
#     n = (a_time+b_time)//86400
#     time = (a_time+b_time)%86400
#     h = time//3600
#     m = (time-3600*h)//60
#     if n>=1:
#         print(f"{h:0>2}:{m:0>2}",f"+{n}")
#     else:
#         print(f"{h:0>2}:{m:0>2}")kkk

# while True:
#     start,d,num = wow()
#     if start==d==num==0:
#         break
#     if d>0:
#         if start<=num:
#             if (num-start)%d == 0:
#                 print((num-start)//d+1)
#             else:
#                 print("X")
#         else:
#             print("X")
#     else:
#         if start>=num:
#             if (num-start)%d == 0:
#                 print((num-start)//d+1)
#             else:
#                 print("X")
#         else:
#             print("X")

# while True:
#     a,b = wow()
#     if a==b==0:
#         break
#     c = a-b
#     cnt = c//2
#     d = c%2
#     if d == 1:
#         if cnt >= 1:
#             print(cnt-1,1)
#         else:
#             print(0,0)
#     else:
#         print(cnt,0)
# import math
# r = one()
# for index in range(r):
#     r2,weight = map(float,inputing().split())
#     cnt = 0
#     for _ in range(int(r2)):
#         a = float(inputing())
#         cnt+=4/3*math.pi*(a**3)
#     cnt/=1000
#     print(f"Data Set {index+1}:")
#     if cnt >= weight:
#         print("Yes")
#     else:
#         print("No")
#     print()

# def progress(num):
#     n_list = []
#     n = num
#     while n!=0:
#         n_list.append(n%2)
#         n//=2
#     n_list = n_list[::-1]
#     return n_list

# for _ in range(one()):
#     a,b = wow()
#     if progress(a).count(1)%2 == b:
#         print("Valid")
#     else:
#         print("Corrupt")

# for _ in range(one()):
#     n_list = list(wow())[1:]
#     even = 0
#     odd = 0
#     for i in n_list:
#         if i%2 == 0:
#             even+=i
#         else:
#             odd+=i
#     if even==odd:
#         print("TIE")
#     else:
#         if even>odd:
#             print("EVEN")
#         else:
#             print("ODD")
# a = 0
# b = 0
# for _ in range(one()):
#     x,y = wow()
#     if x == y:
#         a+=x
#         b+=y
#     else:
#         if x>y:
#             a+=x+y
#         else:
#             b+=x+y
# print(a,b)

# for i in sys.stdin.readlines():
#     a,b = map(int,i.split())
#     cnt = a/b
#     print(f"{cnt:.2f}")
        
# while True:
#     r = one()
#     if r ==0:
#         break
#     n_list = inputing()
#     zero = n_list.count("0")
#     wan = n_list.count("1")
#     print(f"Mary won {zero} times and John won {wan} times")

# a,b = wow()
# def num_num(num):
#     n_list = []
#     for i in range(1,num//2+1):
#         if num%i==0:
#             n_list.append(i)
#     return n_list
# a_list = num_num(a)+[a]
# b_list = num_num(b)+[b]
# for i in a_list:
#     for index in b_list:
#         print(i,index)

# p,a,b,c,d = wow()
# max_max = max(a,b,c,d)
# n_list = [[1]]
# while True:
#     k_list = []
#     for i in n_list[-1]:
#         k_list.extend([i*p,i*p+1])
#     n_list.append(k_list)
#     if max(k_list)>=max_max:
#         break
# zero_list = []
# for i in n_list:
#     zero_list.extend(i)
# n_list = [a,b,c,d]
# n_dict = {}
# for num in n_list:
#     start = 0
#     end = len(zero_list)-1
#     while start<=end:
#         mid = (start+end)//2
#         if zero_list[mid]>num:
#             end=mid-1
#         else:
#             start=mid+1
#     cnt = 0
#     for x in range(end+1):
#         for y in range(end+1):
#             if x != y and zero_list[x]+zero_list[y]==num:
#                 cnt+=1
#     if cnt == 2:
#         print(1,end=" ")
#     else:
#         print(0,end=" ")

        

