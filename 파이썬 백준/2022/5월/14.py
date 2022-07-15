import sys
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# num = one()
# result=0
# n_list=[i for i in range(1,num+1)]
# end=0
# summary = 0
# for start in range(num):
#     while True:
#         if summary<num and end<num:
#             summary+=n_list[end]
#             end+=1
#         else:
#             break
#     # print("end!!",end,summary,result)
#     if summary==num:
#         result+=1
#     summary-=n_list[start]
#     # print("total",start,end,summary,result)
# print(result)

# l,k=wow()
# n_list = list(wow())
# rion_list = []
# if n_list.count(1)>=k:
#     result = l 
#     for start in range(l):
#         if n_list[start] == 1:
#             rion_list.append(start)
#     if len(rion_list)>k:
#         for i in range(len(rion_list)-k+1):
#             result = min(result,rion_list[i+k-1]-rion_list[i]+1)
#         print(result)
#     else:
#         print(rion_list[-1]-rion_list[0]+1)        
# else:
#     print(-1)

l,day = wow()
n_list = list(wow())
result = sum(n_list[:day])
for start in range(l-day):
    end=start+day
    result = max(result,result-n_list[start]+n_list[end])
    print(result,start,end)
















