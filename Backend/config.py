from os import getenv, path
from dotenv import load_dotenv

# Try loading local config.env if it exists, but don't fail if running on Vercel
config_path = path.join(path.dirname(path.dirname(__file__)), "config.env")
if path.exists(config_path):
    load_dotenv(config_path)


def _int_env(key: str, default: int = 0) -> int:
    val = getenv(key)
    if not val:
        return default
    try:
        return int(val.strip())
    except ValueError:
        return default


# ----- Environment-backed configuration
class Telegram:
    # ----- Required: Telegram clients
    API_ID = _int_env("API_ID")
    API_HASH = getenv("API_HASH", "").strip()
    BOT_TOKEN = getenv("BOT_TOKEN", "").strip()

    # ----- Required: Database URIs (handles single string or comma-separated on Vercel)
    DATABASE = [db.strip() for db in (getenv("DATABASE") or "").split(",") if db.strip()]

    # ----- Required: Server
    PORT = _int_env("PORT", 8000)
    OWNER_ID = _int_env("OWNER_ID")

    # ----- Session Security (Crucial for Vercel persistent logins!)
    SESSION_SECRET = getenv("SESSION_SECRET", "methflix-stremio-static-fixed-secret-2026")

    # ----- Read/Write via SettingsManager
    REPLACE_MODE = getenv("REPLACE_MODE", "true").lower() == "true"
    HIDE_CATALOG = getenv("HIDE_CATALOG", "false").lower() == "true"
    AUTH_CHANNEL = [c.strip() for c in (getenv("AUTH_CHANNEL") or "").split(",") if c.strip()]
    TMDB_API = getenv("TMDB_API", "").strip()
    TVDB_API = getenv("TVDB_API", "").strip()
    BASE_URL = getenv("BASE_URL", "").strip().rstrip("/")
    UPSTREAM_REPO = getenv("UPSTREAM_REPO", "").strip()
    UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "").strip()
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "admin").strip()
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "admin").strip()
    SUBSCRIPTION = getenv("SUBSCRIPTION", "false").lower() == "true"
    SUBSCRIPTION_GROUP_ID = _int_env("SUBSCRIPTION_GROUP_ID")
    APPROVER_IDS = [int(x.strip()) for x in (getenv("APPROVER_IDS") or "").split(",") if x.strip().isdigit()]
    HTTP_PROXY_URL = getenv("HTTP_Proxy_URL", "").strip()
    SHOW_PROXY_AND_NON_PROXY_BOTH = getenv("SHOW_ProxyAndNonProxyBoth", "false").lower() == "true"
