import re

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
sumis = 0

for line in open('1.input.txt'):
    # part 2
    for num, digit in enumerate(digits):
        line = line.replace(digit, "{}{}{}".format(digit[0], num+1, digit[-1]))

    # part 1
    numbers = re.findall(r'\d', line)
    readout = numbers[0] + numbers[-1]
    sumis += int(readout)
print("{}".format(sumis))