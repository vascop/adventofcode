# part 1
goals = {'red': 12, 'green': 13, 'blue': 14}
sumis = 0

for gameno, line in enumerate(open('2.input.txt')):
	failed = 0
	for draw in line.split(':')[1].split(';'):
		for picked in draw.split(','):
			number, color = picked.strip().split(' ')
			if goals[color] < int(number): # too many
				failed = 1
				break
	if failed == 0: 
		sumis += gameno+1
print(sumis)


# part 2
import math

sumis = 0

for gameno, line in enumerate(open('2.input.txt')):
	maxseen = {}
	power = 0
	for draw in line.split(':')[1].split(';'):
		for picked in draw.split(','):
			number, color = picked.strip().split(' ')
			if int(number) > maxseen.get(color, 0):
				maxseen[color] = int(number)
	sumis += math.prod(maxseen.values())
print(sumis)