import sys
wow = lambda : map(int,sys.stdin.readline().rstrip().split())
one = lambda : int(sys.stdin.readline().rstrip())
# mark,r = wow()
# n_list = []
# for index in range(mark):
#     name,score = sys.stdin.readline().rstrip().split()
#     score = int(score)
#     n_list.append((name,score,index))
# n_list.sort(key=lambda x : (x[1],x[2]))
# for _ in range(r):
#     num = one()
#     start = 0
#     end = mark-1
#     while start<=end:
#         mid = (start+end)//2
#         # if n_list[mid][1] == num:
#         #     start = mid
#         #     break
#         if n_list[mid][1] >= num:
#             end = mid-1
#         else:
#             start = mid+1
#         # print(start,end,mid)
#     print(n_list[start][0])
# a,b = wow()
# n_list = []
# for _ in range(a):
#     n_list.append(one())
# n_list.sort()
# for _ in range(b):
#     num = one()
#     start = 0
#     end = a-1
#     while start<=end:
#         mid = (start+end)//2
#         if n_list[mid] < num:
#             start=mid+1
#         else:
#             end=mid-1
#         # print(start,mid,end,n_list)
#     print(start if start<a and n_list[start] == num else -1)
import math
total,l,w,h = wow()
if total == 1:
    print(float(min(l,w,h)))
else:
    start = 1
    end = max(l,w,h)
    while start<=end:
        mid = (start+end)/2
        cnt = (l*w*h)//mid**3
        if start==mid:
            break
        if cnt < total:
            end=mid
        else:
            start = mid
        # print(start,mid,end,cnt)
    if cnt == total:
        print(mid)
    else:
        print(end)


















