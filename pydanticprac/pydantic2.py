from datetime import UTC, datetime
from pydantic import BaseModel,ValidationError,Field
from functools import partial
class User(BaseModel):
    uid: int
    username:str
    email: str
    verified_at: datetime | None=None
    is_active: bool=True
    bio: str=""
    full_name: str|None=None

class Item(BaseModel):
   itemid: int
   itemname: str
   itemprice: int 
   purchased_at: datetime=Field(default_factory=partial(datetime.now,tz=UTC))
   expired: bool=False
   ingredients: list[str]=Field(default_factory=list)


try:
 user1=User(uid=123,username="Nishant",email="Nishant@gmail.com",age=22)
 item1=Item(itemid=1,itemname="cake",itemprice=30,ingredients=['sugar','milk'])
 print(item1.ingredients)
 item2=Item(itemid=2,itemname="pastry",itemprice=40,ingredients=['egg','aginomoto'])
 print(item2.ingredients)
 user1.bio="123"
 print(user1.model_dump())
 print(user1.model_dump_json(indent=2))
 print(user1.username)
except ValidationError as e:
   print("Please Check:",e) 
