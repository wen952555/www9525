# 使用官方 Python Slim 镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt requirements.txt

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 暴露端口（Render 平台会动态设置 $PORT）
EXPOSE 5000

# 使用 Gunicorn 作为生产环境的 WSGI 服务器
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:$PORT", "app:app"]