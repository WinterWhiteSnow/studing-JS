import sys
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# days = one()
# n_list = [list(wow()) for _ in range(days)]
# zero_list = [0]*days
# max_pay = 0
# for index in range(days-1,-1,-1):
#     aaa = n_list[index]
#     if aaa[0]+index <= days:
#         pay=aaa[1]
#     else:
#         pay=0
#     if pay != 0:
#         if index+aaa[0] < days:
#             pay+=max(zero_list[index+aaa[0]:])
#             # print(zero_list[index+aaa[0]:])
#     zero_list[index]=pay
#     # print("end!!",zero_list)
# print(max(zero_list))

n = one()
if n < 2:
    print(9)
else:
    













