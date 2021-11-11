# the_num = int(input())
# a = [i for i in input()]
# if len(a) == the_num:
#     a = [int(i) for i in a]
#     print(sum(a))

# import string 

# a = [i for i in string.ascii_lowercase]
# a_dict={}
# for i in range(len(a)):
#     a_dict[a[i]]=i
# b = [i for i in input()]
# for i in a_dict.keys():
#     if i in b:
#         c = b.index(i)
#     else:
#         c = -1
#     print(c,end=" ")

# the_num = int(input())
# count = 0
# a_list = []
# while count != the_num:
#     count+=1
#     a = input().split(" ")
#     repeat = int(a[0])
#     aa=[]
#     for i in range(len(a[-1])):
#         aa.append(a[-1][i]*repeat)
#     a_list.append(aa)
# a_list = ["".join(i) for i in a_list]
# for i in a_list:
#     print(i)

# import string
# a = [i for i in string.ascii_uppercase]
# b = [i for i in input().upper()]
# wow_list = {}
# for i in a:
#     wow = b.count(i)
#     if wow >0:
#         wow_list[i]=wow
# c = sorted(wow_list.items(), key = lambda x : x[1])
# if len(c) < 2:
#     print(c[-1][0])
# else:
#     if c[-1][-1] == c[-2][-1]:
# 	    print("?")
#     else:
#     	print(c[-1][0])

# a=input().split()
# print(len(a))

# a = [i for i in input().split()]
# b = int(a[0][::-1])
# c = int(a[1][::-1])
# wow = [b,c]
# wow.sort()
# print(wow[-1])

# import string
# wow = string.ascii_uppercase
# a = wow[:wow.find("P")]
# b = wow[wow.find("P"):]
# al_list = []
# for i in range(0,len(a)+1,3):
#     if a[i-3:i]:
#     	al_list.append(a[i-3:i])
# al_list.append(b[:b.find("S")+1])
# al_list.append(b[b.find("T"):b.find("V")+1])
# al_list.append(b[b.find("W"):])
# al_dict = {}
# for i in range(len(al_list)):
# 	a = i+2
# 	al_dict[al_list[i]]=a
# answer = [i for i in input()]
# count=0
# for i in answer:
#     for a in al_dict.keys():
#         if i in a:
#             count+=al_dict[a]+1
# print(count)

# cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]
# answer = input()
# count=0
# for i in cro:
#     if i in answer:
#         answer = answer.replace(i,"W")
# print(len(answer))

# the_num = int(input())
# count = 0
# wow = 0
# while count != the_num:
# 	count+=1
# 	answer = input()
# 	list_list = []
# 	a = set([i for i in answer])
# 	for i in a:
# 		start = answer.find(i)
# 		end = answer.rfind(i)
# 		ex = answer[start:end+1].replace(i,"")
# 		if len(ex) == 0:
# 			list_list.append("True")
# 		else:
# 			list_list.append("False")
# 	if "False" not in list_list:
# 		wow+=1
# print(wow)

# 백준 랭크시스템 solved.ac 알게됨 22350위 실버4
#문자열까지 끝냄
# 클래스 남은문제 풀어봄

# a = [int(i) for i in input().split(" ")]
# b = list(range(1,9))
# c = sorted(b,reverse=True)
# if a == b:
#     print("ascending")
# elif a == c:
#     print("descending")
# else:
#     print("mixed")

# a = [int(i) for i in input().split(" ")]
# for i in range(len(a)):
#     a[i] = a[i]**2
# print(sum(a)%10)

answer = [int(i) for i in input().split(" ")]
height = answer[0]
length = answer[1]
count = 0
color = 0
while count != height:
	count+=1
	a = input()
	if count <9:
		if len(a) >8:
			color_dict = {}
			color_dict["B"]=a.rfind("B")-a.find("B") 
			color_dict["W"]=a.rfind("W")-a.find("W")
			print(color_dict)

# 		wow = [a.count("W"),a.count("B")]
# 		wow.sort(reverse=True)
# 		print(wow)
# 		if wow[0] != wow[1]:
# 			color+=wow[0]-4
# print(color)

     
  
