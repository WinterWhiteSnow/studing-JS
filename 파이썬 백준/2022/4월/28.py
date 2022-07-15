# import sys
# num = int(sys.stdin.readline().rstrip())
# n_list = list(map(int,sys.stdin.readline().rstrip().split()))
# total = int(sys.stdin.readline().rstrip())
# if sum(n_list) <= total:
#     print(max(n_list))
# else:
#     n_list.sort()
#     start = n_list[0]
#     end = n_list[-1]
#     while start<=end:
#         cnt = 0
#         mid = (start+end)//2
#         for i in n_list:
#             cnt+=min(mid,i)
#         if cnt > total:
#             end = mid-1
#         else:
#             start = mid+1
#     count = 0
#     for i in n_list:
#         count+=min(end,i)
#     if count > total:
#         print(total//num)
#     else:
#         print(end)

total,win = map(int,input().split())
a = 100*win//total
if a>=99:
    print(-1)
else:
    start = 1
    end = 1000000000
    while start<=end:
        mid = (start+end)//2
        wow = 100*(win+mid)//(total+mid)
        if wow > a:
            end = mid-1
        else:
            start = mid+1
        # print(start,end,mid,wow,a)
    print(start)










