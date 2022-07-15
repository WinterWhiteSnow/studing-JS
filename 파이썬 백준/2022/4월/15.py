# number = "9780921418"
# for _ in range(3):
#     number+=input()
# number = list(map(int,list(number)))
# wow = 0
# for i in range(len(number)):
#     if i%2 == 0:
#         wow+=number[i]
#     else:
#         wow+=number[i]*3
# print("The 1-3-sum is",wow)

# l,r = map(int,input().split())
# if l%2 == 1:
#     sero = r
# else:
#     sero = 0
# if r%2 == 1:
#     garo = l
# else:
#     garo = 0
# print(min(sero,garo))
# import math
# now,goal,plus = map(int,input().split())
# print(math.ceil((goal-now)/plus))

total,k = map(int,input().split())
a = [k//2,k,k*2]
b = [k,k*2,k*2*2]
c = [k//2//2,k//2,k]
wow = [a,b,c]
wow = [i for i in wow if sum(i) <= total and sum(i) == int(sum(i)) and 0 not in i]
wow.sort(key=lambda x: sum(x))
if wow:
    print(sum(wow[-1])*1000)    
else:
    print(0)





        






















