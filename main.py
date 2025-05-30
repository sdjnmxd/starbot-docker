import os
from starbot.core.bot import StarBot
from starbot.core.datasource import JsonDataSource
from starbot.utils import config

def main():
    # 从环境变量或配置文件获取凭据
    sessdata = os.getenv('BILIBILI_SESSDATA')
    bili_jct = os.getenv('BILIBILI_BILI_JCT')
    buvid3 = os.getenv('BILIBILI_BUVID3')

    # 设置B站凭据
    config.set_credential(
        sessdata=sessdata,
        bili_jct=bili_jct,
        buvid3=buvid3
    )

    # 初始化数据源和机器人
    datasource = JsonDataSource("/app/config/push_config.json")
    bot = StarBot(datasource)
    
    # 启动机器人
    bot.run()

if __name__ == "__main__":
    main() 