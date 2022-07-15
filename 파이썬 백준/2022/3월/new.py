n = int(input(),16)
for i in range(1,17):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

#최소공배수
# def wow(list_list):
#     def gcd(x,y):
#         return x*y//gcd(x,y)
#     while True:
#         list_list.append(gcd(list_list.pop(),list_list.pop()))
#         if len(list_list)==1:
#             return list_list[0]

import sys
x,y = 0,1
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    x,y = (x+y)%1000000,x%1000000
print(x)