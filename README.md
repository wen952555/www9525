# VPN Service

## 项目简介
这是一个简单的 Flask 应用，提供以下功能：
- 用户登录认证
- 流量统计
- 管理面板

适合部署到 Render 平台。

## 功能模块
1. **用户管理**
   - 登录认证
2. **流量管理**
   - 流量统计
3. **管理面板**
   - 活跃用户统计
   - 服务负载监控

## 本地运行步骤

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 启动开发服务器
```bash
python app.py
```

访问 `http://127.0.0.1:5000` 测试应用。

## 使用 Docker 本地运行

### 1. 构建 Docker 镜像
```bash
docker build -t vpn-service .
```

### 2. 启动容器
```bash
docker run -p 5000:5000 vpn-service
```

访问 `http://127.0.0.1:5000` 测试应用。

## 部署到 Render

### 1. 推送代码到 GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/vpn-service.git
git push -u origin main
```

### 2. 在 Render 配置 Web 服务
1. 登录 [Render](https://render.com)。
2. 点击 **"New +"** 按钮，选择 **"Web Service"**。
3. 在 **Repository** 中选择刚刚推送到 GitHub 的仓库。
4. 配置 Web 服务：
   - **Environment**：选择 **Docker**。
   - Render 会自动检测到 `Dockerfile` 并进行构建。
5. 点击 **"Create Web Service"**，等待 Render 构建和部署完成。

### 3. 配置环境变量
在 Render 的 **Environment Variables** 设置中添加以下变量：
- `SECRET_KEY`：用于加密的密钥（例如 `your_secret_key`）。
- `DEBUG`：设置为 `False` 禁用调试模式。
- `DATABASE_URI`：设置为数据库连接字符串。

访问 Render 提供的公共 URL，例如：
```
https://vpn-service.onrender.com
```

## 示例 API 路由
- `POST /auth/login`：用户登录
- `GET /traffic/stats`：获取流量统计信息
- `GET /admin/dashboard`：查看管理面板数据