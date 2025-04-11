# VPN Service

## 项目简介
这是一个模块化的 VPN 服务项目，提供认证、流量统计、管理面板等功能，支持生产级部署。

## 功能模块
- 用户管理
  - 登录认证
- 流量管理
  - 流量统计
- 管理面板
  - 活跃用户统计
  - 服务负载监控

## 部署步骤
### 1. 本地测试
```bash
# 安装依赖
pip install -r requirements.txt

# 启动开发服务器
python app.py
```

### 2. 使用 Docker 本地测试
```bash
# 构建镜像
docker build -t vpn-service .

# 启动容器
docker run -p 5000:5000 vpn-service
```

### 3. 部署到 Render
1. 将项目推送到 GitHub。
2. 在 Render 创建 Web 服务，选择 Docker 环境。
3. 部署完成后，访问 Render 提供的公共 URL。

## 环境变量
- `SECRET_KEY`: 加密密钥（默认值为 `default_secret_key`）。
- `DEBUG`: 调试模式（生产环境设置为 `False`）。
- `DATABASE_URI`: 数据库连接字符串（默认使用 SQLite）。