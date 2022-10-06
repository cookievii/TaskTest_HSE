import os
import sys

BUILD_TYPE = os.getenv("BUILD_TYPE", "dev")
TESTING = True if len(sys.argv) > 1 and sys.argv[1] == "test" else False

if TESTING:
    BUILD_TYPE = "test"

match BUILD_TYPE:

    case "dev":
        DEBUG = True
        SECRET_KEY = 'django-insecure-4zp#fo8+)5c#e4eo68)0@&(f)djrh8=@h(%2s_5fjhkw(k1%u4'
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "HOST": "localhost",
                "PORT": "5432",
                "NAME": "postgres",
                "USER": "postgres",
                "PASSWORD": "postgres",
            }
        }

        # LANGUAGE_CODE = "ru-RU"
        LANGUAGE_CODE = "en"

        DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
        TIME_ZONE = 'EST'
        USE_I18N = True
        USE_TZ = False

    case "test":
        DEBUG = True
        SECRET_KEY = 'django-insecure-4zp#fo8+)5c#e4eo68)0@&(f)djrh8=@h(%2s_5fjhkw(k1%u4'
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "HOST": "localhost",
                "PORT": "5432",
                "NAME": "postgres",
                "USER": "postgres",
                "PASSWORD": "postgres",
            }
        }

        LANGUAGE_CODE = "ru-RU"
        TIME_ZONE = 'EST'
        USE_I18N = False
        USE_TZ = False
