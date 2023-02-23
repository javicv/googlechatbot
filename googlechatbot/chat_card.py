from dataclasses import dataclass, field
import logging


@dataclass(frozen=True)
class Card:
    header: dict = field(default_factory=dict)
    sections: list = field(default_factory=list)


class CardBuilder():
    def __init__(self) -> None:
        self.__card = Card()

    def add_header(self, title, subtitle=None, image_url=None, image_style="IMAGE"):
        logging.warning("This method is deprecated and it will be removed in a future version. Please use set_header insted.")
        return self.set_header(title, subtitle, image_url, image_style)

    def set_header(self, title, subtitle=None, image_url=None, image_style="IMAGE"):
        self.__card.header["title"] = title
        if subtitle is not None:
            self.__card.header["subtitle"] = subtitle
        if image_url is not None:
            self.__card.header["imageUrl"] = image_url
            self.__card.header["imageStyle"] = image_style
        return self

    def create_section(self, header=None):
        section = {"widgets": []}
        if header is not None:
            section["header"] = header
        self.__card.sections.append(section)
        return self

    def add_text_paragraph_widget(self, text):
        section = self.__card.sections[-1]
        widget = {}
        widget["text"] = text
        section["widgets"].append({"textParagraph": widget})
        return self

    def add_image_widget(self, image_url, click_url=None):
        section = self.__card.sections[-1]
        widget = {}
        widget["imageUrl"] = image_url
        if click_url is not None:
            widget["onClick"] = {"openLink": {"url": click_url}}
        section["widgets"].append({"image": widget})
        return self

    def add_keyvalue_widget(self, top_label, content=None, icon=None, multiline=False):
        section = self.__card.sections[-1]
        widget = {}
        widget["topLabel"] = top_label
        if content is not None:
            widget["content"] = content
            widget["contentMultiline"] = multiline
        if icon is not None:
            widget["icon"] = icon
        section["widgets"].append({"keyValue": widget})
        return self

    def build(self) -> Card:
        return self.__card
