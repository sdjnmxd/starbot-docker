# StarBot Docker 部署指南

这是 [StarBot](https://github.com/Starlwr/StarBot) 的 Docker 部署配置。

## 快速使用（从Docker Hub拉取）

```bash
# 拉取镜像
docker pull sdjnmxd/starbot:latest

# 或者直接使用docker-compose
docker-compose pull
docker-compose up -d
```

## 前置要求

- Docker
- Docker Compose

## 配置说明

### 基础配置
- 配置文件位置：`./config/push_config.json`
- Redis 数据持久化：数据存储在 Docker volume 中
- 容器自动重启：服务配置了自动重启策略

### Redis配置
支持两种Redis连接方式：

1. 使用内置Redis（默认）：
```bash
docker-compose up -d
```

2. 使用外部Redis：
```bash
# 创建.env文件并配置Redis连接信息
cat > .env << EOF
REDIS_HOST=your-redis-host
REDIS_PORT=6379
REDIS_PASSWORD=your-redis-password  # 可选
REDIS_DB=0                         # 可选，默认0
REDIS_SSL=false                    # 可选，默认false
EOF

# 仅启动StarBot服务（不包含Redis）
docker-compose --profile starbot up -d
```

## 从源码构建

1. 创建配置目录和文件：

```bash
mkdir -p config
```

2. 在 config 目录下创建 push_config.json 文件（可以使用 StarBot 官方的在线制作工具生成）

3. 设置环境变量：
创建 .env 文件并填入以下内容：

```env
# B站账号配置
BILIBILI_SESSDATA=你的sessdata
BILIBILI_BILI_JCT=你的bili_jct
BILIBILI_BUVID3=你的buvid3

# Redis配置（可选，使用外部Redis时需要）
# REDIS_HOST=your-redis-host
# REDIS_PORT=6379
# REDIS_PASSWORD=your-redis-password
# REDIS_DB=0
# REDIS_SSL=false
```

4. 启动服务：

```bash
docker-compose up -d
```

## 版本说明

- `latest`: 最新版本
- `x.y.z`: 特定版本号

镜像会通过GitHub Actions自动构建并推送到[Docker Hub](https://hub.docker.com/r/sdjnmxd/starbot)，每天检查更新。当starbot-bilibili包发布新版本时，会自动构建新的Docker镜像。

## 支持的平台

- linux/amd64
- linux/arm64

## 日志查看

```bash
docker-compose logs -f starbot
```

## 停止服务

```bash
docker-compose down
```

## 更新版本

```bash
docker-compose pull
docker-compose up -d
``` 