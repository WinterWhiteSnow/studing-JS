n = int(input())
cnt= 0
line = 0

while n > cnt:
    line +=1
    cnt += line
print(line,cnt)
gap = cnt - n
if line % 2 == 0:
    top = line - gap
    under = gap + 1
else:
    top = gap + 1
    under = line - gap
print("{}/{}".format(top, under))
