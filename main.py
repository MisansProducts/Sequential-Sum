#Made by Alex

#======Libraries======
import random
import time
import copy

#======Functions======
#List Generator Function
def genList(size):
	l = [] #Initializes empty list

	#Populates list with random integers
	for i in range(size):
		l.append(random.randint(-size, size))
	
	#Returns populated list
	return l

#Print Result Function
def printResult(t):
	#Assumes t is a tuple where index 0 is a list of numbers and index 1 is an integer

	#List contains more than 1 number
	if len(t[0]) > 1:
		#Loops through the list of numbers (not the last)
		for i in range(len(t[0]) - 1):
			#Gets number at current index
			tempNum = t[0][i]

			#Negative number
			if tempNum < 0:
				print(f"({t[0][i]})", end = " + ")
			#Positive number
			else:
				print(t[0][i], end = " + ")
		#Prints last number
		print(t[0][-1], end = " = ") #This number will always be positive
	#Prints max sum
	print(t[1], "is the largest contiguous sum")

#Cubic Function
def cubic(l):
	maxSum = 0 #Initializes max sum
	maxSequence = [] #Initializes max sequence

	#Loops through list (starting index)
	for i in range(len(l)):
		#Loops through list (ending index)
		for j in range(i, len(l)):
			#Resets current sum and current sequence list
			currentSum = 0
			currentSequence = []

			#Loops through range
			for k in range(i, j + 1):
				currentSum += l[k] #Sums numbers
				currentSequence.append(l[k]) #Appends numbers to sequence list
			
			#Comparison
			if currentSum >= maxSum:
				maxSum = currentSum
				maxSequence = copy.deepcopy(currentSequence)
	return maxSequence, maxSum

#Quadratic Function
def quadratic(l):
	maxSum = 0 #Initializes max sum
	maxSequence = [] #Initializes max sequence

	#Loops through list (starting index)
	for i in range(len(l)):
		#Resets current sum and current sequence list
		currentSum = 0
		currentSequence = []

		#Loops through list
		for j in range(i, len(l)):
			currentSum += l[j] #Sums numbers
			currentSequence.append(l[j]) #Appends numbers to sequence list

			#Comparison
			if currentSum >= maxSum:
				maxSum = currentSum
				maxSequence = copy.deepcopy(currentSequence)
	return maxSequence, maxSum

#Linear Function
def linear(l):
	#Variables
	maxSum = 0 #Initializes max sum
	maxSequence = [] #Initializes max sequence
	currentSum = 0 #Current sum
	currentSequence = [] #Current sequence

	#Loops through list
	for i in range(len(l)):
		currentSum += l[i] #Sums numbers
		currentSequence.append(l[i]) #Appends numbers to sequence list

		#Comparison
		if currentSum >= maxSum:
			maxSum = currentSum
			maxSequence = copy.deepcopy(currentSequence)
		elif currentSum < 0:
			currentSum = 0
			currentSequence = []
	return maxSequence, maxSum

#======Main======
def main():
	#Enter Input Loop
	while True:
		#List length input
		try:
			#Prompt
			listLength = float(input("Please enter the list size: "))

			#Bad inputs
			if listLength < 0:
				raise Exception("List size cannot be negative!")
			elif listLength == 0:
				raise Exception("List size must be greater than 0!")
			elif listLength.is_integer() == False:
				raise Exception("List size cannot be floating point values.")
		#Error handling (general)
		except ValueError:
			print("The list size must be a natural number.\n")
		#Error handling (specific)
		except Exception as specificError:
			print(specificError, end = "\n\n")
		#Exit Input Loop
		else:
			listLength = int(listLength)
			print() #Spacer
			break
	
	#Generates a list of random integers of size listLength
	myList = genList(listLength)

	#Prints list
	print("LIST:")
	for i in range(listLength - 1):
		print(myList[i], end = ", ")
	print(myList[-1], end = "\n\n")

	#Gets the largest contiguous sum
	#Time complexity of O(N^3)
	start = time.time() #Gets starting time
	response = cubic(myList)
	end = time.time() #Gets ending time
	cubicTime = end - start
	print("-=-=-=Run time complexity of O(N^3)=-=-=-")
	printResult(response)
	print("Time elapsed:", cubicTime)

	print() #Spacer

	#Time complexity of O(N^2)
	start = time.time() #Gets starting time
	response = quadratic(myList)
	end = time.time() #Gets ending time
	quadraticTime = end - start
	print("-=-=-=Run time complexity of O(N^2)=-=-=-")
	printResult(response)
	print("Time elapsed:", quadraticTime)

	print() #Spacer

	#Time complexity of O(N)
	start = time.time() #Gets starting time
	response = linear(myList)
	end = time.time() #Gets ending time
	linearTime = end - start
	print("-=-=-=Run time complexity of O(N)=-=-=-")
	printResult(response)
	print("Time elapsed:", linearTime)

#======Execution Check======
if __name__ == '__main__':
	main()