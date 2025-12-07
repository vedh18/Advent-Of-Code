import numpy as np
input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

input = input_file.read()
ans = 0

input = [line.split() for line in input.split("\n")]

for i in range(len(input[0])):
    if input[4][i] == "*":
        ans += int(input[0][i]) * int(input[1][i]) * int(input[2][i]) * int(input[3][i])
    elif input[4][i] == "+":
        ans += int(input[0][i]) + int(input[1][i]) + int(input[2][i]) + int(input[3][i])
output_file.write(str(ans))