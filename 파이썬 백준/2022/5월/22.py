import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# r,l = wow()
# garo_dict = {} # 정면
# sero_dict = {} # 측면
# for sero in range(r):
#     a = list(wow())
#     for garo in range(l):
#         if garo not in garo_dict:
#             garo_dict[garo]=[a[garo]]
#         else:
#             garo_dict[garo]+=[a[garo]]   
#     sero_dict[sero]=a
# sero_max = {} #측면 최댓값
# for i in range(r):
#     index = sero_dict[i].index(max(sero_dict[i]))
#     if index not in sero_max:
#         sero_max[index]=[max(sero_dict[i])]
#     else:
#         sero_max[index]+=[max(sero_dict[i])]
# # print(sero_max)
# cnt = 0
# for garo in range(l):
#     # print(garo_dict[garo])
#     pass_list = [max(garo_dict[garo])]
#     if garo in sero_max:
#         pass_list+=sero_max[garo]
#     cnt+=sum(garo_dict[garo])-sum(list(set(pass_list)))
# print(cnt)

for _ in range(one()):
    a = one()
    a_str = list(str(a))
    
    




































