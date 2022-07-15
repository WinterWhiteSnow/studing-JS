import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

r,total = wow()
n_list = [one() for _ in range(r)]
z_list = [10001]*(total+1)
z_list[0]=0
for index in n_list:
    for i in range(index,total+1):
        if z_list[i-index] != 10001:
            z_list[i]=min(z_list[i],z_list[i-index]+1)
if z_list[total] == 10001:
    print(-1)
else:
    print(z_list[total])
    




    













