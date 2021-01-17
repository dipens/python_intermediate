myList = ['banana', 'cherry', 'apple']
print(myList)


item = myList[-1]
print(item)


for i in myList:
    print(i)


if 'banana' in myList:
    print('Yes')
else:
    print('No')

print(len(myList))


myList.append('lemon')

print(myList)


myList.insert(2, 'blueberry')


print(myList)


print(myList.pop())


print(myList)


item = myList.remove('cherry')
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)


new_list = sorted(myList)
print(myList)
print(new_list)


myList = [0] * 5
print(myList)


myList2 = [1, 2, 3, 4, 5]
new_list = myList + myList2

print(new_list)


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = myList[::-1]
print(a)


list_org = ['banana', 'orange', 'cherry']
list_cpy = list_org.copy()
list_cpy.append('lemon')

print(list_cpy)
print(list_org)


myList = [1, 2, 3, 4, 5, 6]
b = [i*i*i for i in myList]

print(myList)
print(b)
