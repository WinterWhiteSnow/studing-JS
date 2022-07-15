import sys
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

r = one()
n_list = [one() for _ in range(r)]
zero_list = [0]*r
zero_list[0]=n_list[0]
if r>=3:
    repeat=0
    zero_list[1]=n_list[1]+zero_list[0]
    zero_list[2]=max(n_list[0]+n_list[2],n_list[1]+n_list[2])
    repeat=0
    repeat_list=[0,1]
    for i in range(3,r-1):
        zero_list[i]=max(zero_list[i-2]+n_list[i],n_list[i-1]+zero_list[i-3]+n_list[i])
    print(max(zero_list))
else:
    print(sum(n_list))
# l = one()
# n_list = list(wow())
# zero_list = [0]*l
# zero_list[0]=n_list[0]
# for i in range(1,l):
#     zero_list[i]=max(n_list[i]+n_list[i-1],zero_list[i-1]+n_list[i],n_list[i])
# print(max(zero_list))

















