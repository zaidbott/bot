import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6723249685:AAHEfoaWmsTUZIN6DIvETJW_O0IrI9sOg2E")

    APP_ID = int(os.environ.get("APP_ID", 27570053))

    API_HASH = os.environ.get("API_HASH", "46b847de1400a4f47541a90433b1af13")
