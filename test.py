import calendar
from datetime import datetime, timedelta

cb = {
    "id": "3524385853443878889",
    "from": {
        "id": 820585026,
        "is_bot": false,
        "first_name": "Eugene",
        "last_name": "Lavrenko",
        "username": "Perihelion_it",
        "language_code": "ru"
            },
    "message": {
        "message_id": 199,
        "from": {
            "id": 5577156730,
            "is_bot": true,
            "first_name": "Джон Сига",
            "username": "devlev_NSFW_Bot"
                },
        "chat": {
            "id": 820585026,
            "first_name": "Eugene",
            "last_name": "Lavrenko",
            "username": "Perihelion_it",
            "type": "private"
                            },
        "date": 1658828373,
        "reply_to_message": {
            "message_id": 198,
            "from": {
                "id": 820585026,
                "is_bot": false,
                "first_name": "Eugene",
                "last_name": "Lavrenko",
                "username": "Perihelion_it",
                "language_code": "ru"
                    },
            "chat": {
                "id": 820585026,
                "first_name": "Eugene",
                "last_name": "Lavrenko",
                "username": "Perihelion_it",
                "type": "private"
                    },
            "date": 1658828373,
            "text": "/menu",
            "entities": [{"type": "bot_command", "offset": 0, "length": 5}]},
        "text": "Главное меню",
        "reply_markup": {
            "inline_keyboard": [[{"text": "Следующая неделя", "callback_data": "week2"},
                                 {"text": "Эта неделя", "callback_data": "week1"}]]}},
    "chat_instance": "717619463786866456", "data": "week1"}


mesg = {
    "message_id": 199,
    "from": {"id": 5577156730, "is_bot": true, "first_name": "Джон Сига", "username": "devlev_NSFW_Bot"},
    "chat": {"id": 820585026, "first_name": "Eugene", "last_name": "Lavrenko", "username": "Perihelion_it", "type": "private"},
    "date": 1658828373,
    "reply_to_message": {"message_id": 198, "from": {"id": 820585026, "is_bot": false, "first_name": "Eugene", "last_name": "Lavrenko", "username": "Perihelion_it", "language_code": "ru"}, "chat": {"id": 820585026, "first_name": "Eugene", "last_name": "Lavrenko", "username": "Perihelion_it", "type": "private"}, "date": 1658828373, "text": "/menu", "entities": [{"type": "bot_command", "offset": 0, "length": 5}]}, "text": "Главное меню", "reply_markup": {"inline_keyboard": [[{"text": "Следующая неделя", "callback_data": "week2"}, {"text": "Эта неделя", "callback_data": "week1"}]]}}