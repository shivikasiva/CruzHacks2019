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
print result