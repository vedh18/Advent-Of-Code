input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

input = input_file.read()
ans = 0
dial = 50
for line in input.split("\n"):
    if line[0] == 'R':
        dial = (dial + int(line[1:])) % 100
    else:
        dial = (dial - int(line[1:]) + 100) % 100
    if dial == 0:
        ans += 1
output_file.write(str(ans))