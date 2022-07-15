import sys
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


# r = one()
# n_list = [1,1,1,2,2]
# answer_list=[]
# for _ in range(r):
#     answer_list.append(one())
# total= max(answer_list)
# for i in range(5,total+1):
#     n_list.append(n_list[i-1]+n_list[i-5])
# for i in answer_list:
#     print(n_list[i-1])
num = one()
n_list=[]
for _ in range(num):
    n_list.append(list(wow()))
zero_list=[0]*(num+1)
for i in range(1,num+1):
    










