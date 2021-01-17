myDict = {"name": "Max", "age": 28, "city": "New York"}
print(myDict)


myDict2 = dict(name="Mary", age=27, city="Boston")
print(myDict2['name'])


myDict['email'] = 'john@mail.com'
print(myDict)

myDict['email'] = 'johnaaa@mail.com'
print(myDict)


del myDict['name']
print(myDict)


myDict.pop('email')
print(myDict)


if "age" in myDict:
    print(myDict['age'])

try:
    print(myDict['age'])
except:
    print('Error')


for key, value in myDict2.items():
    print(key, value)

myDict_cpy = myDict.copy()


myDict.update(myDict2)

print(myDict)


my_dict = {3: 9, 6: 36}

print(my_dict[3])


myTuple = 8, 7
myDict = {myTuple: 15}

print(myTuple)
print(myDict)
