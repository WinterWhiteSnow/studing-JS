a = list(range(1,10))
b = [7,8,9,4,5,6,1,2,3]
c = {}
for i in range(len(b)):
	c[a[i]]=b[i]

answer_list = []
count = 0
while count !=7:
	count +=1
	answer = int(input())
	answer_list.append(c[answer])
for i in answer_list:
	print(i, end="")
