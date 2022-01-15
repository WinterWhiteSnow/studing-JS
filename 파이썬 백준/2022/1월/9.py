# w = list(map(int,input().split()))
# w.sort()
# print(int(w[-1]*w[1]/w[0]))
# 33% 실패

# a,b,c = map(int, input().split())
# print(int(max(a*b/c, a/b*c)))

# wow = input()
# if len(wow) > 2 :
#     b = wow[-2:]
#     if int(b) > 10 or b[0] == "0":
#         b = wow[-1]
#         a = wow[:-1]
#     else:
#         b = wow[-2:]
#         a = wow[:-2]
# else:
#     a = wow[0]
#     b = wow[-1]
# print(int(a)+int(b)) 

# year1,month1,day1 = map(int,input().split())
# year2,month2,day2 = map(int,input().split())
# if month2 >= month1:
#     if month2 == month1:
#         if day2 >= day1:
#             print(year2-year1)
#         else:
#             print(year2-year1-1)
#     else:
#         print(year2-year1)
# else:
#     print(year2-year1-1)
# print(year2-year1+1)
# print(year2-year1)

a,b,c = map(int,input().split())
count = 0
if b ==0 and c == 0 :
    print(a)
else:
    wow = [b,c]
    wow.sort()
    count+=wow[0]
    if b >c :
        count+= a-b
    elif c >b :
        count+= a-c
    else:
        count+= a-b
    print(count)
