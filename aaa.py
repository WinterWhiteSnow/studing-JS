# n = int(input())
# cnt= 0
# line = 0

# while n > cnt:
#     line +=1
#     cnt += line
# gap = cnt - n
# if line % 2 == 0:
#     top = line - gap
#     under = gap + 1
# else:
#     top = gap + 1
#     under = line - gap
# print("{}/{}".format(top, under))


t = int(input())
for i in range(0,t):
    k = int(input())
    n = int(input())
    num = 1
    l = k + n
    for i in range(1,l+1):
        num *= i
    for i in range(1, k+2):
        num /= i
    for i in range(1,n):
        num /= i
    print(int(num))