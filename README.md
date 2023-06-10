# brs-urfu-bot

Telegram bot to notify about estimates changing. I have made a similar simplier copy of brs urfu bot, because I didn't want to share my username and password data to unknown creator of the popular bot. My bot can refresh much more frequently and also don't require any database.   

## Preview

- Example of the notification:
![Example of the notification](https://github.com/yphwd/brs-urfu-bot/attachments/preview.jpg)

- Example of the json data cache file located in `/cache/cache.json` (this folder and file creates automatically when script is executed):
![Example of the json data cache file located in "/cache/cache.json"](https://github.com/yphwd/brs-urfu-bot/attachments/json.jpg)

## Installation

```
pip install -r requirements.txt
```

(required Python 3+)

## .env configuration

```
BOT_TOKEN=
URFU_USERNAME=
URFU_PASSWORD=

// refresh time is in seconds
REFRESH_TIME=10 
```

## Usage

Run the command from the root dir:

```
python main.py
```