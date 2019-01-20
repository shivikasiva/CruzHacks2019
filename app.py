import pyrebase
import datetime


config = {
	"apiKey": "AIzaSyAxrGj0wZa7MY9cawGxV8ee3woJElS6VOo",
    "authDomain": "cruzhacks2019-96ac5.firebaseapp.com",
    "databaseURL": "https://cruzhacks2019-96ac5.firebaseio.com",
    "projectId": "cruzhacks2019-96ac5",
    "storageBucket": "cruzhacks2019-96ac5.appspot.com",
   "messagingSenderId": "550382470877"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
#db.child("names").child("class1").push({"start1" : "9"})
#db.child("names").update({"name" : "qamar"})

end1 = db.child("Sammy Slug").child("end1").get()
end2 = db.child("Sammy Slug").child("end2").get()
start1 = db.child("Sammy Slug").child("start1").get()
start2 = db.child("Sammy Slug").child("start2").get()
frequency1 = db.child("Sammy Slug").child("frequency1").get()
frequency2 = db.child("Sammy Slug").child("frequency2").get()


#users = db.child("names").get()
#print(users.val())


#-------------------------------------------------------------------------------------------------

#Assume variables have been acquired from firebase
#Temporary variables


numClasses = 2
weekendwakeUpTime = 9
currentDay = datetime.datetime.today().weekday()

#Finds earliest course of the day
def findEarliestTime(currentDay):
	earliestStart = 24
	if currentDay < 5:
		if currentDay % 2 == (frequency1 + 1) % 2:
			if start1 <  earliestStart:
				earliestStart = start1
		elif currentDay % 2 == (frequency2 + 1) % 2:
			if start2 <  earliestStart:
				earliestStart = start2
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
	result = firebase.get('/DrewSquid', None)
	d = ast.literal_eval(result)
	str_start1 = d[start1]
	str_start2 = d[start2]
	str_frequency1 = d[frequency1]
	str_frequency2 = d[frequency2]
	str_end1 = d[end1]
	str_end2 = d[end2]
	start1 = int(str_start1)
	start2 = int(str_start2)
	end1 = int(str_end1)
	end2 = int(str_end2)
	frequency1 = int(str_frequency1)
	frequency2 = int(str_frequency2)

	i = 0
	while i < 7:
		i+=1
		#send firebase the wakeup time
		wakeUpTime(i)
		computeSleepTime(i)
		breakfastTime(i)
		return 0



from flask import *

app = Flask(__name__)

@app.route('/test', methods = ['GET', 'POST'])

def basic2():
	#db.child("Sammy Slug").push({"wakeUpTime" : wakeUpTime(i)})
	#db.child("Sammy Slug").push({"sleepTime" : computeSleepTime(i)})
	#db.child("Sammy Slug").push({"breakfastTime" : breakfastTime(i)})
	return 'Computations written to Firebase'

@app.route('/', methods = ['GET', 'POST'])
def basic():
	db.child("users").push({"name" : "Sammy Slug"})
	db.child("users").push({"wake up time" : "8:00"})
	db.child("users").push({"breakfast" : "9:30"})
	db.child("users").push({"sleeptime" : "23:00"})
	return 'Hello World'

if __name__ == '__main__':
	app.run(host = '0.0.0.0')
