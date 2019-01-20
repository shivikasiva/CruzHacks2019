import json
from firebase import firebase
firebase = firebase.FirebaseApplication('https://collegebox-3a06d.firebaseio.com', None)


def init_user(name, college, userid):
	data = {'name': name, 'college': college, 'userid': userid} 
	sent = json.dumps(data)
	result = firebase.post("/users", sent)

#init_user('bob', 'UCSC', '0')
#init_user('alice', 'UCSC', '1')
#init_user('joe', 'UCSB', '2')
#init_user('lilly', 'UCLA', '3')

result = firebase.get('/users', '-LWcJ-7nvaKHi5l4saRa')
print(result)



#-------------------------------------------------------------------------------------------------


#Assume variables have been acquired from firebase
#Temporary variables


numClasses = 2
class1 = event(start1, end1, frequency1)
class2 = event(start2, endT2, frequency2)
weekendwakeUpTime = 9

#Finds earliest course of the day
def findEarliestTime(currentDay):
	earliestStart = 24
	if currentDay < 5:
		if currentDay % 2 == (class1.frequency + 1) % 2:
			if class1.start <  earliestStart:
				earliestStart = class1.start
		elif currentDay % 2 == (class2.frequency + 1) % 2:
			if class2.start <  earliestStart:
				earliestStart = class2.start
	return earliestStart


#Decides what time the user should go to sleep 
def computeSleepTime(currentDay):
	earliestStart = 24
	# for each day, find sleep time based on frequency of the course 
	#if next day is a weekend, sleep time is 
	if currentDay >= 5:
		return wakeUpTime - 9

	else:
		time = findEarliestTime(currentDay)
		if time < 11:
			# one hour to get ready
			return findEarliestTime(currentDay) - 10 
		else:
			return 0


#Returns the time that the user is supposed to wake up 
def wakeUpTime(currentDay):
	return computeSleepTime(currentDay) + 9


def breakfastTime(currentDay):
	return wakeUpTime(currentDay) + 0.5


#---------------------------------------------------------

#"main" 

#Compute schedule for each day
def createWeeklySleepSchedule():
	i = 0
	while i < 7:
		i+=1
		#send firebase the wakeup time
		wakeUpTime(i)
		computeSleepTime(i)
		breakfastTime(i)
		return 0





