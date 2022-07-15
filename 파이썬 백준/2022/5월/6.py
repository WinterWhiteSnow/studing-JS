import sys
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())
# num = one()
# n_list = [0]*(num+1)
# n_list[1]=[1]
# for i in range(2,num+1):
#     if i%6 == 0:
#         wow_list = [len(n_list[i//3]+[n_list[i//3][-1]*3]),len(n_list[i//2]+[n_list[i//2][-1]*2]),len(n_list[i-1]+[n_list[i-1][-1]+1])]
#         if wow_list.index(min(wow_list)) == 0:
#             n_list[i] = n_list[i//3]+[n_list[i//3][-1]*3]
#         elif wow_list.index(min(wow_list)) == 1:
#             n_list[i] = n_list[i//2]+[n_list[i//2][-1]*2]
#         else:
#             n_list[i]=n_list[i-1]+[n_list[i-1][-1]+1]           
#     elif i%3 ==0:
#         if len(n_list[i//3]+[n_list[i//3][-1]*3])<=len(n_list[i-1]+[n_list[i-1][-1]+1]):
#             n_list[i] = n_list[i//3]+[n_list[i//3][-1]*3]
#         else:
#             n_list[i]=n_list[i-1]+[n_list[i-1][-1]+1]
#     elif i%2 ==0:
#         if len(n_list[i//2]+[n_list[i//2][-1]*2])<=len(n_list[i-1]+[n_list[i-1][-1]+1]):
#             n_list[i] = n_list[i//2]+[n_list[i//2][-1]*2]
#         else:
#             n_list[i]=n_list[i-1]+[n_list[i-1][-1]+1]
#     else:
#         n_list[i]=n_list[i-1]+[n_list[i-1][-1]+1]
# print(len(n_list[num])-1)
# print(*n_list[num][::-1])
# num = one()
# n_list= [0]*(num+1)
# for i in range(1,num+1):
#     if i == 1 or i==2 or i==3:
#         n_list[i]=1
#     else:
#         n_list[i]=n_list[i-1]+n_list[i-3]
# print(n_list[num])
   















