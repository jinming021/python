Python学习小结

#Version 0.1 2024-06-07 Jin Ming Change History First draft version
#Refer:https://pythonexamples.org/python-datatypes/
#Refer:https://jgirl.ddns.net/VisualCode/live.html#mode=edit
#Refer:https://github.com/jinming021



1. 数据类型
    (1)数字numeric
        1)整形int()
        2)浮点型float()
        3)布尔型bool()
        4)复数complex()
    (2)字符串string：str()
    (3)列表list()
    (4)元组tuple()
    (5)集合set
    (6)字典dictionary

2. 语句语法
    (1)条件判断语句
        if...elif...else
    (2) 循环语句
        1)for循环
            for i in range(10):
        2)while循环
            while...
        3)range/break/continue

3. 列表
    (1)创建列表
        list1 = [1, 2, 3, 4, 5]
        list2 = ['apple', 'banana', 'orange']
        list3 = [1, 'apple', 3.14, True]
    (2)访问列表元素
        list1[0]
        list2[1]
    (3)修改列表元素
        list1[0] = 10
        list2[1] = 'grape'
    (4)列表长度
        len(list1)
    (5)列表切片
        list1[1:3]
        list2[1:]
    (6)列表方法
        list1.append(6)
        list1.insert(1, 10)
        list1.remove(10)
        list1.pop()
        list1.sort()
        list1.reverse()
        list1.count(1)
        list1.index(1)

4. 字典
    (1)创建字典
        dict1 = {'name': 'Jin', 'age': 25, 'city': 'Beijing'}
        dict2 = {'name': 'Ming', 'age': 20, 'city': 'Shanghai'}
    (2)访问字典元素
        dict1['name']
        dict2['age']
    (3)修改字典元素
        dict1['name'] = 'JinMing'
        dict2['age'] = 21
    (4)字典长度
        len(dict1)
    (5)字典方法
        dict1.keys()
        dict1.values()
        dict1.items()
        dict1.get('name')
        dict1.pop('name')
        dict1.update({'gender': 'Male'})

