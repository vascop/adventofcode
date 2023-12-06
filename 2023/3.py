import collections
import math

engine = open('3.input.txt').read()
schematiclen = engine.find('\n')
oneliner = engine.replace('\n', '')

it = 0
currentpart = ""
hit = 0
allhits = 0
gear = 0
gearloc = -1
gearhits = collections.defaultdict(list)

while it < len(oneliner):
	if oneliner[it].isdigit():
		currentpart += oneliner[it]
		rightbound = oneliner.find('.', it) - 1

		topleft = it - (schematiclen + 1)
		topright = it - (schematiclen - 1)
		bottomleft = it + (schematiclen - 1)
		bottomright = it + (schematiclen + 1)

		crossup = it - schematiclen
		crossleft = it - 1
		crossright = it + 1
		crossdown = it + schematiclen

		adjacents = [topleft, crossup, topright, crossright, bottomright, crossdown, bottomleft, crossleft]
		adjacents = list(filter(lambda x: x > 0 and x < len(oneliner), adjacents))

		if not hit:
			for adj in adjacents:
				if not oneliner[adj].isdigit() and oneliner[adj] != '.':
					hit = 1
					if oneliner[adj] == '*':
						gear = 1
						gearloc = adj
	else:
		if hit:
			allhits += int(currentpart)
			if gear:
				gearhits[gearloc].append(int(currentpart))
				gear = 0
				gearloc = -1
		hit = 0
		currentpart = ""
	it += 1

print(allhits)

sumratios = 0
for gear in gearhits:
	if len(gearhits[gear]) == 2:
		sumratios += math.prod(gearhits[gear])
print(sumratios)