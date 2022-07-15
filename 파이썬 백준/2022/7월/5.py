import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n_list = list(wow())
# n_list.sort()
# a = n_list[0]
# b = n_list[1]
# c = n_list[2]
# if a+b <= c:
#     c = a+b-1
# print(a+b+c)

p,l = wow()
n_list = list(wow())
cnt = 0
for i in n_list:
    if i%2:
        cnt+=i//2+1
    else:
        cnt+=i//2
if p <= cnt:
    print("YES")
else:
    print("NO")











