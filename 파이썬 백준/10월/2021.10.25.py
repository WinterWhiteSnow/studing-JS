answer = input().split(" ")
answer = [int(i) for i in answer]
start = answer[0]
end = answer[1]
answer_list = set()
for a in range(1,1000000+1):
	answer_list.add(a)
	for i in range(2,int(a/2)+1):
		if a%i == 0:
			try:
				answer_list.remove(a)
			except:
				pass
for a in range(start,end+1):
	try:
		answer_list = list(answer_list)
		if answer_list[0] == 1:
			answer_list = answer_list[1:]
		print(answer_list[afnswer_list.index(a)])
	except:
		pass

# for a in range(start, end+1):
	