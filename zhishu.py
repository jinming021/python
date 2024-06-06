#练习一：打印100以内质数

num = 2
for num in range(2,100):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        print("质数为：",num,end=" ")
