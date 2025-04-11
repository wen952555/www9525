from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config import SessionLocal
from models import User, Node
from pydantic import BaseModel
import bcrypt

app = FastAPI()

# 数据库依赖
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic 模型
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class NodeCreate(BaseModel):
    user_id: int
    node_name: str
    node_url: str

# 用户注册
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # 检查是否已存在用户
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email 已注册")
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="用户名已被占用")
    
    # 加密密码
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    
    # 创建用户
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password.decode('utf-8')
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "用户注册成功", "user": new_user}

# 获取所有用户
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# 添加节点
@app.post("/nodes/")
def add_node(node: NodeCreate, db: Session = Depends(get_db)):
    # 检查用户是否存在
    user = db.query(User).filter(User.id == node.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    
    # 添加节点
    new_node = Node(
        user_id=node.user_id,
        node_name=node.node_name,
        node_url=node.node_url
    )
    db.add(new_node)
    db.commit()
    db.refresh(new_node)
    return {"message": "节点添加成功", "node": new_node}

# 获取用户的节点
@app.get("/users/{user_id}/nodes/")
def get_user_nodes(user_id: int, db: Session = Depends(get_db)):
    nodes = db.query(Node).filter(Node.user_id == user_id).all()
    return nodes