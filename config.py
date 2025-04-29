# config.py - 配置文件

# Telegram和OpenAI API密钥
TELEGRAM_TOKEN = "111"  # 替换为您的Telegram Bot Token
OPENAI_API_KEY = "111"      # 替换为您的OpenAI API密钥

# 数据库设置
DB_PATH = "bot_interactions.db"

# 管理员设置
ADMIN_IDS = [8079573322]  # 替换为您的Telegram用户ID

# OpenAI设置
DEFAULT_MODEL = "gpt-3.5-turbo"
DEFAULT_TEMPERATURE = 0.7

# 机器人设置
MAX_HISTORY_LENGTH = 10  # 存储的最大对话历史条数
