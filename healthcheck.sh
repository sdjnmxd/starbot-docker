#!/bin/bash

# 检查Python进程是否运行
if ! pgrep -f "python main.py" > /dev/null; then
    echo "Python process is not running"
    exit 1
fi

# 检查Redis连接
if ! redis-cli ping > /dev/null 2>&1; then
    echo "Cannot connect to Redis"
    exit 1
fi

# 检查内存使用
MEMORY_USAGE=$(free | awk '/Mem:/ {print $3/$2 * 100.0}')
if (( $(echo "$MEMORY_USAGE > 90" | bc -l) )); then
    echo "High memory usage: ${MEMORY_USAGE}%"
    exit 1
fi

exit 0 