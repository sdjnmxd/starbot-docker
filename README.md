# StarBot Docker 部署指南

[![Docker Pulls](https://img.shields.io/docker/pulls/sdjnmxd/starbot.svg)](https://hub.docker.com/r/sdjnmxd/starbot)
[![Docker Stars](https://img.shields.io/docker/stars/sdjnmxd/starbot.svg)](https://hub.docker.com/r/sdjnmxd/starbot)
[![Docker Image CI/CD](https://github.com/sdjnmxd/starbot-docker/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/sdjnmxd/starbot-docker/actions/workflows/docker-publish.yml)
[![GitHub Stars](https://img.shields.io/github/stars/sdjnmxd/starbot-docker.svg?logo=github)](https://github.com/sdjnmxd/starbot-docker)
[![GitHub License](https://img.shields.io/github/license/sdjnmxd/starbot-docker)](https://github.com/sdjnmxd/starbot-docker/blob/main/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/sdjnmxd/starbot-docker)](https://github.com/sdjnmxd/starbot-docker/commits/main)

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
- linux/arm64（未经过测试，期待反馈）

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

## 问题反馈

如果您在使用过程中遇到任何问题或有改进建议，欢迎通过以下方式反馈：

1. [GitHub Issues](https://github.com/sdjnmxd/starbot-docker/issues)：
   - 部署相关问题
   - Docker镜像问题
   - 功能建议
   - 文档改进

2. [StarBot 官方仓库](https://github.com/Starlwr/StarBot/issues)：
   - StarBot本身的功能问题
   - 推送功能异常
   - 其他Bot相关问题

提交问题时，请尽可能提供：
- 详细的问题描述
- 相关的错误日志
- 复现步骤
- 运行环境信息

## License

本项目采用 MIT License 开源，详细信息请参阅 [LICENSE](LICENSE) 文件。

StarBot Docker 是一个独立项目，仅提供容器化部署方案。StarBot 的所有权利归其原作者所有，详见 [StarBot 官方仓库](https://github.com/Starlwr/StarBot)。 