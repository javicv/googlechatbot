import json
import requests
from .chat_card import Card


class GoogleChatBot():
    def __init__(self, url: str) -> None:
        self.endpoint = url

    def send_text_message(self, text: str) -> int:
        msg = {"text": text}
        return self.__send_message(json.dumps(msg))

    def send_card_message(self, card: Card) -> int:
        msg = {"cards": [card.to_dict()]}
        return self.__send_message(json.dumps(msg))

    def __send_message(self, msg: str) -> int:
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        resp = requests.post(self.endpoint, msg, headers=headers)
        return resp.status_code
