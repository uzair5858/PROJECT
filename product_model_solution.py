from pydantic import BaseModel

# creat product model with id , name , price , in_stock

class product (BaseModel):
    id : int 
    name : str 
    price : float 
    in_stock : bool = True
