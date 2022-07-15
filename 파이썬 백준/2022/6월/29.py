import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# limit = one()
# for index in range(1,limit+1):
#     a,b = wow()
#     print(f"Data Set {index}:")
#     if b>=a:
#         print("no drought")
#     else:
#         c = a/b
#         cnt = 0
#         while c>=5:
#             cnt+=1
#             c/=5
#         if c > 1:
#             cnt+=1
#         cnt=cnt-1
#         str_str = ["mega"]*cnt
#         print(*str_str,"drought")
#     if index != limit:
#         print()

# for i in sys.stdin.readlines():
#     num = int(i)
#     cnt = 0
#     while num != 1:
#         if num%2 == 0:
#             cnt+=1
#             num//=2
#         else:
#             cnt+=1
#             num = num*3+1
#     print(cnt)

# r,yes,limit = wow()
# for _ in range(r):
#     now = one()
#     if yes>now:
#         gap = yes-now
#         print(f"NTV: Dollar dropped by {gap} Oshloobs")
#     yes=now
#     if limit<now:
#         print(f"BBTV: Dollar reached {now} Oshloobs, A record!")
#         limit=now













