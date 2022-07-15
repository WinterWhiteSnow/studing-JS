import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# r,l = wow()
# n_list = [list(wow()) for _ in range(r)]
# t = one()
# list_list = []
# for i in range(r-2):
#     tem_list = []
#     # r_start = i
#     # r_end = i+2
#     for ll in range(l-2):
#         # l_start=ll
#         # l_end=ll+2
#         tem_list.extend(n_list[i][ll:ll+3])
#         tem_list.extend(n_list[i+1][ll:ll+3])
#         tem_list.extend(n_list[i+2][ll:ll+3])
#         # print(tem_list)
#         tem_list.sort()
#         list_list.append(tem_list[4])
#         tem_list=[]
#     # print(list_list)

# print(len([i for i in list_list if t<=i]))

# l = one()
# n_list = list(map(float,inputing().split()))
# n_list.sort()
# cnt = 0
# for i in range(l):
#     standard = i
#     start=standard
#     end=l-1
#     while start<=end:
#         mid = (start+end)//2
#         # print(start,end,mid)
#         if n_list[standard]<=n_list[mid] and n_list[standard]>=n_list[mid]*0.9:
#             start=mid+1
#         else:
#             end=mid-1
#     # print(start,end,mid,standard)
#     cnt+=end-standard
# print(cnt)

for _ in range(one()):
    x = one()
    x_list = list(wow())
    y = one()
    y_list = list(wow())
    z = one()
    z_list = list(wow())
    cnt = 0
    check_list = []
    for x in range(x):
        for y in range(y):
            for z in range(z):
                now = set(list(str(x+y+z)))
                if  now == {"5"} or now == {"8"} or now=={"5","8"}:
                    print(set(list(str(x+y+z))))
                    cnt+=1
    print(cnt)
        











