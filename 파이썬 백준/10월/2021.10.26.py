answer = input().split(" ")
answer = [int(i) for i in answer]
start = answer[0]
end = answer[1]
dict_list = {}
for i in range(2,end+1):
	if i == 1:
		pass
	elif i not in dict_list:
		for a in range(i,end+1,i):
			dict_list[a]=0
		dict_list[i]=1
for key,value in dict_list.items():
	if key >=start and value == 1:
		print(key)

