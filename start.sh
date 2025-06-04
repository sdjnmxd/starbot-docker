#!/bin/bash

# 检查是否有自定义字体文件
if [ -d "/app/resource" ] && [ "$(ls -A /app/resource 2>/dev/null)" ]; then
    echo "🎨 发现自定义字体文件，正在复制到 StarBot 资源目录..."
    cp -f /app/resource/* /usr/local/lib/python3.9/site-packages/starbot/resource/ 2>/dev/null || true
    echo "✅ 字体文件复制完成"
    echo "📁 当前字体文件列表："
    ls -la /usr/local/lib/python3.9/site-packages/starbot/resource/*.ttf 2>/dev/null || echo "   未找到 .ttf 字体文件"
else
    echo "📝 使用默认字体文件"
fi

echo ""

# 启动 StarBot
exec python main.py 