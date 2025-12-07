input_file = open("input.txt", "r")
output_file = open("output.txt", "w+")

input = input_file.read()
ans = 0
dial = 50
for line in input.split("\n"):
    if line[0] == 'R':
        temp = dial + int(line[1:])
        ans += temp // 100
        dial = temp % 100
    else:
        temp = dial - int(line[1:])
        if temp <= 0 and dial > 0:
            ans += 1
        ans += abs(temp) // 100
        dial = temp % 100
output_file.write(str(ans)) 