# import sys
# a = sys.stdin.readline()
# aa = set(sys.stdin.readline().rstrip().split(" "))
# b = sys.stdin.readline()
# bb = sys.stdin.readline().rstrip().split(" ")

# for i in bb:
#     if i in aa:
#         print(1)
#     else:
#         print(0)

# a = int(input())
# a_list = []
# for i in range(a):
#     a,b = map(int, input().split())
#     a_list.append([a,b])
# b_list = sorted(a_list, key = lambda x : x[1])
# b_list = sorted(b_list, key = lambda x : x[0])
# for i in b_list:
#     print(i[0],i[1])

# the_num = int(input())
# a_list = []
# for i in range(the_num):
#     a = input().split()
#     a[0] = int(a[0])
#     a.append(i)
#     a_list.append(a)
# a = sorted(a_list, key= lambda x : x[2])
# a = sorted(a, key= lambda x : x[0])
# for i in a:
#     print(i[0],i[1])
# 백준기준 31923위

import sys

a = sys.stdin.readline().rstrip().split()
start = int(a[0])
jump = int(a[1])
count =0
a_list = []
while True:
    count+=1
    if jump*count < start:
        if jump*count not in a_list:
            a_list.append(jump*count)
            a_list.append(start-jump*count)
    else:
        jump=jump-1
        count = 0





    