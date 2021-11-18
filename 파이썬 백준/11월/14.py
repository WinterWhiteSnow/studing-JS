a = int(input())
a_a = [int(i) for i in input().split()]
if len(a_a) == a:
    a = a_a

b = int(input())
b_b = [int(i) for i in input().split()]
if len(b_b) == b:
    b = b_b
a.sort()
for i in b:   
    start = 0
    end = len(a) - 1   
    mid = (start+end)//2
    print(start,end,mid)
    print(a[end],a[start])
    while a[end]-a[start] !=0:
        if i<a[mid]:
            end=mid-1
            print("end",end)
        elif i > a[mid]:
            start=mid+1
            print("start",start)
        elif i == a[mid]:
            print("wow",mid)
            break

    



    
    
    