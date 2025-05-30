# StarBot Docker 部署指南

这是 [StarBot](https://github.com/Starlwr/StarBot) 的 Docker 部署配置。

## 快速使用（从Docker Hub拉取）

```bash
# 拉取镜像
docker pull ${DOCKERHUB_USERNAME}/starbot:latest

# 或者直接使用docker-compose
docker-compose pull
docker-compose up -d
```

## 前置要求

- Docker
- Docker Compose

## 从源码构建

1. 创建配置目录和文件：

```bash
mkdir -p config
```

2. 在 config 目录下创建 push_config.json 文件（可以使用 StarBot 官方的在线制作工具生成）

3. 设置环境变量：
创建 .env 文件并填入以下内容：

```env
BILIBILI_SESSDATA=你的sessdata
BILIBILI_BILI_JCT=你的bili_jct
BILIBILI_BUVID3=你的buvid3
```

4. 启动服务：

```bash
docker-compose up -d
```

## 配置说明

- 配置文件位置：`./config/push_config.json`
- Redis 数据持久化：数据存储在 Docker volume 中
- 容器自动重启：服务配置了自动重启策略

## 版本说明

- `latest`: 最新版本
- `x.y.z`: 特定版本号

镜像会通过GitHub Actions自动构建并推送到Docker Hub，每天检查更新。当starbot-bilibili包发布新版本时，会自动构建新的Docker镜像。

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