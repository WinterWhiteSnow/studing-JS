
# wow = list(map(int,input().split()))
# wow.sort()
# index = 1
# while (wow[-1]-wow[0])*index < wow[-1]:
#     index+=1
# print(index)

# while True:
#     a,b = map(int,input().split())
#     index = 1
#     if a ==b==0:
#         break
#     while a > index**b:
#         index+=1
#     if abs(index**b-a) <= abs((index-1)**b-a):
#         print(index)
#     else:
#         print(index-1)
# a_list = []
# for _ in range(8):
#     a_list.append(int(input()))
# a_list = a_list*2
# list_list = []
# for i in range(8):
#     list_list.append(sum(a_list[i:i+4]))
# print(max(list_list))

# a,m = map(int,input().split())
# k = 1

# while (m*k+1)%a != 0:
#     k+=1
# print((m*k+1)//a)

# n = int(input())
# index = 1
# list_list = []
# for i in range(1,n//2+1):
#     if n%i ==0:
#         list_list.append(i)
#         # print(list_list)
# print(sum(list_list)+n)

# person = int(input())
# times = int(input())
# what = input()
# repeat = 2
# list_list = []
# while list_list.count(what)<times:
#     wow = ["0","1","0","1"]+["0"]*repeat+["1"]*repeat
#     list_list.extend(wow)
#     repeat+=1
# # print(list_list)
# cnt=0
# for i in range(len(list_list)):
#     if list_list[i] == what:
#         cnt+=1
#         if cnt == times:
#             print(i%person)
#             break

# m,seed,x1,x2 = map(int,input().split())
# for a in range(0,m+1):
#     for c in range(0,m+1):
#         if (a*seed+c)%m == x1 and (a*x1+c)%m == x2:
#             print(a,c)
#             exit() 

while True:
    try:
        a = int(input())
        string = [a]
        index = 2
        wow = set(list("".join([i for i in range(10)])))
        cnt = 0
        while set(string).intersection(wow) != wow:
            cnt+=1
            string.append()
        
        
        
    except:
        break


    

    
    
        







