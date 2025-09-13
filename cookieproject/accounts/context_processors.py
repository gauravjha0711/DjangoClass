from django.core import signing
from django.conf import settings

COOKIE_SIGNER_SALT = "accounts.cookie.salt"
COOKIE_MAX_AGE = 24 * 60 * 60  

def _unsign_cookie(request, key):
    raw = request.COOKIES.get(key)
    if not raw:
        return None
    try:
        return signing.loads(raw, salt=COOKIE_SIGNER_SALT, max_age=COOKIE_MAX_AGE)
    except Exception:
        return None

def user_preferences(request):
    return {
        "theme_color": _unsign_cookie(request, "theme_color") or "light",
        "language": _unsign_cookie(request, "language") or "en",
    }
