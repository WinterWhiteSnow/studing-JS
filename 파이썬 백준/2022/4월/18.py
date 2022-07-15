
# a = int(input())
# print(bin(a).count("1"))

# n = input()
# l = len(n)
# index_list = []
# for a in range(1,l-1):
#     for b in range(1,l-1):
#         for c in range(1,l-1):
#             if a+b+c == l:
#                 index_list.append((a,b,c))
# wow_list = []
# for i in index_list:
#     a,b,c = i
#     a_str = n[:a][::-1]
#     b_str = n[a:a+b][::-1]
#     c_str = n[a+b:][::-1]
#     wow = a_str+b_str+c_str
#     wow_list.append(wow)
# wow_list.sort()
# print(wow_list[0])

# a,b = map(int,input().split())
# number =1
# number_list = []
# while len(number_list) < b:
#     number_list.extend([number]*number)
#     number+=1
# print(sum(number_list[a-1:b]))

# a,b,c = map(int,input().split())
# a = a%b
# n_list = []
# while len(n_list) != c:
#     if a < b:
#         a = a*10
#     n_list.append(a//b)
#     a = a%b    
# print(n_list[-1])
# n = input()
# cnt = 0
# while len(n) != 1:
#     n = str(sum(list(map(int,list(n)))))
#     cnt+=1
# print(cnt)
# if int(n)%3 == 0:
#     print("YES")
# else:print("NO")

# a = input()
# answer_dict = []
# for _ in range(int(input())):
#     b = input()
#     c = a+b
#     l = c.count("L")
#     o = c.count("O")
#     v = c.count("V")
#     e = c.count("E")
#     number = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))
#     answer_dict.append((b,number)) 
# answer_dict.sort(key=lambda x:x[0])
# answer_dict.sort(key=lambda x:(x[1]%100),reverse=True)
# print(answer_dict[0][0])

# l = int(input())
# answer = input()
# r = len(answer)//l
# answer_list = []
# for i in range(r):
#     answer_list.append(answer[i*l:i*l+l])
# for i in range(r):
#     if i%2 == 1:
#         answer_list[i]=answer_list[i][::-1]
# answer_dict = {}
# for i in range(r):
#     string = answer_list[i]
#     for index in range(len(string)):
#         if index not in answer_dict:
#             answer_dict[index]=[string[index]]
#         else:
#             answer_dict[index].append(string[index])
# string = ""
# for i in answer_dict.values():
#     string+="".join(i)
# print(string)

# while True:
#     r = int(input())
#     if r == 0:
#         break
#     list_list = [input() for _ in range(r)]
#     list_list.sort(key=lambda x: x.lower())
#     print(list_list[0])

# for _ in range(int(input())):
#     a = list(input())
#     answer_list = []
#     for _ in range(int(input())):
#         b = list(input())
#         cnt = len(set(b)-set(a))
#         count = len(set(a)-set(b))
#         answer_list.append(("".join(b),cnt+count))
#     answer_list.sort(key=lambda x : x[1])
#     print(answer_list[0][0])
# import datetime
# y,m,d = map(int,input().split())
# Y,M,D = map(int,input().split())
# now = datetime.datetime(y,m,d)
# after_years = datetime.datetime(1000+y,m,d)
# max_gap = after_years-now
# now_gap = datetime.datetime(Y,M,D)-now
# if now_gap >= max_gap:
#     print("gg")
# else:
#     print("D-"+str(now_gap.days))
# import datetime
# month,day,year,time = input().split()
# month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
# month = month_list.index(month)+1
# day = int(day[:-1])
# year = int(year)
# time = time.split(":")
# h = int(time[0])
# m = int(time[1])
# # print(datetime.datetime(year=year,month=month,day=day,hour=h,minute=m))
# if month == 1 and day == 1 and h == 0 and m == 0:
#     print(0.0)
# else:
#     after_year = datetime.datetime(year=year+1,month=1,day=1,hour=0,minute=0)
#     now_year = datetime.datetime(year=year,month=1,day=1,hour=0,minute=0)
#     now = datetime.datetime(year=year,month=month,day=day,hour=h,minute=m)
#     # print(((after_year-now_year).days)*24)
#     print(100-((after_year-now)/(after_year-now_year))*100)
# cnt = 1
# while True:
#     r = int(input())
#     if r == 0:
#         break
#     name_list = []
#     for _ in range(r):
#         name_list.append(input())
#     list_list = []
#     for _ in range(r*2-1):
#         wow,wow2 = input().split()
#         if wow in list_list:
#             list_list.remove(wow)
#         else:
#             list_list.append(wow)
#     print(cnt,name_list[int(list_list[0])-1])
#     cnt+=1

x,y,one,diagonal = map(int,input().split())
if one*2 <= diagonal:
    print((x+y)*one)








