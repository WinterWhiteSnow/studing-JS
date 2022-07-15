# r = lambda :map(int,input().split())
# team,broken,add = r()
# broken_list = list(r())
# add_list = list(r())
# for i in add_list:
#     if i in broken_list:
#         broken_list.remove(broken_list[broken_list.index(i)])
#     elif i-1 in broken_list:
#         broken_list.remove(broken_list[broken_list.index(i-1)])
#     elif i+1 in broken_list:
#         broken_list.remove(broken_list[broken_list.index(i+1)])
# print(len(broken_list))

# n = input()
# if set(n) == {"N"}:
#     print(0)
# else:
#     gap = 0
#     cnt = 0
#     index_list = []
#     index= n.index("Y")
#     n = list(n)
#     if index == 0:
#         index_list.append(index)
#         for i in range(len(n)):
#             if n[i] == "Y":
#                 n[i]="N"
#             else:
#                 n[i]="Y"
#         cnt+=1
#         index+=1
#     while set(n) != {"N"}:
#         cnt+=1  
#         index= n.index("Y")
#         if index not in index_list:
#             index_list.append(index)
#             for i in range(index,len(n),index+1):
#                 if n[i] == "Y":
#                     n[i]="N"
#                 else:
#                     n[i]="Y"
#         else:
#             print(-1)
#             exit()              
#         if set(n) == {"N"}:
#             break
#     print(cnt)
# r = lambda : map(int,input().split())
# burger,side,juice = r()
# burger_list = list(r())
# side_list = list(r())
# juice_list = list(r())
# burger_list.sort(reverse=True)
# side_list.sort(reverse=True)
# juice_list.sort(reverse=True)
# total_list = []
# cnt = 0
# mini = min(len(burger_list),len(juice_list),len(side_list))
# for i in range(mini):
#     total_list.append((burger_list[i]+side_list[i]+juice_list[i])*0.9)
# if len(burger_list) > mini:
#     cnt+=sum(burger_list[mini:]) 
# if len(side_list) > mini:
#     cnt+=sum(side_list[mini:]) 
# if len(juice_list) > mini:
#     cnt+=sum(juice_list[mini:]) 
# print(sum(burger_list)+sum(juice_list)+sum(side_list))
# print(int(sum(total_list)+cnt))
# l = int(input())
# a_list = list(map(int,input().split()))
# jun = a_list[0]
# a_list = a_list[1:]
# a_list.sort()
# for i in a_list:
#     if i < jun:
#         jun+=i
#     else:
#         print("No")
#         exit()
# print("Yes")  

          
        
    
