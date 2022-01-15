# num = int(input())
# wow = list(map(int,input().split()))

# if num == 0 or sum(wow) == 0:
#     print("divide by zero")
# else:
#     a = sum(wow)/num
#     b= [i*1/num for i in wow]
#     b = sum(b)
#     d = a/b
#     d = f"{d:.2f}".format(d)
#     print(d)

# a,b = map(int,input().split())
# print(a//b)
# print(a%b)

# ax,ay = map(int,input().split())
# bx,by = map(int,input().split())
# cx,cy = map(int,input().split())
# wow = max(abs(cx-ax),abs(cy-ay)) 어차피 얜 대각선으로만 움직일수있으니까
# why = abs(cx-bx)+abs(cy-by)
# if wow < why:
#     print("bessie")
# elif wow > why:
#     print("daisy")
# else:
#     print("tie")

# pi = 3.141592
# width = int(input())
# height = int(input())
# wow = width*2+height*pi*2
# print("{wow:.6f}".format(wow=wow))

# a,b,c = map(int,input().split())
# if a+b+c >= 100:
#     print("OK")
# else:
#     wow = [a,b,c]
#     wow.sort()
#     if wow[0] == a:
#         print("Soongsil")
#     elif wow[0] == b:
#         print("Korea")
#     else:
#         print("Hanyang")

so,width,height,mun = map(int,input().split())
wow = width//mun*height//mun
print(wow)