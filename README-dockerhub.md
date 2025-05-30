# StarBot Docker

[![Docker Pulls](https://img.shields.io/docker/pulls/sdjnmxd/starbot.svg)](https://hub.docker.com/r/sdjnmxd/starbot)
[![Docker Stars](https://img.shields.io/docker/stars/sdjnmxd/starbot.svg)](https://hub.docker.com/r/sdjnmxd/starbot)
[![GitHub Stars](https://img.shields.io/github/stars/sdjnmxd/starbot-docker.svg?logo=github)](https://github.com/sdjnmxd/starbot-docker)

这是 [StarBot](https://github.com/Starlwr/StarBot) 的 Docker 镜像，提供了开箱即用的容器化部署方案。

## 支持架构

- linux/amd64
- linux/arm64（未经过测试，期待反馈）

## 快速开始

```bash
# 创建配置目录
mkdir -p config

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

# 启动服务
docker-compose up -d
```

## 配置说明

### 配置文件
StarBot 的主要功能配置通过 `push_config.json` 文件管理：
- 位置：`./config/push_config.json`
- 获取方式：使用 [StarBot 官方配置工具](https://bot.starlwr.com) 生成

### 环境变量
本项目支持完整的环境变量配置，所有 StarBot 的配置项都可以通过环境变量进行设置。环境变量名称与 StarBot 的配置键名保持一致，无需额外映射。

必需的环境变量：
- `SESSDATA`: B站账号的SESSDATA
- `BILI_JCT`: B站账号的BILI_JCT
- `BUVID3`: B站账号的BUVID3
- `MIRAI_HOST`: Mirai HTTP API地址
- `MIRAI_PORT`: Mirai HTTP API端口
- `REDIS_HOST`: Redis地址
- `REDIS_PORT`: Redis端口

其他可选配置项请参考 [StarBot 官方文档 - 高级配置](https://bot.starlwr.com/depoly/document)。

## 版本说明

- `latest`: 最新版本，随 StarBot 更新自动构建
- `x.y.z`: 特定版本号，对应 StarBot 发布版本

## 相关链接

- [GitHub 仓库](https://github.com/sdjnmxd/starbot-docker)
- [StarBot 官方仓库](https://github.com/Starlwr/StarBot)
- [StarBot 官方文档](https://bot.starlwr.com/depoly/document)

## 自动构建

镜像通过 GitHub Actions 自动构建并推送：
- 每日自动检查 StarBot 更新
- 发现新版本时自动构建并推送镜像

## 问题反馈

如果您在使用过程中遇到任何问题，欢迎在 [GitHub Issues](https://github.com/sdjnmxd/starbot-docker/issues) 中反馈。 