import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


# cnt = 0
# max_max = 0
# for _ in range(one()):
#     a = one()
#     cnt+=a
#     if cnt < 0:
#         max_max = max(max_max,abs(cnt))
# print(max_max)

# for index in range(1,one()+1):
#     r = one()
#     for _ in range(r):
#         a,b = wow()
#     c,d = wow()
    
#     print(f"Material Management {index}")
#     print("Classification ---- End!")
# now_x = "no"
# now_y = "no"
# cnt = 0
# for _ in range(one()):
#     a,b = wow()
#     if now_x==now_y=="no":
#         pass
#     else:
#         cnt+=abs(now_x-a)+abs(now_y-b)
#     now_x=a
#     now_y=b
# print(cnt)

# a,b = inputing().split()
# if a.isdigit() and b.isdigit():
#     print(int(a)-int(b))
# else:
#     print("NaN")

# for _ in range(one()):
#     a,b = wow()
#     a_list = list(wow())
#     b_list = list(wow())
#     if a<=b:
#         print("Yes")
#     else:
#         print("No")

# for i in range(1,1+one()):
#     end,now,s = wow()
#     cnt = min(now+now-s+(end-s),now+end)
#     print(f"Case #{i}: {cnt}")

# a,b,n,m =wow()
# a_str = ""
# b_str = ""
# while len(a_str) < a:
#     a_str+="1"+"0"*n
# while len(b_str) < b:
#     b_str+="1"+"0"*m
# print(a_str.count("1")*b_str.count("1"))

# num = one()
# while num%2 != 0:
#     num = ((num-1)//2)+1
# print(num)

# a,b,c,d = wow()
# x = min(a,b)
# y = max(a,b)
# p = min(c,d)
# q = max(c,d)
# cnt = 0
# for i in range(1,max(a,b,c,d)+1):
#     if x<=i<=y or p<=i<=q:
#         cnt+=1
     
# print(cnt)



