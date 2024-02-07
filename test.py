from fastapi import FastAPI 
import random
from pydantic import BaseModel 
app= FastAPI()

@app.get('/home')
def home():
    return "H W"

@app.get('/english')
def hrandom():
    a=random.randint(0,100)
    return a

@app.get('/employee/{id}')
def employee_by_id(id:int):
    return f"This is the employee detail of {id}"

@app.get('/x_employee')
def x_employee_by_id(id:int,id2):
    return f"This is the employee detail of {id} , {id2}"

class EMP(BaseModel):
    id:int
    name:str


@app.post('/create_employee')
def create_employee(obj:EMP):
    return str(obj.id) + " "+obj.name+ " is created"