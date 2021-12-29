# import sys
# from collections import deque
# a,b = map(int,sys.stdin.readline().rstrip().split())
# total = a*b
# wow = sys.stdin.readline().rstrip().split()
# for i in wow:
#     print(int(i)-total,end=" ")

# import string
# import sys
# wow = list(i for i in string.ascii_lowercase)
# dict_list = {}
# for i in range(1,len(wow)+1):
#     dict_list[wow[i-1]]=i

# the_num = int(sys.stdin.readline().rstrip())
# the_str = list(sys.stdin.readline().rstrip())
# count = 0
# if len(the_str) == the_num:
#     for i in range(the_num):
#         count+=(dict_list[the_str[i]])*(31**i)
#     print(count)

import sys
from collections import deque
Tree,M = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()
mini = a[0]
maxi = a[-1]
if len(a) == Tree:
    o = 0
    while True:
        # print("시작",mini,maxi)
        limit = (mini+maxi)//2
        for i in a:
            if i >= limit:
                s=i-limit
                o+=s
                # print("for",o,limit)
        # print("작업끝",o,limit)
        if o == M:    
            print(limit)
            break
        elif o < M :
            if o+1 ==M:
                if limit > 1:
                    print(limit-1)
                    break
                else:
                    print(limit+1)
                    break
            else:
                maxi = limit-1
                o = 0
                # print("o<M",mini,maxi,limit)
        elif o > M:
            else:
                mini = limit+1
                o = 0
                # print("o>M",mini,maxi,limit)
# 예시 1 : 2 3 / 2 2 answer = 2 (1을더해줘야함)
# 예시 2 : 2 5 / 7 9 answer = 5 (1을빼줘야함)