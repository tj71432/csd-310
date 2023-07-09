""" 
Taylor Jacobs
CYBR410 - Database Security
Prof. Peter Haas
7/9/2023
"""

#Import mongodb stuff
from pymongo import MongoClient

#Connection URL
url = "mongodb+srv://admin:admin@cluster0.utbzgbt.mongodb.net/pytech"

#Mongodb connection
client = MongoClient(url)

#Connect to database
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "The Betrayer"}})

# find the updated student document 
Illidan = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print("  Student ID: " + Illidan["student_id"] + "\n  First Name: " + Illidan["first_name"] + "\n  Last Name: " + Illidan["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")