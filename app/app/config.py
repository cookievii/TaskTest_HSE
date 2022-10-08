import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

DEBUG = False
SECRET_KEY = os.getenv("SECRET_KEY", default="SECRET_KEY")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("DATABASES_HOST", default="db"),
        "PORT": os.getenv("DATABASES_PORT", default="5432"),
        "NAME": os.getenv("DATABASES_NAME", default="postgres"),
        "USER": os.getenv("DATABASES_USER", default="postgres"),
        "PASSWORD": os.getenv("DATABASES_PASSWORD", default="postgres"),
    }
}

LANGUAGE_CODE = "ru-RU"

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
TIME_ZONE = "EST"
USE_I18N = True
USE_TZ = False
