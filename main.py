import os
from starbot.core.bot import StarBot
from starbot.core.datasource import JsonDataSource
from starbot.utils import config

def get_env_value(value_str, default_value):
    if value_str is None:
        return default_value
        
    if isinstance(default_value, bool):
        return value_str.lower() in ('true', '1', 'yes', 'y', 'on')
    elif isinstance(default_value, int):
        try:
            return int(value_str)
        except:
            return default_value
    elif isinstance(default_value, float):
        try:
            return float(value_str)
        except:
            return default_value
    return value_str

def env_to_config():
    default_config = config.DEFAULT_CONFIG
    
    config_dict = {}
    
    for env_key, env_value in os.environ.items():
        # 如果环境变量名与配置键匹配，则使用该值
        if env_key in default_config:
            config_dict[env_key] = get_env_value(env_value, default_config[env_key])
    
    return config_dict

def main():
    # 显示项目信息
    print("=" * 60)
    print("🤖 StarBot Docker 容器化版本")
    print("=" * 60)
    print("📦 项目仓库: https://github.com/sdjnmxd/starbot-docker")
    print("🐛 问题反馈: https://github.com/sdjnmxd/starbot-docker/issues")
    print("📚 使用文档: https://github.com/sdjnmxd/starbot-docker#readme")
    print("")
    print("ℹ️  这是 StarBot 的 Docker 容器化部署版本")
    print("   如果遇到部署、容器或配置相关问题，请优先到上述仓库提交 Issue")
    print("   只有 StarBot 核心功能问题才需要到原项目反馈")
    print("=" * 60)
    print("")
    
    sessdata = os.getenv('SESSDATA')
    bili_jct = os.getenv('BILI_JCT')
    buvid3 = os.getenv('BUVID3')
    
    if not all([sessdata, bili_jct, buvid3]):
        raise ValueError("缺少必要的B站登录凭据，请设置 SESSDATA, BILI_JCT, BUVID3 环境变量")
    
    config.set_credential(
        sessdata=sessdata,
        bili_jct=bili_jct,
        buvid3=buvid3
    )

    config_dict = env_to_config()
    
    if config_dict:
        config.use(**config_dict)

    datasource = JsonDataSource("/app/config/push_config.json")
    bot = StarBot(datasource)
    
    print("🚀 StarBot 启动中...")
    print("")
    
    # 启动机器人
    bot.run()

if __name__ == "__main__":
    main() 