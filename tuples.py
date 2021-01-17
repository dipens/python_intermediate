import sys
import timeit

myTuple = 'Max', 28, 'Boston',
print(myTuple)


myTuple2 = tuple(['Max', 28, 'Boston'])
print(myTuple2)


item = myTuple2[0]
print(item)


print(len(myTuple2))


my_list = list(myTuple)
print(my_list)

myTuple = tuple(my_list)
print(myTuple)


a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[::2]
print(b)


my_tuple = "Max", 28, "Boston"


name, age, city = my_tuple


print(name)
print(city)
print(age)


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


i1, *i2, i3 = my_tuple

print(i1)
print(i3)
print(i2)


my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")


print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))
