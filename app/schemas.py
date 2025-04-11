from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    subscription_type: str
    traffic_used: float
    active: bool

    class Config:
        orm_mode = True

class NodeBase(BaseModel):
    node_name: str
    node_url: str

class NodeCreate(NodeBase):
    user_id: int

class NodeResponse(NodeBase):
    id: int

    class Config:
        orm_mode = True