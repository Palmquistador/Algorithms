'''
# Algorithm: 		Binary Search (Random Target (1-1000))
# Author: 		Caleb Palmquist (Palmquistador)
# Date:			07/17/2016
# Modified From:	https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/
'''

import random

# Empty list
numbers = []

# Add the numbers from 1 to 1000 to the list
for i in range (1,1001):
	numbers.append(i)

# Overkill but just for fun
def getRandomNumber(theList):

	# Pick a random number from the list to be our target
	target = random.randint(theList[0], theList[-1])

	#Print the list range and target number
	print("\nBetween " + str(theList[0]) + " and " + str(theList[-1]) + ", the random target is " + str(target) + "!\n")

	return target

# Get a random number between 1 and 1000
target = getRandomNumber(numbers)

# Set number of loops
loops = 0

# Set starting number from the list
low = numbers[0]

# Set the highest number from the list
high = numbers[-1]

# Keep looping until target number is found
while low <= high:
	# Increase the loop count
	loops += 1
	# Calculate the middle number, int() rounds down
	mid = int(low + (high - low) / 2)
	# If the middle number matches target, then success
	if mid == target:
		print("\nTarget " + str(target) + " found!")
		print("\nIt took " + str(loops) + " loops to find the answer!")
		break
	# Otherwise, get rid of half of the numbers
	elif mid < target:
		# Display the current middle number
		print("Mid: " + str(mid))
		# Set low to the current middle number + 1
		# This gets rid of all the numbers before the current mid
		low = mid + 1
	else:
		print("Mid: " + str(mid))
		# Same as low but for the highest number
		high = mid - 1
