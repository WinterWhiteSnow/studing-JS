# for _ in range(int(input())):
#     len_count = 0
#     str_count = 0
#     while True:
#         a = input()
#         if a == "":
#             break
#         str_count+=len(a)-a.count("#")
#         len_count+=len(a)
#     num = round((str_count/len_count*100),1)
#     if int(num) == num:
#         print(f"Efficiency ratio is {int(num)}%.")
#     else:
#         print(f"Efficiency ratio is {num}%.")

# while True:
#     a = input()
#     if a == "0":
#         break
#     cnt=0
#     length = len(a)
#     int_a = int(a)
#     while True:
#         string = str(int_a).rjust(length,"0")
#         # print(string,string[::-1])
#         if string == string[::-1]:
#             break
#         int_a+=1
#         cnt+=1
#     print(cnt)

# l = [0 for i in range(int(input()))]
# num_list = []
# for index in range(int(input())):
#     start,end = map(int,input().split())
#     for i in range(start-1,end):
#         if l[i] == 0:
#             l[i] = index+1
#     num_list.append(end-start)
# key_list = set([i for i in l if i >0])
# l_dict = {}
# for i in key_list:
#     l_dict[i]=l.count(i)
# l_list = sorted(l_dict.items(),key=lambda x:x[0])
# l_list.sort(key=lambda x:x[1],reverse=True)
# print(num_list.index(max(num_list))+1)
# print(l_list[0][0])

# string,n = input().split()
# n = int(n)
# string = string.lower()
# string+="0"
# now_str = ""
# use_str = {}
# cnt = 0
# for i in string:
#     if now_str == "":
#         now_str = i
#         cnt+=1
#     else:
#         if now_str == i:
#             cnt +=1
#         else:
#             # print(i,now_str,cnt)
#             if now_str not in use_str:                
#                 if cnt >= n:
#                     use_str[now_str]=["1"]
#                 else:
#                     use_str[now_str]=["0"]
#             else:
#                 use_str[now_str].append("false")
#             now_str=i
#             cnt=1
# string_string = ""
# for i in use_str.values():
#     string_string+=i[0]
# print(string_string)

gyosu_garo = 0
gyosu_sero = 0
seonggyu_garo = 0
seonggyu_sero = 0
garo = {}
for i in range(int(input())):
    a = input().split()
    if "5" in a:
        gyosu_garo = a.index("5")
        gyosu_sero = i
    elif "2" in a:
        seonggyu_garo = a.index("2")
        seonggyu_sero = i
    garo[i]=a
distance = ((seonggyu_garo-gyosu_garo)**2+(seonggyu_sero-gyosu_sero)**2)**(1/2)
if distance >= 5:
    cnt = 0
    for i in range(min(gyosu_sero,seonggyu_sero),max(gyosu_sero,seonggyu_sero)+1):
        wow = garo[i][min(gyosu_garo,seonggyu_garo):max(gyosu_garo,seonggyu_garo)+1]
        cnt+=wow.count("1")
    if cnt >=3:
        print(1)
    else:
        print(0)   
else:
    print(0)
        
    
  
        
