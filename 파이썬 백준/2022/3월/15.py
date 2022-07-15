# n = int(input())
# n_list = [0,0,1,3]
# cnt = 0
# while n > 3:
#     cnt+=(n-2)*2+1
#     n = n-2
# print(cnt+n_list[n])

# money, year = map(int,input().split())
# n_list = [0]*(year+1)
# n_list[0] = money
# for i in range(1,year+1):
#     if i >= 5:
#         n_list[i]=int(max(n_list[i-1]*1.05,n_list[i-3]*1.2,n_list[i-5]*1.35))
#     elif i>=3:
#         n_list[i]=int(max(n_list[i-1]*1.05,n_list[i-3]*1.2))
#     else:
#         n_list[i]=int(n_list[i-1]*1.05)
#     # print(n_list)
# print(n_list[year])

# for _ in range(int(input())):
#     not_list = []
#     a,b = input().split()
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             not_list.append(a[i])
#     x = not_list.count("1")
#     y = not_list.count("0")
#     print(max(x,y))   

# n = int(input())
# n_list = list(map(int,input().split()))
# n_list.sort()
# cnt=0
# for i in n_list:
#     cnt+=i*n
#     n-=1
# print(cnt)

r,total = map(int,input().split())
n_list = [int(input()) for i in range(r)]
for i in range(len(n_list)):
    if n_list[i] >= total:
        if n_list[i] > total:
            n_list = n_list[:i]
        else:
            n_list = n_list[:i+1]
        break
n_list.sort(reverse=True)
cnt = 0
for i in n_list:
    if total//i > 0:
        cnt+=total//i
        total=total%i
    if total == 0:
        break
print(cnt)
        


