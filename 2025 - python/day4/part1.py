import numpy as np
input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

input = input_file.read()
ans = 0

grid = input.split("\n")
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            c = -1
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if k >= 0 and l >= 0 and k < len(grid) and l < len(grid[0]):
                        if grid[k][l] == "@":
                            c += 1
            if c < 4:
                ans += 1
output_file.write(str(ans))