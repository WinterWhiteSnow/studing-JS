import sys
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# l = one()
# n_list = list(wow())
# zero_list = [0]*(l)
# for i in range(l):
#     zero_list[i]=n_list[i]
# for i in range(1,l):
#     for index in range(0,i):
#         # print(n_list[i],n_list[index])
#         if n_list[i] > n_list[index]:
#             zero_list[i]=max(zero_list[i],zero_list[index]+n_list[i])
# print(max(zero_list))

# l = one()
# n_list = list(wow())
# n_list = n_list[::-1]
# zero_list = [1]*l
# for i in range(1,l):
#     for index in range(0,i):
#         if n_list[i]>n_list[index]:
#             zero_list[i]=max(zero_list[i],zero_list[index]+1)
# print(max(zero_list))

l = one()
n_list = list(wow())
zero_list = [n_list[0]]
for i in range(1,l):
    if zero_list[-1] < n_list[i]:
        zero_list.append(n_list[i])
    else:
        start=0
        end=len(zero_list)-1
        while start<=end:
            mid = (start+end)//2
            if zero_list[mid]>n_list[i]:
                



















