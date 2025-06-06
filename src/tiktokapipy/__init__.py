from collections import defaultdict
import pydantic_core

# Monkeypatching pydantic_core.SchemaValidator.validate_python
old_validate_python = pydantic_core.SchemaValidator.validate_python

def patched_validate_python(*args, **kwargs):
    if getattr(args[0], 'title') == 'VideoPage':
        try:
            args[1]['itemInfo']['itemStruct']['video']['subtitleInfos'] = []
        except KeyError:
            pass
    return old_validate_python(*args, **kwargs)

pydantic_core.SchemaValidator.validate_python = patched_validate_python

class TikTokAPIError(Exception):
    """Raised when the API encounters an error"""

    pass


class TikTokAPIWarning(RuntimeWarning):
    pass


ERROR_CODES = defaultdict(
    lambda: "Unknown Error",
    {
        0: "OK",
        450: "CLIENT_PAGE_ERROR",
        10000: "VERIFY_CODE",
        10101: "SERVER_ERROR_NOT_500",
        10102: "USER_NOT_LOGIN",
        10111: "NET_ERROR",
        10113: "SHARK_SLIDE",
        10114: "SHARK_BLOCK",
        10119: "LIVE_NEED_LOGIN",
        10202: "USER_NOT_EXIST",
        10203: "MUSIC_NOT_EXIST",
        10204: "VIDEO_NOT_EXIST",
        10205: "HASHTAG_NOT_EXIST",
        10208: "EFFECT_NOT_EXIST",
        10209: "HASHTAG_BLACK_LIST",
        10210: "LIVE_NOT_EXIST",
        10211: "HASHTAG_SENSITIVITY_WORD",
        10212: "HASHTAG_UNSHELVE",
        10213: "VIDEO_LOW_AGE_M",
        10214: "VIDEO_LOW_AGE_T",
        10215: "VIDEO_ABNORMAL",
        10216: "VIDEO_PRIVATE_BY_USER",
        10217: "VIDEO_FIRST_REVIEW_UNSHELVE",
        10218: "MUSIC_UNSHELVE",
        10219: "MUSIC_NO_COPYRIGHT",
        10220: "VIDEO_UNSHELVE_BY_MUSIC",
        10221: "USER_BAN",
        10222: "USER_PRIVATE",
        10223: "USER_FTC",
        10224: "GAME_NOT_EXIST",
        10225: "USER_UNIQUE_SENSITIVITY",
        10227: "VIDEO_NEED_RECHECK",
        10228: "VIDEO_RISK",
        10229: "VIDEO_R_MASK",
        10230: "VIDEO_RISK_MASK",
        10231: "VIDEO_GEOFENCE_BLOCK",
        10404: "FYP_VIDEO_LIST_LIMIT",
        "undefined": "MEDIA_ERROR",
    },
)
