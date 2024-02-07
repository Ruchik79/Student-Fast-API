from fastapi import FastAPI 
#import dbHelper as dbh
app= FastAPI()

#db_connection=dbh.get_connection()

@app.get("/home")
def home():
    return "Home hai bhai"

@app.get("/room")
def room():
    return "room hai bhai"

# @app.post("/students/")
# def create_student(roll_number:int,name: str, age: int):
#     cursor = db_connection.cursor()
#     query = "INSERT INTO students (roll_number,name, age) VALUES (%s, %s,%s)"
#     data = (roll_number,name, age)
#     cursor.execute(query, data)
#     db_connection.commit()
#     return {"message": "Student created successfully"}