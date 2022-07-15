import sys


inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# num = one()
# cnt = 0
# for a in range(1,num):
#     for b in range(a+1,num):
#         for c in range(b+1,num):
#             if a!=b!=c and c>b>a:
#                 cnt+=1
# print(cnt)
index = 1
while True:
    a,b = wow()
    if a==b==0:
        break
    if index != 1:
        print()
    print(f"Hole #{index}")
    if b==1:
        print("Hole-in-one.")
    else:
        if a==b:
            print("Par.")
        if a-1==b:
            print("Birdie.")
        if a-2==b:
            print("Eagle.")
        if a-3>=b:
            print("Double eagle.")
        if a+1==b:
            print("Bogey.")
        if a+2<=b:
            print("Double Bogey.")
        
    index+=1
    















