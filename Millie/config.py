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

import os
import sys

import yaml
from envparse import env

from Millie.utils.logger import log

DEFAULTS = {
    "LOAD_MODULES": True,
    "DEBUG_MODE": True,
    "REDIS_HOST": "localhost",
    "REDIS_PORT": 6379,
    "REDIS_DB_FSM": 1,
    "MONGODB_URI": "localhost",
    "MONGO_DB": "Millie",
    "API_PORT": 8080,
    "JOIN_CONFIRM_DURATION": "30m",
}

# Basic
TOKEN: "5108238708:AAGlkmm458qm4i4SFb5BDlV11dzEfpEZAhc"

# Get they in https://my.telegram.org/
APP_ID: 18706633
APP_HASH: "1d7c16e89a28c5e332d457e5e1027d0c"

#Generate a telethon str session  with https://repl.it/@SpEcHiDe/GenerateStringSession (telethon one)
STRING_SESSION: "1AZWarzcBu7Pqge_BFYrzPmVtpQbKoiIqvxXuRBv-nTQ_8-9ObaLpm9Dx4XXuwR1-Ly66stt1EggtjkVNV7fyV1pPxZyBC_WYMDexpKv6D6QQyvF-lk87LGVUzWlCF3pam_2fMMQniEH24zDdb1WqR-b7i-F_lwqaome-Hb0zAeojpptv4_lBGl2jd2irnWZ98Rcw0MyykKoMrgSE5B7MukJfFWHwePJ8O_wGDyZtKFuor31hmfttLt6Vl9Ba3qhD35-rhVbI78jFl7lC2di4p9DDPaggoMIAAvwxHKk-EY9tpMHR6rLvBpitbmAGehPm3iK3lTCUaHKQU90xWHY5XymCAQbUQ9Q="


MONGO_URI: "mongodb+srv://rplayvcbot:1rplay2@cluster0.n7alv.mongodb.net/cluster0?retryWrites=true&w=majority"

MONGO_URI2: "mongodb+srv://rplayvcbot:1rplay2@cluster0.n7alv.mongodb.net/cluster0?retryWrites=true&w=majority"
MONGO_PORT: 27017
MONGO_DB: 'Millie'

API_PORT: 8080

REDIS_URI: "redis-15630.c16.us-east-1-2.ec2.cloud.redislabs.com"
REDIS_PORT: 15630
REDIS_PASS: "IsbJe2qu1FaiSct7sfJY8cizhTYhp43A"
TEMP_MAIL_KEY: ""
OWNER_ID: 18706633
OPERATORS: [1141839926, 18706633]
SUPPORT_CHAT: -1001547941154
SUDO_USERS: "1927155351 5570402782 1733484689 1061059757"

DATABASE_URL: "postgres://dksngzpj:VLPEE7HaRBITuF7wUluPyDOSR41AtXO7@peanut.db.elephantsql.com/dksngzpj"
VIRUS_API_KEY: ""
TIME_API_KEY: ""
REM_BG_API_KEY: ""
ARQ_API: "GAXDGI-UPYCXO-CDSLCE-LYBTZK-ARQ"

# Advanced
SW_API: "VWFUxtmR2dFHLpAGLAhh630bHcODm3E35d5bqUHUfpsQqqOc8iFknZUXMgS5Te2g"
IBM_WATSON_CRED_URL: ""
IBM_WATSON_CRED_PASSWORD: ""
OPENWEATHERMAP_ID: ""
WOLFRAM_ID: ""
DEBUG_MODE: False
LOAD_MODULES: True
LOGS_CHANNEL_ID: -1001547941154
ALLOW_FORWARDS_COMMANDS: False
ALLOW_EXCEL: False

CONFIG_PATH = "data/bot_conf.yaml"
if os.name == "nt":
    log.debug("Detected Windows, changing config path...")
    CONFIG_PATH = os.getcwd() + "\\data\\bot_conf.yaml"

if os.path.isfile(CONFIG_PATH):
    log.info(CONFIG_PATH)
    DEFAULTS[item.upper()] = data[item]
else:
    log.info("Using env vars")


def get_str_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not data:
        log.critical("No str key: " + name)
        sys.exit(2)
    else:
        return data


def get_int_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not data:
        log.critical("No int key: " + name)
        sys.exit(2)
    else:
        return data


def get_list_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not data:
        log.critical("No list key: " + name)
        sys.exit(2)
    else:
        return data


def get_bool_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not data:
        log.critical("No bool key: " + name)
        sys.exit(2)
    else:
        return data
