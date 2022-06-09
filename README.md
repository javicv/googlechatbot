# Google Chat
A small package to simplify the creation of Google Chat Bots

## Examples
### Text Messages
To send a simple text message to a Google Chat webhook
```python
from googlechatbot import GoogleChatBot

webhook_url = "https://chat.googleapis.com/v1/..."
bot = GoogleChatBot(webhook_url)
bot.send_text_message("test message")
```
### Cards
To simplify card creation there is a builder
```python
from googlechatbot import CardBuilder, GoogleChatBot

webhook_url = "https://chat.googleapis.com/v1/..."
bot = GoogleChatBot(webhook_url)

builder = CardBuilder()
builder.add_header("Title", "Subtitle", "https://example.com/images/image.png")
builder.create_section("My section")
builder.add_keyvalue_widget("Key","Value","STAR")
card = builder.build()

resp = bot.send_card_message(card)
```