import sys
insert = lambda : sys.stdin.readline().rstrip().split()
wow = lambda : map(int,insert())
one = lambda : int(sys.stdin.readline().rstrip())

# r,k = wow()
# n_list = [one() for _ in range(r)]
# start = 1
# end = max(n_list)
# while start<=end:
#     mid = (start+end)//2
#     remainder = k
#     for index in n_list:
#         if index < mid:
#             remainder-=(mid-index)
#     # print(start,mid,end,remainder)
#     if remainder < 0:
#         end=mid-1
#     else:
#         start=mid+1
# print(end)       

# r,person = wow()
# n_list = [one() for _ in range(r)]
# start = 1
# end = max(n_list)
# if end == 0:
#     print(0)
# else:
#     while start<=end:
#         mid = (start+end)//2
#         cnt = 0
#         for index in n_list:
#             cnt+=index//mid
#         if cnt < person:
#             end = mid-1
#         else:
#             start = mid+1
#     print(end)

# for _ in range(one()):
#     a = one()
#     start = 1
#     end = a
#     while start<=end:
#         mid = (start+end)//2
#         num = mid*(mid+1)//2
#         # print(start,mid,end,num)
#         if num <=a:
#             start=mid+1
#         else:
#             end=mid-1
#     print(end)

# r,total = wow()
# n_list = [one() for _ in range(r)]
# start = 1
# end = max(n_list)
# while start<=end:
#     mid = (start + end)//2
#     if mid == 0:
#         break
#     cnt = 0
#     for index in n_list:
#         cnt+=index//mid
#     # print(start,mid,end,cnt)
#     if cnt < total:
#         end=mid-1
#     else:
#         start=mid+1
# count = 0
# remainder = 0
# n_list.sort()
# # print(start,mid,end,cnt)
# if end == 0:
#     print(count)
# else:
#     for i in n_list:
#         if count < total:
#             count+=i//end
#             if count > total:
#                 remainder+=(count-total)*end
#             remainder+=i%end
#         else:
#             remainder+=index
#     print(remainder)
l = one()
n_list = list(wow())
n_list.sort()
max_num = n_list[0]+n_list[-1]
start = 0
end = l-1
start_num = n_list[0]
end_num = n_list[-1]
while start!=end:
    mid = (start+end)//2
    print(start,mid,end,"start:",n_list[start],"end:",n_list[end])
    if n_list[start]+n_list[end] == 0:
        start_num=n_list[start]
        end_num = n_list[end]
        break    
    else:
        if abs(n_list[start] + n_list[end]) <abs(max_num):
            start_num=n_list[start]
            end_num = n_list[end]
        if n_list[start] + n_list[end] < 0:
            start=mid
        else:
            end=mid
print(start_num,end_num)
    













