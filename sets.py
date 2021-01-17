mySet = {1, 2, 3}

mySet.add(4)
mySet.discard(2)


print(mySet)


for i in mySet:
    print(i)


if 1 in mySet:
    print("yes")


odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}


u = odds.union(evens)
print(u)

u = odds.intersection(primes)
print(u)


setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3, }
diffA = setA.difference(setB)
diffB = setB.difference(setA)
diffsym = setA.symmetric_difference(setB)

print(diffA)
print(diffB)
print(diffsym)


print(setB.issubset(setA))
print(setA.issuperset(setB))


a = frozenset([1, 2, 3, 4])
