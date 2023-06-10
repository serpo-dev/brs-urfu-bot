from dotenv import dotenv_values
import os

env = dotenv_values(".env")

class Config:
    BOT_TOKEN = env["BOT_TOKEN"] or "bot_token"

    URFU_USERNAME = env["URFU_USERNAME"] or "username"
    URFU_PASSWORD = env["URFU_PASSWORD"] or "password"

    REFRESH_TIME = int(env["REFRESH_TIME"]) or 60

    APP_DIR = os.path.abspath(os.path.dirname(__file__))