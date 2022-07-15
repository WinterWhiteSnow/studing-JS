# r = lambda : map(int,input().split())
# location, l = r()
# location_list = list(r())
# location_list.sort()
# cnt = 1
# for i in range(len(location_list)):
#     if i == 0:
#         start = location_list[i]
#     else:
#         if location_list[i]-start >= l:
#             cnt+=1
#             start = location_list[i]
# print(cnt)
# import sys
# r = lambda : int(sys.stdin.readline().rstrip())
# n_list = [r() for _ in range(r())]
# n_list.sort()
# # print(n_list)
# cnt = 0
# gap = 1
# for i in range(len(n_list)):
#     cnt+=abs(n_list[i]-gap)
#     gap+=1
# print(cnt)
# import sys
# l = int(sys.stdin.readline().rstrip())
# n_list = list(map(int,sys.stdin.readline().rstrip().split()))
# n_list.sort()
# if len(n_list)%2 == 0:
#     index = len(n_list)//2-1
# else:
#     index = len(n_list)//2
# print(n_list[index])

# n,m = map(int,input().split())
# j = int(input())
# n_list = []
# for _ in range(j):
#     n_list.append(int(input()))
# cnt = 0
# start = 1
# end = m
# for i in range(len(n_list)):
#     # print("변경전",start,end,"cnt",cnt)
#     if start <= n_list[i] <= end:
#         pass
#     else:
#         if n_list[i] > end:    
#             cnt+=n_list[i]-end
#             end+=n_list[i]-end
#             start = end-(m-1)
#         else:
#             cnt+=start-n_list[i]
#             start = n_list[i]
#             end = start+(m-1)
#     # print("변경후",start,end,"cnt",cnt)
# print(cnt)

l,k=map(int,input().split())
n_list = list(input())
cnt = 0
for i in range(len(n_list)):
    if n_list[i] == "P":
        print(i,k)
        if i-k < 0:
            index = 0
        else:
            index=i-k
        if "H" in n_list[index:i+1]:
            print(n_list[index:i+1],n_list[index:i+1].index("H"))
            cnt+=1
            n_list[n_list[index:i+1].index("H")]="E"
            n_list[i]="W"
        else:
            if i+k+1 > len(n_list):
                index = len(n_list)
            else:
                index = i+k+1
            if "H" in n_list[i:index]:
                print(n_list[i:index],n_list[i:index].index("H"))
                cnt+=1
                n_list[n_list[i:index].index("H")]="E"
                n_list[i]="W"
print(cnt)
        
        
    
