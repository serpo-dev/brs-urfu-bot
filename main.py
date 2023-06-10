import config
from src.app import app
from telegram.ext import Application, CommandHandler


def main() -> None:
    token = config.Config.BOT_TOKEN
    bot = Application.builder().token(token).build()

    bot.add_handler(CommandHandler("start", app))

    bot.run_polling()


if __name__ == '__main__':
    main()