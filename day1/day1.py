import re

file = open('day1', 'r')
lines = [line.rstrip() for line in file]
digits = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
totParte1 = 0 
totParte2 = 0 

def parte1(lines):
	somma = 0
	for line in lines:
		num = [c for c in line if c.isnumeric()]
		somma += int(num[0]+num[-1])
	return somma

def parte2(lines):
	somma = 0
	r = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
	pattern = re.compile(r)
	for line in lines:
		words = []
		for word in pattern.findall(line):
			if(word in digits):
				words.append(str(digits[word]))
			else: words.append(word)			
		somma += int(words[0]+words[-1])
	return somma

totParte1 = parte1(lines)
totParte2 = parte2(lines)
print("parte1: ", totParte1)
print("parte2: ", totParte2)
