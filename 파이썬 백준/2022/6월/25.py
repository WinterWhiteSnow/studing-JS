import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n_list = list(one() for _ in range(4))
# a = max(n_list[0],n_list[2])
# b = n_list[1]+n_list[3]
# print((a+2)*2+b*2)

# a,b,c,d = wow()
# a = a*3600+b*60
# b = c*3600+d*60
# if b < a:
#     b +=60*60*24
# print((b-a)//60, (b-a)//60//30)

# n_list = list(wow())
# average = sum(n_list)//3
# cnt = 0
# for i in range(2):
#     if n_list[i]<average:
#         n_list[i+1]-=average-n_list[i]
#         cnt+=average-n_list[i]
# print(cnt)

n = one()
m = one()
print(m)







