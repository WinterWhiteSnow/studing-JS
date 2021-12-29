# import sys
# a = list(map(int, sys.stdin.readline().rstrip()))
# a.sort(reverse=True)
# a = map(str,a)
# print("".join(a))

# import sys
# a = [int(i) for i in sys.stdin.readline().rstrip().split()]
# a.sort()
# print(a[0]*a[2])

# import sys
# a,b = map(int,sys.stdin.readline().rstrip().split())
# wow = sys.stdin.readline().rstrip().split()
# bow = sys.stdin.readline().rstrip().split()
# if len(wow) == a and len(bow) == b:
#     i = list(map(int,wow+bow))
#     i.sort()
#     for a in i: print(a,end=" ")

# import sys

# a = list(map(int,sys.stdin.readline().rstrip().split(" ")))
# a.sort()
# for i in a:
#     print(i, end=" ")

# import sys
# a = list(map(int,list(sys.stdin.readline().rstrip())))
# a.sort(reverse=True)
# a = list(map(str,a))
# b = "".join(a)
# if int(b) % 30 == 0:
#     print(b)
# else:
#     print(-1)

# import sys
# num = int(sys.stdin.readline().rstrip())
# a = sys.stdin.readline().rstrip().split(" ")
# if len(a) == num:
#     c = list(set(map(int,a)))
#     c.sort()
#     for i in c:
#         print(i, end=" ")

#22413

# import sys
# a = []
# for i in range(1,8+1):
#     d = [int(sys.stdin.readline().rstrip())]
#     d.append(i)
#     a.append(d)
# a = sorted(a, key = lambda x : x[0])
# a = a[3:]
# b = []
# count = 0
# for i in a:
#     count+=i[0]
#     b.append(i[1])
# b.sort()
# print(count)
# for i in b:
#     print(i,end=" ")

#22161

# import sys

# repeat,num = map(int, sys.stdin.readline().rstrip().split())
# a = []
# for _ in range(repeat):
#     o = list(map(int,sys.stdin.readline().rstrip().split()))
#     a.append(o)
# a = sorted(a, key= lambda x : (x[1]*3+x[2]*2+x[3]),reverse=True)
# oo = []
# cc = []
# for i in a:
#     count = i[1]*3+i[2]*2+i[3]
#     oo.append(count)
# for x in range(len(a)):
#     count = 0
#     for y in range(len(a)):
#         if oo[x]<oo[y]:
#             count+=1
#     cc.append(count)
# print(cc[num-1]+1)
            
    