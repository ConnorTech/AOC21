#!/usr/bin/python3

previous = 0
count = 0
lower = 0
higher = 0
same = 0
f = open("input.txt", "r")
for n in f:
	n.strip()
	depth = int(n)
	if previous < depth:
		count += 1
		higher += 1
	elif previous > depth:
		lower += 1
	else:
		same += 1
	previous = depth
total = higher + lower + same
print("\nHigher: ", higher)
print("\nLower: ", lower)
print("\nSame: ", same)
print("\nTotal: ", total)
