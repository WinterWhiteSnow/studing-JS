import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())
# from itertools import permutations
# a,b = inputing().split()
# b = int(b)
# a = list(map(int,list(a)))
# list_list = list(permutations(a,r=len(a)))
# list_list.sort()
# start=0
# end=len(list_list)-1
# while start<=end:
#     mid = (start+end)//2
#     if int("".join(list(map(str,list_list[mid])))) < b:
#         start=mid+1
#     else:
#         end=mid-1
#     # print(list_list[mid])
# answer = "".join(list(map(str,list_list[end])))
# if answer[0] == "0":
#     print(-1)
# else:
#     if int(answer) > b:
#         print(-1)
#     else:
#         print(answer)

# from itertools import combinations_with_replacement

# num = [1,5,10,50]
# list_list = list(combinations_with_replacement(num,r=one()))
# a_dict = {}
# for i in list_list:
#     a_dict[sum(i)]=1
# print(len(a_dict.keys()))

n,m = wow()
n_list = [one() for _ in range(n)]
start = 0
end = 1000000
while start<=end:
    count = 0
    mid = (start+end)//2
    cnt = 0
    for i in n_list:
        if cnt+i <= mid:
            cnt+=i
        else:
            cnt = i
            count+=1
        # print(cnt,count)
    # print(start,end,mid)
    if cnt != 0:
        count+=1
        cnt=0
    print(cnt,count,mid)
    if count >= m:
        start = mid+1
    else:
        end = mid-1
print(end)























