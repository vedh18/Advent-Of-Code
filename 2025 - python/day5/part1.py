import numpy as np
input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

input = input_file.read()
ans = 0

i = 0
input = input.split("\n")
rng = list()
while input[i] != "":
    # print(input[i].split("-"))
    rng.append(input[i].split("-"))
    i+=1
i+=1
for j in range(i, len(input)):
    for r in rng:
        if int(input[j]) >= int(r[0]) and int(input[j]) <= int(r[1]):
            ans += 1
            break
output_file.write(str(ans))