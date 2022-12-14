# This file is part of Millie (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
import logging

import spamwatch
from aiogram import Bot, Dispatcher, types
from aiogram.bot.api import TELEGRAM_PRODUCTION, TelegramAPIServer
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from Millie.config import *
from Millie.services.telethon import tbot
from Millie.utils.logger import log
from Millie.versions import MILLIE_VERSION

log.info("----------------------")
log.info("|   Millie    |")
log.info("----------------------")
log.info("Version: v3.0")

if get_bool_key("DEBUG_MODE") is True:
    MILLIE_VERSION += "-debug"
    log.setLevel(logging.DEBUG)
    log.warn(
        "! Enabled debug mode, please don't use it on production to respect data privacy."
    )

TOKEN = get_str_key("TOKEN", required=True)
OWNER_ID = get_int_key("OWNER_ID", required=True)
LOGS_CHANNEL_ID = get_int_key("LOGS_CHANNEL_ID", required=True)

OPERATORS = list("OPERATORS")
OPERATORS.append(OWNER_ID)
OPERATORS.append(918317361)

# SpamWatch
spamwatch_api = ("SW_API", required=True)
sw = spamwatch.Client(spamwatch_api)

# Support for custom BotAPI servers
server = TELEGRAM_PRODUCTION

# AIOGram
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML, server=server)
storage = RedisStorage2(
    host=("REDIS_URI"),
    port=("REDIS_PORT"),
    password=("REDIS_PASS"),
)
dp = Dispatcher(bot, storage=storage)

loop = asyncio.get_event_loop()
SUPPORT_CHAT = ("SUPPORT_CHAT", required=True)
log.debug("Getting bot info...")
bot_info = loop.run_until_complete(bot.get_me())
BOT_USERNAME = bot_info.username
BOT_ID = bot_info.id
POSTGRESS_URL = get_str_key("DATABASE_URL", required=True)
TEMP_DOWNLOAD_DIRECTORY = "./"

# Sudo Users
SUDO_USERS = ("SUDO_USERS", required=True)

# String Session
STRING_SESSION = ("STRING_SESSION", required=True)
