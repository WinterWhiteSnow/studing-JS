import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# zero_list = [0,1,2,4]
# answer_list = []
# for _ in range(one()):
#     a = one()
#     answer_list.append(a)
# max_num = max(answer_list)
# while len(zero_list)<=max_num:
#     zero_list.append((zero_list[-1]+zero_list[-2]+zero_list[-3])%1000000009)
# for i in answer_list:
#     print(zero_list[i])

from itertools import combinations_with_replacement

number_list = [1,2,3]
for _ in range(one()):
    a = one()
    cnt = 1
    for i in range(1,a):
        b = [i for i in list(combinations_with_replacement(number_list,r=i)) if sum(i) == a]
        cnt+=len(b)
    print("answer:",cnt)






























