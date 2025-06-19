# Knife Monitor Worker

Моніторить появу ножів по ключових словах на сайтах і в сабредіті r/Knife_Swap. Надсилає сповіщення в Telegram.

## Що підтримує:
- Перевірка сайтів: [marksoutdoors.com](https://marksoutdoors.com), [dlttrading.com](https://www.dlttrading.com), [usamadeblade.com](https://usamadeblade.com), [georgeknives.bigcartel.com](https://georgeknives.bigcartel.com), [lantacknives.com](https://lantacknives.com), [tacticalelements.com](https://www.tacticalelements.com)
- Моніторинг Reddit: r/Knife_Swap

## Ключові слова:
Vecp, Talos, Sonora, Mk3, Les George, 0620, 0630, 0920, 0301, 0302, 0303

## Запуск:
```bash
pip install -r requirements.txt
python main.py
```

## Використовуються змінні середовища:
- TELEGRAM_TOKEN
- TELEGRAM_CHAT_ID
- REDDIT_CLIENT_ID
- REDDIT_CLIENT_SECRET
- REDDIT_USERNAME
- REDDIT_PASSWORD