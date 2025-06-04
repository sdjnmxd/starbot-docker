# 贡献指南

感谢你对 StarBot Docker 项目的关注和贡献！

## 如何贡献

### 🐛 报告 Bug

如果你发现了 Bug，请：

1. 先查看 [Issues](https://github.com/sdjnmxd/starbot-docker/issues) 确认问题未被报告过
2. 创建新的 Issue，包含：
   - 清晰的问题描述
   - 复现步骤
   - 期望行为和实际行为
   - 环境信息（Docker 版本、系统版本等）
   - 相关日志输出

### 💡 功能建议

如果你有功能建议：

1. 先查看现有 Issues 确认建议未被提出过
2. 创建 Feature Request Issue，说明：
   - 功能的具体需求
   - 使用场景
   - 期望的实现方式

### 🔧 代码贡献

1. **Fork 项目**
   ```bash
   git clone https://github.com/your-username/starbot-docker.git
   cd starbot-docker
   ```

2. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/your-bug-fix
   ```

3. **开发和测试**
   - 确保代码遵循现有代码风格
   - 测试你的修改
   - 更新相关文档

4. **提交代码**
   ```bash
   git add .
   git commit -m "feat: 添加新功能"
   # 或
   git commit -m "fix: 修复字体加载问题"
   ```

5. **推送并创建 PR**
   ```bash
   git push origin your-branch-name
   ```
   然后在 GitHub 上创建 Pull Request

## 代码规范

### Commit 消息规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式（不影响代码运行的变动）
- `refactor`: 重构
- `test`: 增加测试
- `chore`: 构建过程或辅助工具的变动

示例：
```
feat: 添加自定义字体支持
fix: 修复容器启动时的权限问题
docs: 更新 README 中的部署说明
```

### 文件组织

- `Dockerfile` - Docker 镜像构建文件
- `start.sh` - 容器启动脚本
- `main.py` - Python 主程序
- `requirements.txt` - Python 依赖
- `docker-compose.yml` - Docker Compose 配置
- `README.md` - 项目文档

## 测试

在提交之前，请确保：

1. **本地测试**
   ```bash
   # 构建镜像
   docker build -t starbot-test .
   
   # 运行测试
   docker run --rm starbot-test
   ```

2. **文档测试**
   - 确保 README 中的命令可以正常执行
   - 检查文档的准确性

## 问题类型

### 适合在此仓库报告的问题

- Docker 镜像构建问题
- 容器运行问题
- 部署配置问题
- 字体文件处理问题
- 环境变量配置问题
- 文档问题

### 不适合在此仓库报告的问题

请到 [StarBot 官方仓库](https://github.com/Starlwr/StarBot/issues) 报告：

- StarBot 核心功能问题
- B站 API 相关问题
- Mirai 相关问题
- 推送逻辑问题

## 开发环境

推荐的开发工具：

- **Docker**: 用于构建和测试
- **Git**: 版本控制
- **IDE**: VS Code, PyCharm 等
- **系统**: Linux, macOS, Windows

## 联系方式

- GitHub Issues: [项目 Issues](https://github.com/sdjnmxd/starbot-docker/issues)
- 维护者: [@sdjnmxd](https://github.com/sdjnmxd)

## 许可证

通过贡献代码，你同意你的贡献将在 [MIT License](LICENSE) 下发布。 