'''
# Algorithm: 		Binary Search
# Author: 			Caleb Palmquist (Palmquistador)
# Date:				07/17/2016
# Modified From:	https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/
'''

# Start with a list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Pick a target number in the list above
target = 13

# Set starting number from the list
low = 1

# Set the highest number fomr the list
high = len(numbers)

# Display the target number
print("\nTarget: " + str(target) + "\n")

# Keep looping until target number is found
while low <= high:
	# Calculate the middle number
	mid = int(low + (high - low) / 2)
	# If the middle number matches target, then success
	if numbers.index(mid) == target:
		print("\nTarget " + str(target) + " found!")
		break
	# Otherwise, get rid of half of the numbers
	elif numbers.index(mid) < target:
		# Display the current middle number
		print("Mid: " + str(mid))
		# Set low to the current middle number + 1
		# This effectively gets rid of all numbers before current mid + 1
		low = mid + 1
	else:
		# Same as low but for the highest number
		high = mid - 1