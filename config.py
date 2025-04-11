import os

class Config:
    """通用配置"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')  # 加密密钥
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't']  # 调试模式
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///app.db')  # 数据库连接