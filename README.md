# StarBot Docker 部署指南

[![Docker Pulls](https://img.shields.io/docker/pulls/sdjnmxd/starbot.svg)](https://hub.docker.com/r/sdjnmxd/starbot) [![Docker Stars](https://img.shields.io/docker/stars/sdjnmxd/starbot.svg)](https://hub.docker.com/r/sdjnmxd/starbot) [![Docker Image Size](https://img.shields.io/docker/image-size/sdjnmxd/starbot/latest)](https://hub.docker.com/r/sdjnmxd/starbot) [![Docker Image CI/CD](https://github.com/sdjnmxd/starbot-docker/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/sdjnmxd/starbot-docker/actions/workflows/docker-publish.yml) [![GitHub Stars](https://img.shields.io/github/stars/sdjnmxd/starbot-docker.svg?logo=github)](https://github.com/sdjnmxd/starbot-docker) [![GitHub License](https://img.shields.io/github/license/sdjnmxd/starbot-docker)](https://github.com/sdjnmxd/starbot-docker/blob/main/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/sdjnmxd/starbot-docker)](https://github.com/sdjnmxd/starbot-docker/commits/main)

> **重要提示：**
> 
> - 当前 StarBot 版本（2.0）基于Python实现，将在2025年6月9日后只进行bug修复
> - StarBot 3.0版本（基于Java重构）正在开发中，预计2025年6月开始测试
> - 本Docker镜像将同步跟进这些变更，会在适当的时候完成 3.0 版本的Docker化

这是 [StarBot](https://github.com/Starlwr/StarBot) 的 Docker 部署配置，提供了一个开箱即用的容器化部署方案。

## 运行要求

在开始部署之前，你需要准备：

1. **B站账号凭据**
   - 从B站网页版Cookie中获取以下信息：
     - SESSDATA
     - BILI_JCT
     - BUVID3
   > 详细获取方法请参考 [StarBot 官方文档](https://bot.starlwr.com/depoly/document) 中的 "六、启动 StarBot -> 2.获取登录 Cookie" 章节

2. **Mirai 实例**
   - 需要一个运行中的 Mirai 实例
   - 👉 推荐使用 [overflow-docker](https://github.com/sdjnmxd/overflow-docker)，这是 [Overflow](https://github.com/MrXiaoM/Overflow) 的开箱即用容器化方案
   - 这是一个开箱即用的 Mirai + Overflow 部署方案，可以让你在使用 Onebot 实现的同时保持 Mirai 接口兼容性
   - Overflow 作为 Mirai 到 Onebot 的桥接器，让你可以无缝使用 Mirai 插件

3. **Redis 服务**
   - StarBot 依赖 Redis 进行直播相关的数据存储
   - 默认已集成在 docker-compose 配置中
   - 如需使用外部 Redis，可在环境变量中配置

4. **StarBot 配置文件**
   - 使用 [StarBot 官方配置工具](https://bot.starlwr.com) 生成
   - 文件名：`push_config.json`

## 快速开始

1. 创建项目目录并下载配置文件：
```bash
# 创建目录
mkdir starbot && cd starbot

# 下载配置文件
curl -O https://raw.githubusercontent.com/sdjnmxd/starbot-docker/main/docker-compose.yml
curl -O https://raw.githubusercontent.com/sdjnmxd/starbot-docker/main/env.example
mkdir -p config
```

2. 配置必要的环境变量：
```bash
# 复制环境变量示例文件
cp env.example .env

# 编辑 .env 文件，填入你的配置
vim .env  # 或使用其他编辑器
```

环境变量说明：
- B站账号凭据（必需）：
  - SESSDATA
  - BILI_JCT
  - BUVID3
- Mirai HTTP API 连接信息（必需）：
  - MIRAI_HOST：mirai服务地址
  - MIRAI_PORT：mirai服务端口
- Redis 连接信息（可选，默认使用内置 Redis）：
  - REDIS_HOST：redis服务地址
  - REDIS_PORT：redis服务端口

3. 配置 StarBot：
   - 使用 [StarBot 配置工具](https://bot.starlwr.com) 生成 `push_config.json`
   - 将文件保存到 `config` 目录

4. 启动服务：
```bash
docker compose up -d
```

服务启动后，你可以：
- 查看日志：`docker compose logs -f`
- 停止服务：`docker compose down`
- 重启服务：`docker compose restart`
- 更新版本：`docker compose pull && docker compose up -d`

## 高级配置

### 自定义字体配置
如果你需要使用自定义字体（如中文字体）：

1. 创建字体目录：
```bash
mkdir -p resource
```

2. 将你的字体文件（如 `normal.ttf`、`bold.ttf`）放入 `resource` 目录

3. 在 StarBot 配置中指定字体路径：
```json
{
  "PAINTER_NORMAL_FONT": "你的字体文件名.ttf",
  "PAINTER_BOLD_FONT": "你的粗体字体文件名.ttf"
}
```

注意：
- 字体文件会在容器启动时自动复制到 StarBot 内部资源目录
- 修改字体文件后重启容器即可生效，无需重新构建镜像
- 容器启动时会显示字体文件复制状态

### 其他环境变量
本项目支持完整的环境变量配置，所有 StarBot 的配置项都可以通过环境变量进行设置。环境变量名称与 StarBot 的配置键名保持一致，无需额外映射。

其他可选配置项请参考 [StarBot 官方文档](https://bot.starlwr.com/depoly/document) 中的 "七、高级配置" 章节。

## 版本和更新

- 镜像标签：
  - `latest`: 最新版本，随 StarBot 更新自动构建
  - `x.y.z`: 特定版本号，对应 StarBot 发布版本

- 自动更新：
  - 通过 GitHub Actions 自动构建并推送至 [Docker Hub](https://hub.docker.com/r/sdjnmxd/starbot)
  - 每日自动检查 StarBot 更新
  - 发现新版本时自动构建并推送镜像

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

StarBot Docker 是一个独立项目，仅提供容器化部署方案。上游项目使用以下许可证：
- [StarBot](https://github.com/Starlwr/StarBot) 采用 [AGPL-3.0 License](https://github.com/Starlwr/StarBot)，所有权利归原作者所有
- [Mirai](https://github.com/mamoe/mirai) 采用 [AGPL-3.0 License](https://github.com/mamoe/mirai/blob/dev/LICENSE)，所有权利归原作者所有 