"""
    Taylor Jacobs
    CYBR410 - Database Security
    Prof. Peter Haas
    7/2/2023
"""

#Import mongodb stuff
from pymongo import MongoClient

#Connection URL
url = "mongodb+srv://admin:admin@cluster0.utbzgbt.mongodb.net/pytech"

#Mongodb connection
client = MongoClient(url)

#Connect to database
db = client.pytech

#Three student documents - Illidan Stormrage, Arthas Menethil, Sylvanas Windrunner
#Illidan Stormrage

illidan = {
    "student_id": "1007",
    "first_name": "Illidan",
    "last_name": "Stormrage",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "4.0",
            "start_date": "NA",
            "end_date": "NA",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Database Security",
                    "instructor": "Peter Haas",
                    "grade": "A+"
                },
                {
                    "course_id": "PH106",
                    "description": "Ethics",
                    "instructor": "Jigglypuff",
                    "grade": "A+"
                }
            ]
        }
    ]

}

#Arthas Menethil 
arthas = {
    "student_id": "1008",
    "first_name": "Arthas",
    "last_name": "Menethil",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "4.0",
            "start_date": "NA",
            "end_date": "NA",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Database Security",
                    "instructor": "Peter Haas",
                    "grade": "9000"
                },
                {
                    "course_id": "PH106",
                    "description": "Ethics",
                    "instructor": "Cardi B",
                    "grade": "A-"
                }
            ]
        }
    ]
}

#Sylvanas Windrunner
sylvanas = {
    "student_id": "1009",
    "first_name": "Sylvanas",
    "last_name": "Windrunner",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "666",
            "start_date": "NA",
            "end_date": "NA",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Database Security",
                    "instructor": "Peter haas",
                    "grade": "Z"
                },
                {
                    "course_id": "PH106",
                    "description": "Ethics",
                    "instructor": "Peter Haas",
                    "grade": "PG13"
                }
            ]
        }
    ]
}

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
illidan_student_id = students.insert_one(illidan).inserted_id
print("  Inserted student record Illidan Stormrage into the students collection with document_id " + str(illidan_student_id))

arthas_student_id = students.insert_one(arthas).inserted_id
print("  Inserted student record Arthas Menethil into the students collection with document_id " + str(arthas_student_id))

sylvanas_student_id = students.insert_one(sylvanas).inserted_id
print("  Inserted student record Sylvanas Windrunner into the students collection with document_id " + str(sylvanas_student_id))

input("\n\n  End of program, press any key to exit... ")