import pyrebase
config = {
	"apiKey": "AIzaSyBuO7cVVSD--QXf2sn32Z1pVxE1BLS25SU",
    "authDomain": "newprojec-cec0b.firebaseapp.com",
    "databaseURL": "https://newprojec-cec0b.firebaseio.com",
    "projectId": "newprojec-cec0b",
    "storageBucket": "newprojec-cec0b.appspot.com",
   "messagingSenderId": "692607960826"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
#db.child("names").push({"name" : "Sammy Slug"})
#db.child("names").child("class1").push({"start1" : "9"})
#db.child("names").update({"name" : "qamar"})
#users = db.child("names").get()
#print(users.val())
end1 = db.child("Sammy Slug").child("end1").get()
end2 = db.child("Sammy Slug").child("end2").get()
start1 = db.child("Sammy Slug").child("start1").get()
start2 = db.child("Sammy Slug").child("start2").get()
frequency1 = db.child("Sammy Slug").child("frequency1").get()
frequency1 = db.child("Sammy Slug").child("frequency1").get()



from flask import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def basic():
	return 'Hello World'

if __name__ == '__main__':
	app.run(debug = True)
