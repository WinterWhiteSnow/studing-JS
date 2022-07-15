import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

for i in range(1,31):
    wow = open(f"C:\\Users\\선옥\\Desktop\\코딩\\JS\\파이썬 백준\\2022\\11월\\{i}.py","a",encoding="utf8")
    wow.write("import sys")
    wow.write("\n")
    wow.write("\ninputing = lambda : sys.stdin.readline().rstrip()")
    wow.write("\nwow = lambda : map(int,inputing().split())")
    wow.write("\none = lambda : int(inputing())")
    






