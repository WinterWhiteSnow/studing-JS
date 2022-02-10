# repeat = int(input())
# for _ in range(repeat):
#     a = list(input())
#     print(len(set(a)))

# a = list("CAMBRIDGE")
# b = list(input())
# c = [i for i in b if i not in a]
# print("".join(c))
    
a,b = input().split()
bb = list(b) #이게 세로
aa = list(a) # 가로
cnt = 0
for i in b:
    if i in a:
        cnt=i
        break
height = bb.index(cnt)
width = aa.index(cnt)
for i in range(len(bb)):
    if i != height:
        print("."*width,end="")
        print(bb[i],end="")
        print("."*(len(bb)-width-1))
    else:
        print(a)