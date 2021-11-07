# print("""\\    /\\
#  )  ( ')
# (  /  )
#  \\(__)|""")

# answer = int(input())
# if answer%4 == 0 and answer%100 != 0:
#     print("1")
# elif answer%400 == 0:
# 	print("1")
# else:
#     print(0)

# answer_one = int(input())
# answer_two = int(input())
# if answer_one !=0 and answer_two !=0:
# 	if answer_one > 0:
# 		if answer_two > 0:
# 			print(1)
# 		else:
# 			print(4)
# 	else:
# 		if answer_two > 0:
# 			print(2)
# 		else:
# 			print(3)

# answer = input().split(" ")
# answer = [int(i) for i in answer]
# a = answer[0]
# b = answer[1]-45
# if b<0:
# 	if a == 0 :
# 		a = 24
# 	a = a-1
# 	b = b+60
# print(a,b)

# import sys
# the_num = int(sys.stdin.readline())
# count = 0
# answer_list = []
# while count != the_num:
# 	count+=1
# 	answer = sys.stdin.readline().split(" ")
# 	answer = [int(i) for i in answer]
# 	answer_list.append(answer[0]+answer[1])
# for i in answer_list:
# 	print(i)

# import sys
# a = int(sys.stdin.readline())
# b = list(range(1,a+1))
# b.sort(reverse=True)
# print(b)

# a= int(input())
# for i in range(1,a+1):
# 	print(("*"*i).rjust(a))

# a = input().split(" ")
# a = [int(i) for i in a]
# the_num = a[0]
# s = a[1]
# b = input().split(" ")
# b = [int(i) for i in b]
# if len(b) == the_num:
# 	list_list = []
# 	for i in b:
# 		if i < s:
# 			print(i,end=" ")

# a = input()	
# first = int(a)
# if first <10:
# 	a = f"0{a}"
# a = [int(i) for i in a]
# count = 0
# while True:
# 	count +=1
# 	b = a[1]
# 	c = a[0]+a[1]
# 	if c >= 10:
# 		c -=10
# 	d = f"{b}{c}"
# 	if int(d) == first:
# 		print(count)
# 		break
# 	else:
# 		a = [int(i) for i in d]

# count = 0
# a_list = []
# while count != 9:
# 	count+=1
# 	a = int(input())
# 	a_list.append(a)
# a_list_sort = sorted(a_list)
# print(a_list_sort[-1],a_list.index(a_list_sort[-1])+1)
	
# a = int(input())
# b = int(input())
# c = int(input())
# wow = str(a*b*c)
# for i in range(10):
# 	print(wow.count(str(i)))
#1차원배열
