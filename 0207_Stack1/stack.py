import sys

a = []
print(sys.getsizeof(a))
a.append(1)
print(sys.getsizeof(a))
a.append(2)
print(sys.getsizeof(a))
a.append(3)
print(sys.getsizeof(a))