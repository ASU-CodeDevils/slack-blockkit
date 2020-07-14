from .block import Block


class TextObject(Block):
    """
    Represents a text object. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#text
    """

    BTYPE_PLAIN_TEXT = "plain_text"
    BTYPE_MARKDOWN = "mrkdwn"

    def __init__(
        self, btype: str, text: str, emoji: bool = False, verbatim: bool = False
    ):
        # validate that the type is correct
        if btype == self.BTYPE_PLAIN_TEXT or btype == self.BTYPE_MARKDOWN:
            self.btype = btype
        else:
            raise AttributeError(
                f"Invalid btype. Must be {self.BTYPE_MARKDOWN} or {self.BTYPE_PLAIN_TEXT}: {btype}"
            )

        self.text = text

        # emoji field is only usable if the type is plain text
        self.emoji = emoji and btype == self.BTYPE_PLAIN_TEXT
        self.verbatim = verbatim

    def is_plain_text(self):
        return self.btype == self.BTYPE_PLAIN_TEXT

    def is_markdown(self):
        return self.btype == self.BTYPE_MARKDOWN

    def get_text_length(self):
        return len(self.text)

    def validate_text_block(self, max_length: int = 0, required_type: str = None):
        # check that the text is not greater than the max length
        if max_length != 0 and len(self.text) > max_length:
            raise AttributeError(
                f"text object text should not be greater than {max_length} characters, but is "
                f"{len(self.text)}"
            )
        if required_type and self.btype != required_type:
            raise AttributeError(
                f"text object type should be {required_type}, but is {self.btype}"
            )

    def render(self) -> dict:
        block = {"type": self.btype, "text": self.text}

        if self.emoji:
            block.update({"emoji": self.emoji})

        if self.verbatim:
            block.update({"verbatim": self.verbatim})

        return block


class ConfirmObject(Block):
    """
    An object that defines a dialog that provides a confirmation step to any interactive element. This dialog will ask
    the user to confirm their action by offering a confirm and deny buttons. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#confirm
    """

    def __init__(
        self, title: TextObject, text: TextObject, confirm: TextObject, deny: TextObject
    ):
        # validate input
        title.validate_text_block(
            max_length=100, required_type=TextObject.BTYPE_PLAIN_TEXT
        )
        text.validate_text_block(max_length=300)
        confirm.validate_text_block(
            max_length=30, required_type=TextObject.BTYPE_PLAIN_TEXT
        )
        deny.validate_text_block(
            max_length=30, required_type=TextObject.BTYPE_PLAIN_TEXT
        )

        self.title = title
        self.text = text
        self.confirm = confirm
        self.deny = deny

    def render(self) -> dict:
        return {
            "title": self.title.render(),
            "text": self.text.render(),
            "confirm": self.confirm.render(),
            "deny": self.deny.render(),
        }


class OptionObject(Block):
    """
    An object that represents a single selectable item in a select menu, multi-select menu, radio button group,
    or overflow menu. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#option
    """

    def __init__(self, text: TextObject, value: str, url: str = None):
        # validate input
        text.validate_text_block(
            max_length=75, required_type=TextObject.BTYPE_PLAIN_TEXT
        )
        self.validate_input("value", value, max_length=75)
        self.validate_input("url", url, max_length=3000)

        self.text = text
        self.value = value
        self.url = url

    def render(self) -> dict:
        block = {"text": self.text.render(), "value": self.value}

        if self.url:
            block.update({"url": self.url})

        return block


class OptionGroupObject(Block):
    """
    Provides a way to group options in a select menu or multi-select menu. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#option_group
    """

    def __init__(self, label: TextObject, options: list):
        # validate input
        label.validate_text_block(
            max_length=75, required_type=TextObject.BTYPE_PLAIN_TEXT
        )
        if not isinstance(options[0], OptionObject):
            raise AttributeError(
                "options list needs to be a list of OptionObject objects"
            )
        if len(options) > 100:
            raise AttributeError("options list cannot exceed 100 options")

        self.label = label
        self.options = options

    @staticmethod
    def expand_options_group(options: [OptionObject]) -> list:
        ret = []
        for option in options:
            ret.append(option.render())
        return ret

    def render(self) -> dict:
        return {
            "label": self.label.render(),
            "options": self.expand_options_group(self.options),
        }
