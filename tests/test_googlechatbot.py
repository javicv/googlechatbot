import os
from googlechatbot import GoogleChatBot, CardBuilder

def test_googlechatbot_text():
    bot = GoogleChatBot(os.environ['CHAT_WEBHOOK'])
    resp = bot.send_text_message("test message")
    assert resp == 200, "Message not sent"

def test_googlechatbot_keyvalue():
    builder = CardBuilder()
    builder.add_header("Test", "KeyValue", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/OOjs_UI_icon_alert-yellow.svg/240px-OOjs_UI_icon_alert-yellow.svg.png")
    builder.create_section()
    builder.add_keyvalue_widget("Key","Value","STAR")
    card = builder.build()
    bot = GoogleChatBot(os.environ['CHAT_WEBHOOK'])
    resp = bot.send_card_message(card)
    assert resp == 200, "Message not sent"

def test_googlechatbot_image():
    builder = CardBuilder()
    builder.add_header("Test", "Image", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/OOjs_UI_icon_alert-yellow.svg/240px-OOjs_UI_icon_alert-yellow.svg.png")
    builder.create_section("image")
    builder.add_image_widget("https://upload.wikimedia.org/wikipedia/commons/5/58/GChat.png", "https://workspace.google.com/intl/es/products/chat/")
    card = builder.build()
    bot = GoogleChatBot(os.environ['CHAT_WEBHOOK'])
    resp = bot.send_card_message(card)
    assert resp == 200, "Message not sent"
