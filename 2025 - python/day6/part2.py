import numpy as np
input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

input = input_file.read()
ans = 0

input = input.split("\n")

i = 0
while i < len(input[0]):
    if input[4][i] == "*":
        temp = 1
        while i < len(input[0]) and str(input[0][i] + input[1][i] + input[2][i] + input[3][i]).strip() != "":
            temp = temp * int(str(input[0][i] + input[1][i] + input[2][i] + input[3][i]).strip())
            i+=1
        ans += temp
    elif input[4][i] == "+":
        temp = 0
        while i < len(input[0]) and str(input[0][i] + input[1][i] + input[2][i] + input[3][i]).strip() != "":
            temp = temp + int(str(input[0][i] + input[1][i] + input[2][i] + input[3][i]).strip())
            i+=1
        ans += temp
    i+=1
output_file.write(str(ans))