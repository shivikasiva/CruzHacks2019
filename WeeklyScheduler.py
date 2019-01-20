import json

from firebase import firebase

import ast

#flask

firebase = firebase.FirebaseApplication('https://cruzhacks-229107.firebaseio.com/', None)


def init_user(name, college, userid, start1, end1, frequency1, start2, end2, frequency2):
    data = {'name': name, 'college': college, 'userid': userid}
    data1 = {'start1': start1, 'end1': end1, 'frequency1': frequency1}
    data2 = {'start2': start2, 'end2': end2, 'frequency2': frequency2}
    sent = json.dumps(data)
    sent1 = json.dumps(data1)
    sent2 = json.dumps(data2)
    result = firebase.post("/users", sent)
    result1 = firebase.post("/users", sent1)
    result2 = firebase.post("/users", sent2)

#init_user('bob', 'UCSC', '0')
#init_user('alice', 'UCSC', '1')
#init_user('joe', 'UCSB', '2')
#init_user('lilly', 'UCLA', '3')

#result = firebase.get('/users', '-LWcJ-7nvaKHi5l4saRa')
#print(result)

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
    frequency2 = int(str_frequency2)
    
    i = 0
    while i < 7:
        i+=1
        #send firebase the wakeup time
        wakeUpTime(i)
        computeSleepTime(i)
        breakfastTime(i)
        return 0



createWeeklySleepSchedule();
