# l = int(input())
# n_list = list(map(int,input().split()))
# n_list.sort(reverse=True)
# cnt = 0
# while len(n_list) >= 2:
#     a = n_list.pop()
#     b = n_list.pop()
#     cnt+=a*b
#     n_list.append(a+b)
#     # print(n_list)
#     n_list.sort(reverse=True)
# print(cnt)  

# n = int(input())
# print(2**n)
    
# d,h,m = map(int,input().split())
# if d == 11:
#     wow = h*60+m-(60*11+11)
#     if wow < 0:
#         print(-1)
#     else:
#         print(wow)
# else:
#     print((d-11)*(60*24)+h*60+m-(60*11+11))

# limit = int(input())
# now = int(input())
# if now <= limit :
#     print("Congratulations, you are within the speed limit!")
# else:
#     gap = now-limit
#     if 1<=gap<=20:
#         print("You are speeding and your fine is $100.")
#     elif 21<=gap<=30:
#         print("You are speeding and your fine is $270.")
#     else:
#         print("You are speeding and your fine is $500.")    
# n_list = []
# for _ in range(4):
#     n = int(input())
#     n_list.append(n)
# start = n_list[0]
# a_list = []
# for i in range(1,len(n_list)):
#     if start < n_list[i]:
#         a_list.append("plus")
#     elif start == n_list[i]:
#         a_list.append("equal")
#     else:
#         a_list.append("minus")
#     start = n_list[i]
# if len(set(a_list)) == 1:
#     if set(a_list) == {"plus"}:
#         print("Fish Rising")
#     elif set(a_list) == {"minus"}:
#         print("Fish Diving")
#     else:
#         print("Fish At Constant Depth")
# else:
#     print("No Fish")

# antenna = int(input())
# eyes = int(input())
# a_list = []
# if antenna >= 3 and eyes <= 4:
#     a_list.append("TroyMartian")
# if antenna <= 6 and eyes >= 2:
#     a_list.append("VladSaturnian")
# if antenna <= 2 and eyes <= 3:
#     a_list.append("GraemeMercurian")
# for i in a_list:
#     print(i)

# n = int(input())
# print((n+1)*2,(n+1)*3)


    
        
    


