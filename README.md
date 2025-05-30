# StarBot Docker 部署指南

这是 [StarBot](https://github.com/Starlwr/StarBot) 的 Docker 部署配置，提供了一个开箱即用的容器化部署方案。

## 快速开始

从 Docker Hub 拉取镜像并运行：

```bash
# 方式一：直接使用 docker-compose（推荐）
docker-compose pull
docker-compose up -d

# 方式二：手动拉取镜像
docker pull sdjnmxd/starbot:latest
```

## 环境要求

- Docker
- Docker Compose

## 配置指南

### 配置文件
StarBot 的主要功能配置通过 `push_config.json` 文件管理：
- 位置：`./config/push_config.json`
- 获取方式：使用 [StarBot 官方配置工具](https://bot.starlwr.com) 生成

### 环境变量
本项目支持完整的环境变量配置，所有 StarBot 的配置项都可以通过环境变量进行设置。环境变量名称与 StarBot 的配置键名保持一致，无需额外映射。

必需的环境变量如下：

```env
# B站账号凭据
SESSDATA=你的B站SESSDATA
BILI_JCT=你的B站BILI_JCT
BUVID3=你的B站BUVID3

# Mirai HTTP API 连接信息
MIRAI_HOST=localhost
MIRAI_PORT=7827

# Redis 连接信息
REDIS_HOST=localhost
REDIS_PORT=6379
```

其他可选配置项请参考 [StarBot 官方文档 - 高级配置](https://bot.starlwr.com/depoly/document)。

## 部署流程

1. 准备配置文件目录：
```bash
mkdir -p config
```

2. 配置 StarBot：
   - 使用官方配置工具生成 `push_config.json`
   - 将文件保存到 `config` 目录

3. 配置环境变量：
```bash
# 创建环境变量文件
cat > .env << 'EOF'
# B站账号凭据
SESSDATA=你的B站SESSDATA
BILI_JCT=你的B站BILI_JCT
BUVID3=你的B站BUVID3

# Mirai HTTP API 连接信息
MIRAI_HOST=localhost
MIRAI_PORT=7827

# Redis 连接信息
REDIS_HOST=localhost
REDIS_PORT=6379
EOF
```

4. 启动服务：
```bash
docker-compose up -d
```

## 版本管理

镜像版本说明：
- `latest`: 最新版本，随 StarBot 更新自动构建
- `x.y.z`: 特定版本号，对应 StarBot 发布版本

镜像通过 GitHub Actions 自动构建并推送至 [Docker Hub](https://hub.docker.com/r/sdjnmxd/starbot)：
- 每日自动检查 StarBot 更新
- 发现新版本时自动构建并推送镜像

## 支持架构

- linux/amd64
- linux/arm64

## 常用命令

```bash
# 查看日志
docker-compose logs -f starbot

# 停止服务
docker-compose down

# 更新版本
docker-compose pull
docker-compose up -d
``` 