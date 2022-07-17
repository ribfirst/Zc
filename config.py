#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("19076488"))
API_HASH = getenv("98e471abc04bd8febc1226d81ecef0c7")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("5434112680:AAHO-aq4EzMrKR8t3uWZps_dsapXq9S7fUM")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("5315473510", "").split())
)  # Input type must be interger

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("-1001601487753"))

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = getenv(
    "PRIVATE_START_MESSAGE",
    "Hello! Welcome to my Personal Assistant Bot",
)

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("mongodb+srv://abdul540:abdul540@#@cluster0.i1gao.mongodb.net/?retryWrites=true&w=majority", None)
