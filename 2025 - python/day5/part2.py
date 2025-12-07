import numpy as np
input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

input = input_file.read()
ans = 0

i = 0
input = input.split("\n")
rng = list()
while i < len(input) and input[i] != "":
    # print(input[i].split("-"))
    rng.append([int(input[i].split("-")[0]), int(input[i].split("-")[1])])
    i+=1

rng.sort()
i = 0
while i < len(rng):
    j = i+1
    while j < len(rng) and rng[j][0] <= rng[j-1][1]:
        rng[j][1] = max(rng[j][1], rng[j-1][1])
        j += 1
    ans += rng[j-1][1] - rng[i][0] + 1
    i = j

output_file.write(str(ans))