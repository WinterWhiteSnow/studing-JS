import sys
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# num = one()
# zero_list = [1*i for i in range(num+1)]
# zero_list[0]=1
# for i in range(1,num+1):
#     if int(i**(1/2))**2 == i:
#         zero_list[i]=1
#     else:
#         number= int(i**(1/2))
#         zero_list[i]=zero_list[i-1]+1
#         for index in range(2,number+1):
#             zero_list[i]=min(zero_list[i],zero_list[index**2]+zero_list[i-index**2])
# print(zero_list[num])

# r = one()
# n_list = [one() for _ in range(r)]
# zero_list = [0]*r
# zero_list[0]=n_list[0]
# next_chain = [0,1]
# if r>=3:
#     zero_list[1]=n_list[1]+zero_list[0]
#     # zero_list[2]=max(n_list[0]+n_list[2],n_list[1]+n_list[2])
#     for i in range(2,r):
#         if n_list[i] == 0:
#             zero_list[i]=max(zero_list[i-2]+n_list[i],zero_list[i-1],zero_list[i-3]+n_list[i-1]+n_list[i],zero_list[-1])      
#             next_chain.append(0)
#         else:
#             if next_chain[i-1] == 1:
#                 zero_list[i]=max(zero_list[i-2]+n_list[i],zero_list[i-1],zero_list[i-3]+n_list[i-1]+n_list[i])      
#                 next_chain.append(0)
#             else:
#                 zero_list[i]=max(zero_list[i-2]+n_list[i],zero_list[i-1],zero_list[i-3]+n_list[i-1]+n_list[i])            
#                 if zero_list[i] == zero_list[i-2]+n_list[i] or zero_list[i] == zero_list[i-1]:
#                     next_chain.append(0)
#                 else:
#                     next_chain.append(1)
#         # print(zero_list,next_chain)
#     print(max(zero_list))
# else:
#     print(sum(n_list))

num = one()
if num == 1:
    print(10)
else:
    n_list = [str(i).zfill(2) for i in range(10**(num))]
    print(n_list)













