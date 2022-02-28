import string
a_list = list(string.ascii_lowercase)
A_list = list(string.ascii_uppercase)
wow = "!@#$%^&*()-+"
wow = list(wow)
n_list = list(map(str,[i for i in range(10)]))
a = 0
A = 0
m = 0
n = 0
l = int(input())
answer = list(input())
if l>=6:
    for i in answer:
        if i in a_list:
            a+=1
        elif i in A_list:
            A+=1
        elif i in wow:
            m+=1
        elif i in n_list:
            n+=1
    aa = [a,A,m,n]
    print(aa.count(0))
else:
    for i in answer:
        if i in a_list:
            a+=1
        elif i in A_list:
            A+=1
        elif i in wow:
            m+=1
        elif i in n_list:
            n+=1
    aa = [a,A,m,n]
    hm = aa.count(0)
    if hm+l >= 6:
        print(hm)
    else:
        print((6-(hm+l)+hm))