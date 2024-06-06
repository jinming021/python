#3)Copy模块 - 浅拷贝 - shallow copy
import copy
a = [1,2,3,[4,5,6]]
b = copy.copy(a)
print(a)
print(b)

a[3] = 100

print(a)
print(b)