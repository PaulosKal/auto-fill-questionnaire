#program to generate random answers to a questionaire, based on probability given by the user for each possible answer

import random
import Functions.CheckValues as cv
import Functions.ClearScreen as cs


cs.ClearScreen()
print("Do you want to manually insert questions and probabilities for each answer?\n1. Yes\n2. No")
answer = cv.CheckValues("int", 1, 2, cv.low, cv.high)

if(answer == 1):  #manually inserted data
	probabilities = []
	stop_questions = False
	i = 0  #number of questions
	while(not stop_questions):
		i += 1
		probabilities.append([])
		cs.ClearScreen()
		print("Question no.", i)
		
		stop_answers = False
		j = 0  #number of answers
		total = 0
		while(not stop_answers):
			j += 1
			print("Type the percentage of answer no. {} or type 0 to reset answers: ".format(j))
			answer = cv.CheckValues("int", 0, 100 - total, cv.low, cv.high)
			if(answer == 0):
				probabilities[i - 1] = []
				j = 0
				total = 0
			else:
				total += int(answer)
				probabilities[i - 1].append(total)

			if(total >= 100):
				stop_answers = True  #no more answers for this question
		print("Next question?\n1. Continue\n2. Finish")
		answer = cv.CheckValues("int", 1, 2, cv.low, cv.high)
		if(answer == 2):
			stop_questions = True
else:  #prefilled array of data
	probabilities = [[61, 100], [45, 100], [10, 36, 100], [3, 13, 35, 78, 100], [32, 58, 100], [16, 55, 87, 97, 100], [26, 58, 71, 77, 90, 100], [45, 80, 93, 97, 100], [29, 42, 77, 93, 100], [10, 29, 68, 94, 100], [29, 55, 90, 97, 100], [3, 19, 51, 70, 100], [84, 90, 93, 93, 100], [25, 66, 85, 97, 100], [26, 52, 77, 90, 100], [52, 84, 94, 97, 100], [26, 61, 71, 93, 100], [3, 6, 29, 81, 100], [3, 3, 10, 35, 100], [77, 100], [42, 100], [45, 100], [58, 68, 100], [19, 58, 100], [19, 51, 100], [26, 71, 100], [32, 81, 100], [19, 45, 100], [32, 100]]

#create a votes array of zeros, same size as probabilities array
votes = []
for i in range(len(probabilities)):
	votes.append([])
	for j in range(len(probabilities[i])):
		votes[i].append(0)

print(probabilities)
print(votes)

letters = ["- a", "- b", "- c", "- d", "- e"]
n = int(input("Number of people: "))
for person in range(n):
	for question in range(len(probabilities)):
		temp = random.randint(1, 100)
		for answer in range(len(probabilities[question])):
			if(temp <= probabilities[question][answer]):
				votes[question][answer] += 1
				break
for question in range(len(probabilities)):
	if(question <= 6):
		print("\n\nQuestion {}:\n".format(question + 1))    
	elif(question >= 7 and question <= 11):
		print("\n\nQuestion 8 {}:\n".format(letters[question - 7]))
	elif(question >= 12 and question <= 16):
		print("\n\nQuestion 9 {}:\n".format(letters[question - 12]))
	elif(question >= 17 and question <= 22):
		print("\n\nQuestion {}:\n".format(question - 7))        
	elif(question >= 23 and question <= 27):
		print("\n\nQuestion 16 {}:\n".format(letters[question - 23]))
	else:
		print("\n\nQuestion {}:\n".format(question - 11))
	for answer in range(len(probabilities[question])):
		print("Answer {}: {} / {}%".format(answer + 1, votes[question][answer], int(votes[question][answer]/n*1000)/10))
input()