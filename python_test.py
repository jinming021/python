"""
1. 请编程找出矩阵中的幸运数字.
说明：假设给定一个 m * n 的矩阵（矩阵中数值的取值范围是 0~1024，且各不相同），
如果某一个元素的值在同一行的所有元素中最小，并且在同一列的所有元素中最大，那么该元素便是幸运数字。
假设给定的矩阵如下：
matrix = [[10, 36, 52],
          [33, 24, 88],
          [66, 76, 99]]
          
那么输出结果应该是 66（同时满足同一行的所有元素中最小，并且在同一列的所有元素中最大）。
"""

import random
matrix = []

for m in range(3):
    matrix.append([])
    for n in range(3):
        matrix[m].append(random.randint(0,1024))
print(matrix)

for m in range(3):
    min_num = min(matrix[m])
    max_num = max(matrix[i][m] for i in range(3))
    if min_num == max_num:
        print(min_num)


