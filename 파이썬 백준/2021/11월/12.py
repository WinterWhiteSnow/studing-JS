# a = input().split()
# start = int(a[0])
# end = int(a[1])
# def wow (potato,tomato):
#     a = [potato,tomato]
#     x = potato
#     y = tomato
#     a.sort()
#     greatest = 1
#     for i in range(2,a[-1]+1):
#         while True:
#             if x % i == 0 and y % i == 0:
#                 x = x//i
#                 y = y//i
#                 greatest*=i
#             else:
#                 break    
#     return greatest,greatest*x*y
# wow_wow = wow(start,end)
# print(wow_wow[0])
# print(wow_wow[1])
# 백준 기준 33471위

# a = [int(i) for i in input().split()]
# length = a[0]
# th = a[1]
# if length%2 != 0:
#     max_num = length//2+1
# else:
#     max_num = length//2
# count = 0
# a_list = []
# for i in range(length):
#     a = i+1
#     if a > max_num:
#         a = max_num - (a-max_num)
#     a_list.append(a)
# print(max_num , a_list)

# a = [int(i) for i in input().split()]
# length = a[0]+1
# th = a[1]
# a_dict = {}
# for i in range(1,length+1):
# 	a_dict[i] = []
# 	for b in range(1,i+1):
# 		if b == 1 or b == i:
# 			a_dict[i].append(1)
# 		elif 1<b<i: # i = 3 / b = 2
# 			a_dict[i].append(a_dict[i-1][b-2]+a_dict[i-1][b-1])
# print(a_dict[length][th])
# 백준 기준 33033위, solved기준 21403위

a = int(input())
a_a = [int(i) for i in input().split()]

 
b = int(input())
b_b = [int(i) for i in input().split()]

 
for i in b_b:
    if i in a_a:
        print(1)
    else:
        print(0)