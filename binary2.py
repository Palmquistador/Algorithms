'''
# Algorithm: 		Binary Search 2
# Author: 			Caleb Palmquist (Palmquistador)
# Date:				07/17/2016
# Modified From:	https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/
'''

import random

# Empty list
numbers = []

# Add the numbers from 1 to 100 to the list
for i in range (1,101):
	numbers.append(i)

# Pick a random number from the list to be our target
target = random.randint(1, 100)

print("The random target is: " + str(target) + "!\n")

# Set starting number from the list
low = 1

# Set the highest number from the list
high = len(numbers)

# Keep looping until target number is found
while low <= high:
	# Calculate the middle number
	mid = int(low + (high - low) / 2)
	# If the middle number matches target, then success
	if mid == target:
		print("\nTarget " + str(target) + " found!")
		break
	# Otherwise, get rid of half of the numbers
	elif mid < target:
		# Display the current middle number
		print("Mid: " + str(mid))
		# Set low to the current middle number + 1
		# This effectively gets rid of all numbers before current mid + 1
		low = mid + 1
	else:
		print("Mid: " + str(mid))
		# Same as low but for the highest number
		high = mid - 1