# ZeusMusic (Telegram bot project)
# Copyright (C) 2021  Sathishzus & Bharathi2003

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
from os import getenv

from dotenv import load_dotenv
from ZeusMusic.helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SHAKIDAAUPDATES")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/5233d8c1398d4d6628e00.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/03b7244c8901a3f0c55d3.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ՏհɑƘíժɑ | 𝙈𝙐𝙎𝙄𝘾 𝘼𝙎𝙎𝙄𝙎𝙏𝘼𝙉𝙏")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "SHAKIDAASUPORT")
PROJECT_NAME = getenv("PROJECT_NAME", "SHAKIDAAMUSIC")
OWNER = getenv("OWNER", "@AANDAVAR8064")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/ZeusNetworks/ZeusMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
DATABASE_URL = os.environ.get("DATABASE_URL") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

#heroku
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/ZeusNetworks/ZeusMusic"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
