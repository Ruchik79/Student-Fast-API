from pydantic import BaseModel

class Student(BaseModel):
    roll_number:int
    name:str
    class_name:str
    address:str
    phone:str

    
class MarkSheet(BaseModel):
    roll_number:int
    math:int
    science:int
    sst:int
    hindi:int
    english:int

    
