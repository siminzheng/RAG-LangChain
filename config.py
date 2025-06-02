# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # 从 .env 加载环境变量

# 从环境变量中读取 OpenAI 配置
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "")

if not OPENAI_API_KEY or not OPENAI_API_BASE:
    raise ValueError("请在 .env 中配置 OPENAI_API_KEY 和 OPENAI_API_BASE")
