import itertools
num = [1,2,3,4]
a = list(itertools.product(num,repeat=4))
b = list(itertools.permutations(num,r=4))
# print(a)
# print(b)
c = list(itertools.combinations(num,r=4))
d = list(itertools.combinations_with_replacement(num,r=4))
print(c)
print(d)