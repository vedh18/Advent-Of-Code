import numpy as np
input_file = open("2025 - python\input.txt", "r")
output_file = open("2025 - python\output.txt", "w+")

input = input_file.read()
ans = 0

input = [line.split(",") for line in input.split("\n")]

parent = [i for i in range(1000)]
size = [1 for _ in range(1000)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

x = []
for i in range(len(input)):
    for j in range(i+1, len(input)):
        l1 = list(map(int, input[i]))
        l2 = list(map(int, input[j]))
        d = sum([(l1[k]-l2[k])**2 for k in range(3)])
        x.append([d, i, j])
x.sort()
for i in range(1000000):
    # print(x[i])
    union(x[i][1], x[i][2])
    flag = True
    for j in range(1, len(input)):
        if find(j) != find(0):
            flag = False
            break
    if flag:
        print(x[i])
        ans = int(input[x[i][1]][0]) * int(input[x[i][2]][0])
        break

output_file.write(str(ans))