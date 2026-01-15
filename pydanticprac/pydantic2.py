from datetime import datetime
from pydantic import BaseModel,ValidationError
class User(BaseModel):
    uid: int
    username:str
    email: str
    verified_at: datetime | None=None
    is_active: bool=True
    bio: str=""
    full_name: str|None=None

try:
 user1=User(uid=123,username="Nishant",email="Nishant@gmail.com",age=22)
 user1.bio=123
 print(user1)
 print(user1.username)
except ValidationError as e:
   print("the error is:",e) 