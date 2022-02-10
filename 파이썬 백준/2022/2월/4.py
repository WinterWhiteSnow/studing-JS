# import string
# a = list(string.ascii_uppercase)
# a_dict = {}
# cnt = 0
# num = 2
# for i in range(15):
#     if cnt ==3:
#         num+=1
#         cnt=0
#     a_dict[a[i]]=num
#     cnt+=1
# num = 7
# cnt = 0
# limit = 4
# for i in range(15,len(a)):
#     a_dict[a[i]]=num
#     cnt+=1
#     if cnt == 4:
#         if limit ==4:
#             num+=1
#             cnt=0
#             limit =3
#     elif cnt == 3:
#         if limit ==3:
#             num+=1
#             cnt=0
#             limit=4
# a_dict[" "]=1
# p,w = map(int,input().split())
# wow = list(input())
# cnt = 0
# num = 0
# for i in wow:
#     fly = [key for key,value in a_dict.items() if value == a_dict[i]]
#     index = fly.index(i)
#     if num == a_dict[i]:
#         if num ==1:
#             cnt+=p*(index+1)
#         else:            
#             cnt+=w+p*(index+1)
#     else:
#         cnt+=p*(index+1)
#     # print(i,fly,index,num)
#     num=a_dict[i]
# print(cnt)

# n,p = map(int,input().split())
# k =n
# n_list = [n]
# while True:
#     n = n_list[-1]*k%p
#     if n in n_list:
#         n_list.append(n)
#         break
#     n_list.append(n)
# print(len(n_list)-1-n_list.index(n_list[-1]))
# a_list = []
# for _ in range(5):
#     a = int(input())
#     a_list.append(a)
# a_list.sort()
# print(sum(a_list)//5)
# print(a_list[2])

# n = int(input())
# wow = input()
# wow_list = []
# a_dict = {"000000":"A","001111":"B","010011":"C","011100":"D","100110":"E","101001":"F","110101":"G","111010":"H"}
# start = 0
# for _ in range(n):
#     a = wow[start:start+6]
#     wow_list.append(a)
#     start+=6
# answer= []
# for i in wow_list:
#     if i in a_dict:
#         answer.append(a_dict[i])
#     else:
#         a = list(i)
#         b = list(a_dict.keys())
#         is_append=False
#         for c in b:
#             d = list(c)
#             cnt = 0
#             for aa in range(len(a)):
#                 if a[aa] == d[aa]:
#                     cnt+=1
#                 if cnt ==5:
#                     answer.append(a_dict[c])
#                     is_append=True
#                     break
#             if is_append==True:
#                 break
#         if is_append==False:
#             print(1+wow_list.index(i))
#             exit()
# print("".join(answer)) 

# l = int(input())
# wow = list(map(int,input().split()))
# answer = []
# if len(wow) == l:
#     for i in range(len(wow)):
#         if wow[i] == 0:
#             answer.append(i+1)
#         else:
#             answer.insert(len(answer)-wow[i],i+1)
# print(*answer)       

# repeat = int(input()) 
# for _ in range(repeat):
#     a = list(map(int,input().split(":")))
#     b = []
#     for i in a:
#         c = bin(i)[2:]
#         c = "0"*(6-len(c))+c
#         b.append(c)
#     three_hang = ""
#     join_b = "".join(b)
#     for x in range(len(b[0])):
#         for y in range(len(a)):
#             three_hang+=join_b[(y*6)+x]
#     print(three_hang,join_b)

# repeat = int(input())
# for _ in range(repeat):
#     index,string = input().split()
#     index = int(index)-1
#     for i in range(len(string)):
#         if i == index:
#             pass
#         else:
#             if i != index:
#                 print(string[i],end="")
#     print()

# repeat = int(input()) #round5
# for _ in range(repeat):
#     num,unit = input().split()
#     num = float(num)
#     if unit == "kg":
#         wow = round(num*2.2046,4)
#         unit = "lb"
#     elif unit == "g": #갤런
#         wow = round(num*3.7854,4)
#         unit ="l"
#     elif unit == "lb": #파운드
#         wow = round((num*0.4536),4)
#         unit = "kg"
#     else: #리터
#         wow = round((num*0.2642),4)
#         unit = "g"
#     print(f"{wow:.4f}",unit)

# a = input()
# print(len(a))

# import string
# a = list(string.ascii_uppercase)
# a_dict = {}
# for i in range(len(a)):
#     a_dict[a[i]]=i+10

# string,num = input().split()
# num= int(num)
# print(int(string,num))

repeat = int(input())
for _ in range(repeat):
    string = input().split()
    player1_list = string[:len(string)//2]
    player2_list = string[len(string)//2:]
    total = [player1_list,player2_list]
    player1 = 0
    player2 = 0
    count = 1
    for i in total: #처음은 p1 두번째 p2
        x_list = []
        y_list = []
        cnt = 0
        for a in i:
            if cnt%2 == 0:
                x_list.append(a)
            else:
                y_list.append(a)
            cnt+=1
        for x,y in zip(x_list,y_list):
            x = float(x)
            y = float(y)            
            line = abs(x)*abs(x)+abs(y)*abs(y)
            if 0<line <=3*3:
                plus = 100
            elif 3*3<line<=3*3*3:
                plus=80
            elif 3*3*3<line<=3*3*3*3:
                plus=60
            elif 3*3*3*3<line<=3*3*3*3*3:
                plus=40
            elif 3*3*3*3*3<line<=3*3*3*3*3*3:
                plus=20
            print(count,line,plus)
                
            if count == 1:
                player1+=plus
            else:
                player2+=plus
        if count==1:
            count=2
    print(player1,player2)
        
            
    # for i in range(len(string)):
    #     if i%2 ==0:
    #         x_list.append(float(string[i]))
    #     else:
    #         y_list.append(float(string[i]))

    # cnt = 0
    # print(player1,player2)
                     
            
    
    
