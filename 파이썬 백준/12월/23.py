# import sys

# a = int(sys.stdin.readline().rstrip())

# for _ in range(a):
#     start, end = map(int, sys.stdin.readline().rstrip().split())
#     gap = end-start
#     repeat = 1
#     plus = 2 # repeat =2 될때마다 +1
#     move = 3 # 할때마다 1씩
#     maxi = 4 # puls만큼 더해줌
#     if gap < 3:
#         move = gap
#     else: # gap 4부터
#         while gap > maxi:
#             repeat+=1
#             maxi+=plus
#             move+=1
#             if repeat == 2:
#                 repeat=0
#                 plus+=1
#     print(move)        

import sys
# 1은 소수가 아닙니다.
num_len = int(sys.stdin.readline().rstrip())
num_list = [int(i) for i in sys.stdin.readline().rstrip().split()]
dict_list = {}
for i in range(2,1001):
	if i not in dict_list:
		for a in range(i,1001,i):
			dict_list[a]=0
		dict_list[i]=1
if len(num_list) == num_len:
    count=0
    for i in num_list:
        if i == 1:
            pass
        elif dict_list[i] == 1:
            count+=1
    print(count)
