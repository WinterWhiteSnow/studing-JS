# r,l = map(int,input().split())
# a_list = []
# for _ in range(r):
#     a = input()
#     b = a[::-1]
#     a = a+b
#     a_list.append(a)
# r_i,l_i = map(int,input().split())
# for i in a_list[::-1]:
#     a_list.append(i)
# r_i = r_i-1
# l_i = l_i -1
# a_list[r_i]=list(a_list[r_i])
# if a_list[r_i][l_i]=="#":
#     a_list[r_i][l_i]="."
# else:
#     a_list[r_i][l_i]="#"      
# a_list[r_i]="".join(a_list[r_i])
# for i in a_list:
#     print(i)
# a_list = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
# n = input().split()
# a=""
# for i in range(len(n)):
#     if n[i] in a_list:
#         if i == 0:
#             a+=n[i][0].upper()
#         else:
#             pass
#     else:
#         a+=n[i][0].upper()
# print(a)        
# r = int(input())
# cnt = 0
# for _ in range(r):
#     time,d = input().split()
#     h,m = map(int,time.split(":"))
#     d = int(d)
#     if m+d >=60:
#         a=60-m #15
#         b=d-a #30-15
#         if 7<=h<19:
#             cnt+=a*10
#         else:
#             cnt+=a*5
#         if 7<=h+1<19:
#             cnt+=b*10
#         else:
#             cnt+=b*5        
#     else:
#         if 7<=h<19:
#             cnt+=d*10
#         else:
#             cnt+=d*5
# print(cnt)
while True:
    try:
        a = int(input())
        if a%6 == 0:
            print("Y")
        else:
            print("N")
    except:
        exit()
    