import os

class Config:
    """通用配置类"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')  # 加密密钥
    DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']  # 调试模式