import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# name_list = [inputing() for _ in range(one())]
# in_list = sorted(name_list)
# de_list = sorted(name_list,reverse=True)
# if name_list == in_list:
#     print("INCREASING")
# elif name_list == de_list:
#     print("DECREASING")
# else:
#     print("NEITHER")
# n_dict = {}
# for _ in range(one()):
#     a,b = inputing().split(".")
#     if b not in n_dict:
#         n_dict[b]=1
#     else:
#         n_dict[b]+=1
# for i in sorted(n_dict.items(),key=lambda x : x[0]):
#     print(*i)

l,k = wow()
n_list = sorted([float(inputing())*10 for _ in range(l)])
if sum(n_list) == 0:
    print(0)
    print(0)
elif k == 0:
    z = round(sum(n_list)/l,2)
    print(f"{z:.2f}")
    print(f"{z:.2f}")
else:
    a = n_list[k:-k]
    x = round(sum(a)/len(a),2)
    a = [a[0]]*k+a+[a[-1]]*k
    y = round(sum(a)/len(a),2)
    print(f"{x:.2f}")
    print(f"{y:.2f}")










