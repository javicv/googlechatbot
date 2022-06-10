

class Card():
    def __init__(self) -> None:
        self.header = None
        self.sections = []

    def to_dict(self):
        resp = {}
        if self.header is not None:
            resp["header"] = self.header
        resp["sections"] = self.sections
        return resp

    def __str__(self) -> str:
        return self.to_dict().__str__()

    def __repr__(self) -> str:
        return self.to_dict().__repr__()


class CardBuilder():
    def __init__(self) -> None:
        self._card = Card()

    def add_header(self, title, subtitle=None, image_url=None, image_style="IMAGE"):
        self._card.header = {}
        self._card.header["title"] = title
        if subtitle is not None:
            self._card.header["subtitle"] = subtitle
        if image_url is not None:
            self._card.header["imageUrl"] = image_url
            self._card.header["imageStyle"] = image_style
        return self

    def create_section(self, header=None):
        section = {"widgets": []}
        if header is not None:
            section["header"] = header
        self._card.sections.append(section)
        return self

    def add_text_paragraph_widget(self, text):
        section = self._card.sections[-1]
        widget = {}
        widget["text"] = text
        section["widgets"].append({"textParagraph": widget})
        return self

    def add_image_widget(self, image_url, click_url=None):
        section = self._card.sections[-1]
        widget = {}
        widget["imageUrl"] = image_url
        if click_url is not None:
            widget["onClick"] = {"openLink": {"url": click_url}}
        section["widgets"].append({"image": widget})
        return self

    def add_keyvalue_widget(self, top_label, content=None, icon=None, multiline=False):
        section = self._card.sections[-1]
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
        return self._card
