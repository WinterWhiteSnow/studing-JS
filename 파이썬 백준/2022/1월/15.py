# while True:
#     wow = list(input())
#     if wow[0] == "#":
#         break
    
#     dict_list = {"-":0,"\\":1,"(":2,"@":3,"?":4,">":5,"&":6,"%":7,"/":-1}
#     why = [int(dict_list[i]) for i in wow]
#     cnt = [i for i in range(len(why))]
#     cnt.sort(reverse=True)
#     result = 0
#     for i in range(len(why)):
#         result+=why[i]*(8**(cnt[i]))
#     print(result)


# cnt = 7
# result = 5
# wow = int(input())
# for _ in range(wow-1):
#     result+=cnt
#     cnt+=3
# print(result%45678)
# import sys
# num = int(sys.stdin.readline().rstrip())
# b = []
# for _ in range(num):
#     a = int(sys.stdin.readline().rstrip())
#     b.append(a)
# print(sum(b)-(num-1))

# k,l =map(int,input().split())
# sosu_dict = {}
# for i in range(2,l):
#     if i not in sosu_dict:
#         for a in range(i,l,i):
#             sosu_dict[a]=0
#         sosu_dict[i]=1
# sosu_list = [i[0] for i in sosu_dict.items() if i[1] == 1]
# cnt=0
# while True:
#     if cnt == len(sosu_list):
#         print("GOOD")
#         break
    
#     if k%sosu_list[cnt] == 0:
#         print("BAD",sosu_list[cnt])
#         break
#     else:
#         cnt+=1

# import sys
# a,b = map(int,sys.stdin.readline().rstrip().split())
# g=[a,b]
# g.sort()
# a = g[0]
# b = g[1]
# wow = b-a+1
# repeat = wow//2
# num = a+b
# if wow % 2 == 0:
#     print(num*repeat)
# else:
#     print(num*repeat+((a+b)//2))

# num = int(input())
# wow = [i for i in range(1,num+1)]
# for i in wow[::-1]:
#     a = "*"*i
#     print(a.rjust(len(wow)))

# num = int(input())
# cnt = [1]
# plus = 2
# write = 1
# standard = "plus"
# for _ in range(num-1):
#     a = cnt[-1]+plus
#     cnt.append(a)

# repeat = cnt[-1]
# w = num*2

# for _ in range(repeat):
#     if write == num :
#         standard = "minus"
#     wow = w-2*write
#     print("*"*write,end="")
#     print(" "*wow,end="")
#     print("*"*write)
    
#     if standard == "plus":
#         write+=1
#     elif standard == "minus":
#         write-=1

# num = int(input())
# cnt = [1]
# plus = 2
# d_cnt = 0
# for _ in range(num-1):
#     a = cnt[-1]+plus
#     cnt.append(a)
# down_cnt = cnt[::-1]
# for i in down_cnt:
#     print(" "*d_cnt,end="")
#     print("*"*i,end="")
#     print()
#     d_cnt+=1
# up_cnt = 2
# cnt = cnt[1:]
# for i in cnt:
#     print(" "*(num - up_cnt),end="")
#     print("*"*i,end="")
#     print()
#     up_cnt+=1

# yes = 0
# max_num = 0
# for _ in range(10):
#     a,b = map(int,input().split())
#     yes+=b
#     yes-=a
#     if max_num < yes:
#         max_num = yes
# print(max_num)

# repeat = int(input())
# m = []
# for _ in range(repeat):
#     a,b,c = map(int,input().split())
#     l = [a,b,c]
#     l.sort()
#     s = set(l)
#     if len(s) == 3 :
#         m.append(l[-1]*100)
#     elif len(s) == 2 :
#         m.append(l[1]*100+1000)
#     else:
#         m.append(10000+l[0]*1000)
        
# print(max(m))

# for _ in range(3):
#     wow = input().split(" ")
#     if wow.count("0") == 1:
#         print("A")
#     elif wow.count("0") == 2:
#         print("B")
#     elif wow.count("0") == 3:
#         print("C")
#     elif wow.count("0") == 4:
#         print("D")
#     else:
#         print("E")

# num,times = map(int,input().split())
# yaksu = {}
# for i in range(1,num+1):
#     if num%i == 0:
#         yaksu[i]=1
# if len(yaksu) < times:
#     print(0)
# else:
#     yaksu = [i[0] for i in yaksu.items()]
#     print(yaksu[times-1])

# length = int(input())
# wow = input().split()
# cnt = 0
# plus = 0
# if len(wow) == length:
#     for i in range(length):
#         if wow[i] == "1":             
#             plus+=1
#             cnt+=plus
#         else:
#             plus=0  
# print(cnt)   

a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_p = 0
b_p = 0
last = "wow"
for A,B in zip(a,b):
    if A > B :
        a_p+=3
        last = "A"
    elif B > A:
        b_p+=3
        last = "B"
    else:
        b_p+=1
        a_p+=1
print(a_p,b_p)
if a_p > b_p:
    print("A")
elif a_p < b_p:
    print("B")
elif a_p == b_p:
    if last != "wow":
        print(last)
    else:
        print("D")
     
