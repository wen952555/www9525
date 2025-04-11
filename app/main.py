from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.config import SessionLocal, engine

# 初始化数据库表
models.Base.metadata.create_all(bind=engine)

# 创建 FastAPI 应用
app = FastAPI()

# 数据库依赖
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email 已被注册")
    return crud.create_user(db, user=user)

@app.get("/users/", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.post("/nodes/", response_model=schemas.NodeResponse)
def create_node(node: schemas.NodeCreate, db: Session = Depends(get_db)):
    return crud.create_node(db, node=node)

@app.get("/users/{user_id}/nodes/", response_model=List[schemas.NodeResponse])
def get_user_nodes(user_id: int, db: Session = Depends(get_db)):
    return crud.get_nodes_by_user(db, user_id=user_id)