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
	#print(f"Total stones: {sum}")
	
part1()
part2()
	 

