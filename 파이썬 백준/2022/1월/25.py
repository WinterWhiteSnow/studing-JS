# import sys

# start_h,start_m = map(int,sys.stdin.readline().rstrip().split())
# end_h,end_m = map(int,sys.stdin.readline().rstrip().split())
# n = int(sys.stdin.readline().rstrip())
# cnt=0 #1720 2045 2
# while True:
#     if str(int(n)) in str(int(start_m)) or str(int(n)) in str(int(start_h)):
#         # print(str(start_m))
#         cnt+=1
#     if end_h==start_h and start_m==end_m:
#         break
#     start_m+=1
#     if start_m==60:
#         start_m=0
#         start_h+=1
# print(cnt)
#26 시간초과
#sys 해도 26초과    

# import sys   
# import math
# l = int(sys.stdin.readline().rstrip())
# wow = list(map(int,sys.stdin.readline().rstrip().split()))
# a=wow[0]
# b=wow[1]
# c=wow[-1]
# mini = math.gcd(a,b,c)
# for i in range(1,(mini//2)+1):
#     if a%i==b%i==c%i==0:
#         print(i)
# print(mini)
# wow = list(map(int,input().split()))
# wow.sort()
# cnt =1
# for i in range(wow[0],wow[1]+1):
#     a = [i for i in range(1,i+1)]
#     cnt*=sum(a)
# print(cnt%14579)

# l = int(input())
# wow = list(map(int,input().split()))
# cnt=0
# index=0
# for i in wow:
#     if i == index%3:
#         cnt+=1
#         index+=1
# print(cnt)
num = int(input())
cnt = 0 
start = 0
for i in range(1,num+1):
    if cnt < num:
        for _ in range(i):
            cnt+=1
    if cnt >= num:
        start=i
        break
total = start+1
b = total-start+(num-start)
a = total-b 
print("start:",start,"total:",total)
          