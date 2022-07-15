#1로 만들기

n=int(input())
d=[0]*1000001
d[1]=0

for i in range(2,n+1):
    i2,i3=int(i/2),int(i/3)
    if (not i%2)&(not i%3): d[i]=min(d[i-1]+1,d[i2]+1,d[i3]+1)
    elif not i%2: d[i]=min(d[i-1]+1,d[i2]+1)
    elif not i%3: d[i]=min(d[i-1]+1,d[i3]+1)
    else: d[i]=d[i-1]+1
    print(d[:n+1])
print(d[n])


# 내식대로

num = one()
wow_list = [0]*(10**6+1)
for i in range(2,num+1):
    if i%6 == 0:
        wow_list[i] = min(wow_list[i-1]+1,wow_list[i//2]+1,wow_list[i//3]+1)
    else:
        if i%2 == 0:
            wow_list[i] =  min(wow_list[i-1]+1,wow_list[i//2]+1)
        elif i%3 == 0:
            wow_list[i] = min(wow_list[i-1]+1,wow_list[i//3]+1)
        else:
            wow_list[i] = wow_list[i-1]+1
    # print(wow_list[:num+1])
print(wow_list[num])

a= [0,1,0]
for i in a:
    print(not i)
#헐...





