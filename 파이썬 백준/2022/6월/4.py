import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# for i in sys.stdin:
#     str_str = i
#     while "BUG" in str_str: 
#         str_str = str_str.replace("BUG","")
#     print(str_str.rstrip())
n = one()
n_list =[0,1,1,2]
while len(n_list) <= n:
    n_list.append(n_list[-1]+n_list[-2])
    # print(n_list)
print(n_list[n])












