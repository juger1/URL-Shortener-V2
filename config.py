import os
from dotenv import load_dotenv


# Load environment variables from config.env
load_dotenv('config.env', override=True)

# Function to interpret boolean-like values
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Helper function to get environment variables with type casting and validation
def get_env_var(var_name, cast_type=str, default=None, required=False):
    value = os.environ.get(var_name, default)
    if required and value is None:
        raise ValueError(f"Environment variable '{var_name}' is required but not set.")
    if cast_type == int and value is not None:
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f"Environment variable '{var_name}' must be an integer.")
    return value

# Mandatory variables for the bot to start
API_ID = get_env_var("API_ID", int, required=True)
API_HASH = get_env_var("API_HASH", required=True)
BOT_TOKEN = get_env_var("BOT_TOKEN", required=True)
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "").split(",") if i] or []

DATABASE_NAME = get_env_var("DATABASE_NAME", default="URLShortenerBotV2")
DATABASE_URL = get_env_var("DATABASE_URL", required=True)
OWNER_ID = get_env_var("OWNER_ID", int, required=True)
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

# Optional variables
LOG_CHANNEL = get_env_var("LOG_CHANNEL", int, default=0)
UPDATE_CHANNEL = get_env_var("UPDATE_CHANNEL", int, default=False)
BROADCAST_AS_COPY = is_enabled(get_env_var("BROADCAST_AS_COPY", default="False"), False)
IS_PRIVATE = is_enabled(get_env_var("IS_PRIVATE", default="False"), False)
SOURCE_CODE = get_env_var("SOURCE_CODE", default="")
WELCOME_IMAGE = get_env_var("WELCOME_IMAGE", default="")
LINK_BYPASS = is_enabled(get_env_var("LINK_BYPASS", default="False"), False)
SHORTENER_SITE = get_env_var("SHORTENER_SITE", default="")

# Admin-specific settings
CHANNELS = is_enabled(get_env_var("CHANNELS", default="True"), True)
CHANNEL_ID = [int(i.strip()) for i in os.environ.get("CHANNEL_ID", "").split(" ") if i] or []
DE_BYPASS = [i.strip() for i in os.environ.get("DE_BYPASS", "").split(",") if i] or []
DE_BYPASS.append("mdisk.me")

FORWARD_MESSAGE = is_enabled(get_env_var("FORWARD_MESSAGE", default="False"), False)

WEB_SERVER = is_enabled(get_env_var("WEB_SERVER", default="True"), True)
PING_INTERVAL = get_env_var("PING_INTERVAL", int, default=240)
PORT = get_env_var("PORT", int, default=8000)

