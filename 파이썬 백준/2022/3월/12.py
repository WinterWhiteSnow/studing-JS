# goal = int(input())
# wow_list = [0]*(goal+1)
# cnt = 0
# def wow(n):
#     # print("wow",n,wow_list)
#     if n == 1 or n == 2:
#         return 1
#     if wow_list[n] != 0:
#         return wow_list[n]
#     wow_list[n]=wow(n-1)+wow(n-2)
#     return wow_list[n]
# print(wow(goal),goal-2)

# a = list(input())
# b = list(input())
# a_list = []

# for i in range(len(a)):
#     a_list.append(int(a[i]))
#     a_list.append(int(b[i]))
# while True:
#     b_list = []
#     for i in range(len(a_list)-1):
#         b_list.append((a_list[i]+a_list[i+1])%10)
#     if len(b_list) == 2:
#         a_list = b_list
#         break
#     a_list = b_list
# for i in a_list:
#     print(i,end="")

# n = int(input())
# wow = n//3
# why = n%3
# if wow%2 == 0:
#     now = "CY"
# else:
#     now = "SK"
# if why%2 == 0:
#     if now == "CY":
#         print("SK")
#     else:
#         print("CY")
# elif why == 1:
#     print(now)
        

        
    
        