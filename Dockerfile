# 使用官方 Python 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 复制代码文件
COPY . .

# 设置环境变量（可选）
# ENV TELEGRAM_BOT_TOKEN="<YOUR_BOT_TOKEN>"

# 定义容器启动时的入口命令
CMD ["python", "bot.py"]