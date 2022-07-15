import sys


inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# num = float(inputing())*1609.344/1000
# a = 3.785411784
# index = 100/num
# print(a*index)

# n_list = [one() for _ in range(3)]
# cnt = 10001
# for i in range(3):
#     count = 0
#     for a in range(3):
#         count+=n_list[a]*2*abs(i-a)
#     # print(cnt,count)
#     cnt = min(cnt,count)

# print(cnt)

# next =one()
# limit = one()
# if next <= limit+60:
#     print(next*1500)
# else:
#     print((next-(60+limit))*3000+(60+limit)*1500)

# n_list = list(wow())
# if n_list.count(1) > n_list.count(2):
#     print(1)
# else:
#     print(2)

# l = one()
# str_str = list(inputing())
# str_list = ["a", "i", "u", "e", "o"]
# cnt = 0
# for i in str_str:
#     if i in str_list:
#         cnt+=1
# print(cnt)

# n_list = list(wow())
# n_list.sort()
# print(n_list[-1]+n_list[-2])

# x,l,r = wow()
# n_list = [i for i in range(l,r+1)]
# n_list.sort(key= lambda y : abs(x-y))
# print(n_list[0])

# n_list = [one() for _ in range(3)]
# cnt = 0
# for i in range(1,4):
#     cnt+=n_list[i-1]*i
# if cnt >= 10:
#     print("happy")
# else:
#     print("sad")

# n_dict = {}
# for i in sys.stdin.readlines():
#     a,b = i.lstrip().split(":")
#     n_dict[a]=b.replace("\n","")
# print(n_dict)
# n_dict = {'1995': ' ITMO', '1996': ' SPbSU', '1997': ' SPbSU', '1998': ' ITMO', '1999': ' ITMO', '2000': 
# ' SPbSU', '2001': ' ITMO', '2002': ' ITMO', '2003': ' ITMO', '2004': ' ITMO', '2005': ' ITMO', '2006': ' PetrSU, ITMO', 
# '2007': ' SPbSU', '2008': ' SPbSU', '2009': ' ITMO', '2010': ' ITMO', '2011': ' ITMO', '2012': ' ITMO', '2013': ' SPbSU', '2014': ' ITMO', '2015': ' ITMO', '2016': ' ITMO', '2017': ' ITMO', '2018': ' SPbSU', '2019': 
# ' ITMO'}
# print(n_dict[inputing()].lstrip())

# a = one()
# b = one()
# x = one()
# y = one()
# t = one()
# a_cnt = a if t <= 30 else (t-30)*b*21+a
# b_cnt = x if t<=45 else (t-45)*y*21+x
# print(a_cnt,b_cnt)

# A,C,E = wow()
# a,c,e = wow()
# if c>=C and a>=A:
#     print("A")
# elif c>=C and a>=A/2:
#     print("B")
# elif c>=C:
#     print("C")
# elif c>=C/2:
#     print("D")
# else:
#     print("E")

# num = one()
# print(num**(1/2)*4)

# total,auto,step = list(map(float,inputing().split()))
# left_start,right_start = list(map(float,inputing().split()))
# now_left,now_right = list(map(float,inputing().split()))

# l_cnt = 1/left_start*now_left+total/step
# r_cnt = 1/right_start*now_right+total/auto
# if l_cnt > r_cnt:
#     print("latmask")
# else:
#     print("friskus")
# import math
# num=(one())**(1/2)
# print(num*2*math.pi)
# import math
# num = (one()/math.pi)**(1/2)
# print(2*num*math.pi)

# c = one()
# coke,beer = wow()
# print(min(coke//2+beer,c))

# a = inputing()
# if a == "N" or a == "n":
#     print("Naver D2")
# else:
#     print("Naver Whale")

# apple,pear = wow()
# print("Axel" if apple*7>pear*13 else "lika" if apple*7 == pear*13 else "Petra" )

# a,b,x,y = wow()
# print(1 if a-2>=x and b-2>=y else 0)

# for _ in range(one()):
#     print("SciComLove")

# temp = one()
# print(5*temp-400)
# if temp < 100:
#     print(1)
# elif temp == 100:
#     print(0)
# else:
#     print(-1)

# num = one()
# index = 25+num*0.01
# if index < 100:
#     index = 100
# elif index > 2000:
#     index = 2000
# print(f"{index:.2f}")

# a,b = wow()
# print(1 if a == 0 and b!=0 else min(a+1,b))

# a,b,c = wow()
# max_max = max(a,b,c)
# print(max_max*3-a-b-c)

# index = 1
# while True:
#     a = inputing()
#     if a == "0":
#         break
#     print(f"Case {index}: Sorting... done!")
#     index+=1

# a,b,c = wow()
# print(1 if a<=c<b else 0)

# a,b = wow()
# print(max(a+b,a-b))
# print(min(a+b,a-b))

# n_list = [one() for _ in range(3)]
# print(1 if n_list[0]+n_list[1]<=n_list[2] else 0)

# a = one()
# b = one()
# c = (a+b)%12
# print(c if c != 0 else 12)














