from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config import Base
import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    subscription_type = Column(String, default="free")  # free, premium
    traffic_used = Column(Float, default=0.0)  # 流量使用（以 GB 为单位）
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    active = Column(Boolean, default=True)

    # 关系：用户与订阅节点
    nodes = relationship("Node", back_populates="user")

class Node(Base):
    __tablename__ = 'nodes'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    node_name = Column(String, nullable=False)
    node_url = Column(String, nullable=False)

    # 关系：节点与用户
    user = relationship("User", back_populates="nodes")