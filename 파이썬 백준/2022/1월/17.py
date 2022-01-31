# a = list(input())
# b = [1,2,3]
# for i in a:
#     if i == "A":
#         x = b[0]
#         y = b[1]
#         b[0] = y
#         b[1] = x
#     elif i == "B":
#         x = b[1]
#         y = b[-1]
#         b[1] = y
#         b[-1] = x
#     else:
#         x = b[0]
#         y = b[-1]
#         b[0] =y
#         b[-1]=x
# print(b.index(1)+1)

# repeat,w,h = map(int,input().split())
# wow = ((w**2)+(h**2))**(1/2)
# for _ in range(repeat):
#     a =int(input())
#     if a <= wow:
#         print("DA")
#     else:
#         print("NE")

# repeat = int(input())
# for _ in range(repeat):
#     a = list(map(int,input().split()))
#     b = [i for i in a if i%2 == 0]
#     print(sum(b),min(b))

# repeat = int(input())
# for _ in range(repeat):
#     a = int(input())
#     b = bin(a)
#     b = list(b[2:][::-1])
#     for i in range(len(b)):
#         if b[i] == "1":
#             print(i,end=" ")

# while True:
#     a,b = map(int,input().split())
#     if a == 0 and b == 0:
#         break
    
#     if a > b:
#         print("Yes")
#     else:
#         print("No")
while True:
    wow = input().split()
    if wow[0] == "0" and wow[1] == "0":
        break
    
    a = list(map(int,wow[0]))
    b = list(map(int,wow[1]))
    a = a[::-1]
    b = b[::-1]
    l = min(len(a),len(b))
    plus = 0
    cnt=0
    for i in range(l):
        if a[i]+b[i]+plus > 9:
            cnt+=1
            plus+=1
        else:
            plus=0
    print(cnt)
# 99 1 처리해야함