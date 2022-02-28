# r,p=lambda:range(int(input())),print
# for T in r():
#     l=[input()for i in r()];p(f'Scenario #{T+1}:')
#     for T in r():p(''.join(l[int(i)]for i in input().split()[1:]))
#     p()
    
# p = print
# r = lambda : [i for i in range(int(input()))]
# p(r())

r = lambda : range(int(input()))
p = print
l=[input()for i in r()]
p(l)