import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# test = one()
# for _ in range(test):
#     l = one()
#     n_list = list(wow())
#     total = 0
#     maxi = n_list[-1]
#     for i in range(l-2,-1,-1):
#         if n_list[i] < maxi:
#             total+=maxi-n_list[i]
#         else:
#             maxi = n_list[i]
#     print(total)
            
# l = one()
# n_list = list(wow())
# n_list.sort()
# if len(n_list)%2 == 0:
#     start=0
#     end = len(n_list)-1
#     maxi = n_list[0]+n_list[-1]
# else:
#     start=0
#     end = len(n_list)-2
#     maxi = n_list[0]+n_list[-2]
# while start<end:
#     maxi = max(maxi,n_list[start]+n_list[end])
#     start+=1
#     end-=1
# print(maxi)


        
    
            




































