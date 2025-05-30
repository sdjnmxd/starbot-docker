import os
from starbot.core.bot import StarBot
from starbot.core.datasource import JsonDataSource
from starbot.utils import config

def get_env_value(value_str, default_value):
    """根据默认值类型转换环境变量值"""
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
    """从环境变量生成配置字典"""
    # 获取默认配置
    default_config = config.DEFAULT_CONFIG
    
    # 生成配置字典
    config_dict = {}
    
    # 遍历所有环境变量
    for env_key, env_value in os.environ.items():
        # 如果环境变量名与配置键匹配，则使用该值
        if env_key in default_config:
            config_dict[env_key] = get_env_value(env_value, default_config[env_key])
    
    return config_dict

def main():
    # 从环境变量生成配置
    config_dict = env_to_config()
    
    # 应用配置
    if config_dict:
        config.use(**config_dict)

    # 初始化数据源和机器人
    datasource = JsonDataSource("/app/config/push_config.json")
    bot = StarBot(datasource)
    
    # 启动机器人
    bot.run()

if __name__ == "__main__":
    main() 