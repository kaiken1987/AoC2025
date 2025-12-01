import math

#f = open("example.txt", "r")

f = open("input.txt", "r")


def part1():
	print( "Part 1")
	dial = 50
	zeros = 0
	
	for line in f:
		change = int(line[1:-1])
		if (line[0] == 'R' ): #Right -> add
			dial += change
		elif(line[0] == 'L') :
			dial -= change
		else:
			break
		dial = dial%100
		if( dial == 0 ):
			zeros+=1
				
	print(f"Password is: {zeros}")


def part2():
	print( "Part 2")
	dial = 50
	zeros = 0
	f.seek(0)
	for line in f:
		change = int(line[1:])
		if (change>100):
			zeros += int((change / 100))
			change = change%100
		if (line[0] == 'R' ): #Right -> add
			if( dial+change >= 100 ):
				zeros+=1
			dial += change
		elif(line[0] == 'L') :
			if( dial-change < 0 ) and (dial!=0):
				zeros+=1
			dial -= change
		else:
			break
		if( dial == 0 ):
			zeros+=1
		dial = dial%100
	print(f"Password is: {zeros}")
	
part1()
part2()
	 

