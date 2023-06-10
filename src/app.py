from telegram import Update
from telegram.ext import ContextTypes

from .get_grades import get_grades
from .get_subjects import get_subjects
from .check_diff import check_diff
from .login import login
import config
import time
from .format_mesasge import format_mesasge

async def app(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    is_ok = True
    is_first = False

    CACHED = None

    while (is_ok):
        is_logged, session = await login()
        if is_logged is True:
            if is_first is False:
                is_first = True
                await update.message.reply_text("You logged in successfully")

            is_list, subjects = get_subjects(session=session)
            if is_list:
                subjects = get_grades(subjects=subjects, session=session)
                is_diff, diff_grades = check_diff(subjects=subjects)
                if is_diff:
                    for msg in format_mesasge(diff_grades):
                        await update.message.reply_text(msg)
            else:
                await update.message.reply_text("Cannot get list of subjects")

        else:
            is_ok = False
            await update.message.reply_text("Incorrect USERNAME or PASSWORD")
    
        REFRESH_TIME = config.Config.REFRESH_TIME
        time.sleep(REFRESH_TIME)