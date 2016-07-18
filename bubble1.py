'''
# Algorithm: 		Bubble Sort (Simple)
# Author: 			Caleb Palmquist (Palmquistador)
# Date:				07/18/2016
# Modified From:	https://www.topcoder.com/community/data-science/data-science-tutorials/sorting/
'''

numbers = [9,5,4,6,7,3,2,1,8,10]

print("\nUnsorted Numbers:\n" + str(numbers))

for i in range(0, len(numbers)):

	for j in range(0, len(numbers) - 1):

		# If 9 > 5
		if numbers[j] > numbers[j + 1]:

			# Assign current index value to tmp, i.e. 9
			tmp = numbers[j]
			#print("\ntmp = " + str(tmp))

			# Value of index j in list is now equal to the value of the next index
			# i.e., 9 now equals 5
			numbers[j] = numbers[j + 1]

			# The next index in the list now equals the old first value
			# i.e., 9 now = 5 and 5 now = 9
			numbers[j + 1] = tmp

print("\nSorted Numbers:\n" + str(numbers))