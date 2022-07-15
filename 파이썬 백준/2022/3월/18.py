# topping_sort = int(input())
# dough_price,topping_price= map(int,input().split())
# dough_k = int(input())
# dough_avarage = int(dough_k/dough_price)
# topping_list = [int(input()) for _ in range(topping_sort)]
# wow = dough_avarage
# topping_list.sort(reverse=True)
# for i in range(topping_sort):
#     if int((dough_k+sum(topping_list[:i+1]))/(dough_price+topping_price*len(topping_list[:i+1]))) >= wow:
#        wow = int((dough_k+sum(topping_list[:i+1]))/(dough_price+topping_price*len(topping_list[:i+1])))
#     else:
#         break
# print(wow)

# now,goal = map(int,input().split())
# book_mark = int(input())
# book_list = []
# for _ in range(book_mark):
#     book_list.append(int(input()))
# book_list.sort()
# gap = abs(goal-now)
# number = "wow"
# for i in range(book_mark):
#     if abs(goal-book_list[i]) < gap:
#         gap = abs(goal-book_list[i])
#         number = i
#     else:
#         pass
# if type(number) == int:
#     print(1+abs(goal-book_list[number]))
# else:
#     print(abs(goal-now))

# l = int(input())
# n_list = list(map(int,input().split()))
# n_list.sort()
# total = n_list[-1]
# for i in n_list[:-1]:
#     total+=i/2
# print(total)

# l = int(input())
# n_list = list(map(int,input().split()))
# n_list.sort()
# level = n_list[-1]
# n_list = n_list[:-1]
# print(len(n_list)*level+sum(n_list))



