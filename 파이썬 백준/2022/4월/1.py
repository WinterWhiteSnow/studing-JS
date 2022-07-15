# from collections import deque

# n = int(input())
# n_list = list(map(int,input().split()))
# n_list.sort()
# wow = deque([])
# while len(n_list) != 0:
#     direction = "left-right"
#     if len(n_list) == 1:
#         num = n_list.pop()
#         if abs(wow[0]-num) >= abs(wow[-1]-num):
#             wow.appendleft(num)
#         else:
#             wow.append(num)
#     else:
#         maxi = n_list.pop()
#         n_list = n_list[::-1] #내림차순
#         mini = n_list.pop()#현재 내림차순 상태
#         if direction == "left-right":
#             wow.appendleft(maxi)
#             wow.append(mini)
#             direction = "right-left"
#         else:
#             wow.append(maxi)
#             wow.appendleft(mini)
#             direction = "left-right"
# wow = list(wow)
# cnt = 0
# for i in range(n-1):
#     list_list = wow[i:i+2]
#     cnt+=abs(list_list[0]-list_list[1])
# print(cnt)

# n = int(input())
# sosu_dict = {}
# for i in range(2,1005001):
#     if i not in sosu_dict:
#         for a in range(i,1005001,i):
#             sosu_dict[a]=0
#         sosu_dict[i]=1
# sosu_list = [str(key) for key,value in sosu_dict.items() if value == 1 and key >= n]
# num = 0            
# for number in sosu_list:
#     index = len(number)//2
#     if num == 0:
#         if len(number)%2 == 0:
#             if number[:index][::-1] == number[index:]:
#                 num = number
#                 # print(number,number[:index],number[index:])
#         else:
#             if number[:index+1][::-1] == number[index:]:
#                 num = number
#                 # print(number,number[:index+1],number[index:])
#     else:
#         break
# print(num)
            
    
    


    
    


    







