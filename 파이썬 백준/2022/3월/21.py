# cnt = 0
# while True:
#     a = input()
#     if "-" in a:
#         break
#     while "{}" in a:
#         a= "".join(a.split("{}"))
#     string = []
#     stack = 0
#     for i in list(a):
#         if len(string) == 0:
#             string+=i
#         else:
#             if i == "}":
#                 if string[-1] == "}":
#                     string.pop()
#                     stack+=1
#                 else:
#                     string.append(i)
#             else:#{
#                 if string[-1] == "{":
#                     string.pop()
#                     stack+=1
#                 else:
#                     string.append(i)
#         # print(string)
#     cnt+=1
#     # print("최종",string,stack)
#     print(f"{cnt}.", len(string)+stack)

l = int(input())
n_list = list(map(int,input().split()))
if sum(n_list)%3 == 0 and sum(n_list)%2 == 0:
    print("YES")
else:
    print("NO")
        