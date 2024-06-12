#列表list
#https://www.processon.com/mindmap/6669018e0d53821802b910e2


#创建一个新的空列表
list1 = []
print(list1)

#创建一个新的列表
list1 = [1,2,3,4,5]
print(list1)

#元组转换列表
list1 = list(("a","b","c","d"))
print(list1)

list1 = list(range(0,10))
print(list1)

#添加列表
list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
print(list1)

#for循环添加列表
list1 = []
for i in range(0,10):
    list1.append(i)
print(list1)

#扩展列表
list1 = []
list1.extend([1,2,3])
list1.extend([4,5,6])
print(list1)

#插入列表
list1 = []
list1.insert(0,1)
list1.insert(1,2)
list1.insert(2,3)
list1.insert(3,4)
list1.insert(4,5)
print(list1)

#访问列表
list1 = [1,2,3,4,5,6,7,8,9]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[-1])
print(list1[-2])
print(list1[-3])

#列表切片
list1 = [1,2,3,4,5,6,7,8,9]
print(list1[1:2])
print(list1[:2])
print(list1[2:])
print(list1[:])
print(list1[::2])
print(list1[1::2])
print(list1[::-1])

#遍历列表
list1 = [1,2,3,4,5,6,7,8,9]
for i in list1:
    print(i)
#列表推导式
[print(i) for i in list1 if i%2==0]

#更新列表
list1 = ["Apple","Facebook","Tecent","Baidu","Xiaomi"]
print(list1)
list1[2] = "Alibaba"
print(list1)
list1[-2] = "Microsoft"
print(list1)

#删除列表
list1 = [1,2,3,4,5]
print(list1)
list1.remove(1)
print(list1)
list1 = ["Apple","Facebook","Tecent","Baidu","Xiaomi"]
print(list1)
list1.remove("Apple")
print(list1)

#弹出列表
list1 = [1,2,3,4,5]
print(list1)
list1.pop()
print(list1)
list1.pop(1)
print(list1)

#清空列表
list1 = [1,2,3,4,5]
print(list1)
list1.clear()
print(list1)

#删除列表
list1 = [1,2,3,4,5]
print(list1)
del list1[0]
print(list1)
del list1
#print(list1)

#列表操作
#统计
list1 = [1,2,2,2,2,3,4,5]
print(list1.count(2))

#排序
list1 = [1,2,3,4,5,6]
list1.sort(reverse=True)
print(list1)
list1.sort()
print(list1)

list1 = ["Apple","Facebook","Tecent","Baidu","Xiaomi"]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
print(sorted(list1))

#翻转
list1 = ["Apple","Facebook","Tecent","Baidu","Xiaomi"]
list1.reverse()
print(list1)

#索引
list1 = ["Apple","Facebook","Tecent","Baidu","Xiaomi"]
print(list1.index("Tecent"))

#拷贝
list1 = [1,2,3,4,5]
list2 = list1.copy()
print(list1)
print(list2)
list1[2] = 100
print(list1)
print(list2)
list2[3] = 200
print(list1)
print(list2)

#拼接
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = list1 + list2
print(list3)
list1.extend([list2])
print(list1)

#重复
list1 = [1,2,3]
print(list1 * 3)

#列表运算
#比较
list1 = [1,2,3]
list2 = [4,5,6]
print(list1 == list2)
print(list1 > list2)
print(list1 < list2)

list1 = ["a","b","c"]
list2 = ["d","e","f"]
print(list1 == list2)
print(list1 > list2)
print(list1 < list2)

print(["a","b"] == ["a","b"] and ["A","B"] == ["A","b"])
print(["a","b"] == ["a","b"] or ["A","B"] == ["A","b"])


#判断
list1 = ["a","b","c","d"]
print("a" in list1)
print("e" in list1)
print("b" not in list1)
print("e" not in list1)


list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1
print(list1)
print(list2)
print(list3)
print(list1 is list2)
print(list1 is list3)
print(list1 == list2)
print(list1 == list3)

print(iter(list1))
print(iter(list2))
print(iter(list3))
print(id(list1))
print(id(list2))
print(id(list3))


list1 = ["a","b","c"]
list2 = ["a","b","c"]
list3 = list1
print(list1)
print(list2)
print(list3)
print(list1 is list2)
print(list1 is list3)
print(list1 == list2)
print(list1 == list3)
print(iter(list1))
print(iter(list2))
print(iter(list3))
print(id(list1))
print(id(list2))
print(id(list3))

#列表函数
#长度
list1 = [1,2,3,4,5,6,7,8,9]
print(len(list1))

#类型
list1 = [1,2,3,4,5,6,7,8,9]
print(type(list1))

#转换列表
print(list(("a","b","c","d","e","f")))

#最大值
list1 = [1,2,3,4,5,6]
print(max(list1))

#最小值
list1 = [1,2,3,4,5,6]
print(min(list1))

#排序
list1 = ["a","b","d","1","2"]
print(sorted(list1))

#去重复
list1 = [1,2,3,3,4,5,5,6,]
print(set(list1))


#列表嵌套
list1 = [1,2,3,[4,5,6]]
print(list1)
print(list1[0])
print(list1[-1])
print(len(list1))

#二维列表
list1 = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(list1)
print(list1[0])
print(list1[0][0])

list2 = []
for i in list1:
    for j in i:
        list2.append(j)
print(list2)


#map
name = ["小明","小红","小刚"]
score = [85,76,95]


#列表推导式
list1 = [1,2,3,4,5,6,7,8,9]
print([i**2 for i in list1 if i%2==0])
print([i**2 for i in list1 if i%2!=0])

list2 = [i**2 for i in range(0,10)]
print(list2)

list1 = [[1,2,3],
         [4,5,6],
         [7,8,9]]

list2 = []

for i in list1:
    for j in i:
        list2.append(j)
        print(list2)


list1 = [[1,2,3],
         [4,5,6],
         [7,8,9]]
list2 = [i for j in list1 for i in j]
print(list2)


