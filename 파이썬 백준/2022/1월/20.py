# repeat = int(input())
# a_list = []
# for _ in range(repeat):
#     car = int(input())
#     two = int(input())
#     for i in range(two):
#         a,b = map(int, input().split())
#         car+=a*b
#     a_list.append(car)
    
# for i in a_list:
#     print(i)

# repeat = int(input())
# for i in range(1,repeat+1):
#     a = list(map(int,input().split()))
#     print(f"Case #{i}: ",end="")
#     if len(set(a)) ==1:
#         print("equilateral")
#     elif len(set(a)) ==2:
#         if a[0]+a[1]>a[-1]:
#             print("isosceles")
#         else:
#             print("invalid!")
#     elif len(set(a))==3:
#         a.sort()
#         if a[0]+a[1]>a[-1]:
#             print("scalene")
#         else:
#             print("invalid!")

# while True:
#     wow = list(map(int,input().split()))
#     if sum(wow) == 0:
#         break
    
#     page = wow[0]
#     number = wow[1]
#     why = []
#     num = page+1
#     if number%2 == 0:        
#         for i in range(number-1,number+1):
#             a = i
#             b = num-i
#             why.append(a)
#             why.append(b)
#     else:
#         for i in range(number,number+2):
#             a = i
#             b = num-i
#             why.append(a)
#             why.append(b)
#     why.sort()
#     for i in why:
#         if i == number:
#             pass
#         else:
#             print(i,end=" ")
#     print()

# repeat = int(input())
# for _ in range(repeat):
#     num,mile,t1,t2,f = map(float,input().split())
#     wow = mile/(t1+t2)*f
#     print(int(num),f"{wow:.6f}")
while True:
    m,a,b = map(int,input().split())
    if m+a+b == 0:
        break    
    a_m = (m/a)*60
    b_m = (m/b)*60
    if a_m > int(a_m):
        a_s = str(a_m)[3:]
        if len(a_s) == 1:
            a_s = a_s+"0"
        a_m = str(a_m)[:2]
    else:
        a_s = 0
        
    if b_m > int(b_m):
        b_s = str(b_m)[3:]
        if len(b_s) == 1:
            b_s = b_s+"0"
        b_m = str(b_m)[:2]
    else:
        b_s = 0
    a_m,a_s,b_m,b_s = map(int,[a_m,a_s,b_m,b_s])
    a_s = a_s*0.6
    b_s = b_s*0.6  
    total_m = a_m-b_m
    total_s = a_s-b_s
    if total_s < 0:
        total_s +=60
        total_m -=1
    total_m = str(total_m).zfill(2)
    total_s = str(int(total_s)).zfill(2)
    print(f"0:{total_m}:{total_s}")
