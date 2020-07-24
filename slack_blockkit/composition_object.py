from typing import List

from .block import Block
from slack_blockkit.utils import get_validated_input


class TextObject(Block):
    """
    Represents a text object. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#text
    """

    BTYPE_PLAINTEXT = "plain_text"
    BTYPE_MARKDOWN = "mrkdwn"

    def __init__(
        self, btype: str, text: str, emoji: bool = False, verbatim: bool = False
    ):
        # validate that the type is correct
        self.btype = get_validated_input(
            btype, str, equality_fields=[self.BTYPE_PLAINTEXT, self.BTYPE_MARKDOWN]
        )
        self.text = text

        # emoji field is only usable if the type is plain text
        self.emoji = emoji and btype == self.BTYPE_PLAINTEXT
        self.verbatim = verbatim
        super().__init__(btype=btype)

    def is_plain_text(self):
        return self.btype == self.BTYPE_PLAINTEXT

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
        return self


class PlainTextObject(TextObject):
    """
    Represents a plain-text object. This is a `TextObject` where `btype` is set to *plain_text*.
    """

    def __init__(self, text: str):
        super().__init__(
            btype=TextObject.BTYPE_PLAINTEXT, text=text, emoji=False, verbatim=False
        )

    def render(self):
        vars_dict = super().render()
        vars_dict.pop("emoji"),
        vars_dict.pop("verbatim")
        return vars_dict


class MarkdownTextObject(TextObject):
    """
    Represents a markdown text object. This is a `TextObject` where `btype` is set to *mrkdwn*.
    """

    def __init__(self, text: str, emoji: bool = False, verbatim: bool = False):
        super().__init__(
            btype=TextObject.BTYPE_MARKDOWN, text=text, emoji=emoji, verbatim=verbatim
        )


class ConfirmObject(Block):
    """
    An object that defines a dialog that provides a confirmation step to any interactive element. This dialog will ask
    the user to confirm their action by offering a confirm and deny buttons. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#confirm
    """

    def __init__(
        self, title: TextObject, text: TextObject, confirm: TextObject, deny: TextObject
    ):
        super().__init__(btype=None)
        # validate input
        title.validate_text_block(
            max_length=100, required_type=TextObject.BTYPE_PLAINTEXT
        )
        self.title = title

        text.validate_text_block(max_length=300)
        self.text = text

        confirm.validate_text_block(
            max_length=30, required_type=TextObject.BTYPE_PLAINTEXT
        )
        self.confirm = confirm

        deny.validate_text_block(
            max_length=30, required_type=TextObject.BTYPE_PLAINTEXT
        )
        self.deny = deny


class OptionObject(Block):
    """
    An object that represents a single selectable item in a select menu, multi-select menu, radio button group,
    or overflow menu. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#option
    """

    TEXT_MAX_LENGTH = 75
    URL_MAX_LENGTH = 3000
    VALUE_MAX_LENGTH = 75

    def __init__(self, text: TextObject, value: str, url: str = None):
        # validate input
        text.validate_text_block(
            max_length=self.TEXT_MAX_LENGTH, required_type=TextObject.BTYPE_PLAINTEXT
        )
        super().__init__(btype=None)
        self.text = text
        self.value = get_validated_input(value, str, max_length=self.VALUE_MAX_LENGTH)
        self.url = get_validated_input(url, str, max_length=self.URL_MAX_LENGTH)


class OptionGroupObject(Block):
    """
    Provides a way to group options in a select menu or multi-select menu. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#option_group
    """

    LABEL_MAX_LENGTH = 75

    def __init__(self, label: TextObject, options: List[OptionObject]):
        # validate input
        # TODO validate label
        self.label = label.validate_text_block(
            max_length=self.LABEL_MAX_LENGTH, required_type=TextObject.BTYPE_PLAINTEXT
        )
        if not isinstance(options[0], OptionObject):
            raise AttributeError(
                "options list needs to be a list of OptionObject objects"
            )
        if len(options) > 100:
            raise AttributeError("options list cannot exceed 100 options")

        self.options = options
