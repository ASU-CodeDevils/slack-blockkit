from typing import List

from .block import Block
from slack_blockkit.utils import get_validated_input


class TextObject(Block):
    """
    An object containing some text, formatted either as *plain_text* or using *mrkdwn*, our proprietary
    textual markup that's just different enough from Markdown to frustrate you.
    https://api.slack.com/reference/block-kit/composition-objects#text

    Args:
        btype (str): The text for the block. This field accepts any of the standard text formatting markup
            when ``btype`` is *mrkdwn*.
        text (str): The text for the block. This field accepts any of the standard text formatting markup
            when ``btype`` is *mrkdwn*.
        emoji (bool): Indicates whether emojis in a text field should be escaped into the colon emoji format.
            This field is only usable when type is ``plain_text``.
        verbatim (bool): When set to false (as is default) URLs will be auto-converted into links, conversation
            names will be link-ified, and certain mentions will be automatically parsed. Using a value of ``True``
            will skip any preprocessing of this nature, although you can still include manual parsing strings.
            This field is only usable when ``btype`` is *mrkdwn*.
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
        if btype == self.BTYPE_PLAINTEXT:
            self.emoji = emoji
        # verbatim field is only usable if the type is markdown
        else:
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
    Represents a plain-text object. This is a :class:`TextObject` where ``btype`` is set to *plain_text*.

    Args:
        text (str): The text for the block. This field accepts any of the standard text formatting markup
            when ``btype`` is *mrkdwn*.
        emoji (bool): Indicates whether emojis in a text field should be escaped into the colon emoji format.
    """

    def __init__(self, text: str, emoji: bool = False):
        super().__init__(btype=TextObject.BTYPE_PLAINTEXT, text=text, emoji=emoji)


class MarkdownTextObject(TextObject):
    """
    Represents a markdown text object. This is a :class:`TextObject` where ``btype`` is set to *mrkdwn*.

    Args:
        text (str): The text for the block. This field accepts any of the standard text formatting markup
            when ``btype`` is *mrkdwn*.
        verbatim (bool): When set to false (as is default) URLs will be auto-converted into links, conversation
            names will be link-ified, and certain mentions will be automatically parsed. Using a value of ``True``
            will skip any preprocessing of this nature, although you can still include manual parsing strings.
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

    Args:
        title (TextObject): A ``plain_text`` -only :class:`TextObject` that defines the dialog's title. Maximum length
            for this field is 100 characters.
        text (TextObject): A :class:`TextObject` that defines the explanatory text that appears in the confirm dialog.
            Maximum length for the text in this field is 300 characters.
        confirm (TextObject): A ``plain_text`` -only :class:`TextObject` to define the text of the button that confirms
            the action. Maximum length for the text in this field is 30 characters.
        deny (TextObject): A ``plain_text`` -only :class:`TextObject` to define the text of the button that cancels
            the action. Maximum length for the text in this field is 30 characters.
        style (str): Defines the color scheme applied to the confirm button. A value of ``danger`` will display the
            button with a red background on desktop, or red text on mobile. A value of ``primary`` will display the
            button with a green background on desktop, or blue text on mobile. If this field is not provided, the
            default value will be ``primary``.
    """

    def __init__(
        self,
        title: TextObject,
        text: TextObject,
        confirm: TextObject,
        deny: TextObject,
        style: str = "primary",
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

        self.style = get_validated_input(
            style, str, equality_fields=["danger", "primary"]
        )


class OptionObject(Block):
    """
    An object that represents a single selectable item in a select menu, multi-select menu, radio button group,
    or overflow menu. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#option

    Args:
        text (TextObject): A :class:`TextObject` that defines the text shown in the option on the menu. Overflow,
            select, and multi-select menus can only use ``plain_text`` objects, while radio buttons and checkboxes
            can use ``mrkdwn`` text objects. Maximum length for the text in this field is 75 characters.
        value (str): The string value that will be passed to your app when this option is chosen. Maximum length
            for this field is 75 characters.
        description (TextObject): Optional; A ``plain_text`` only :class:`TextObject` that defines a line of
            descriptive text shown below the text field beside the radio button. Maximum length for the text
            object within this field is 75 characters.
        url (str): A URL to load in the user's browser when the option is clicked. The ``url`` attribute is only
            available in overflow menus. Maximum length for this field is 3000 characters. If you're using ``url``,
            you'll still receive an interaction payload and will need to send an acknowledgement response.
    """

    TEXT_MAX_LENGTH = 75
    URL_MAX_LENGTH = 3000
    VALUE_MAX_LENGTH = 75

    def __init__(
        self,
        text: TextObject,
        value: str,
        description: TextObject = None,
        url: str = None,
    ):
        # validate input
        text.validate_text_block(
            max_length=self.TEXT_MAX_LENGTH, required_type=TextObject.BTYPE_PLAINTEXT
        )
        super().__init__(btype=None)
        self.text = text
        if description:
            description.validate_text_block(
                max_length=self.TEXT_MAX_LENGTH,
                required_type=TextObject.BTYPE_PLAINTEXT,
            )
            self.description = description
        self.value = get_validated_input(value, str, max_length=self.VALUE_MAX_LENGTH)
        self.url = get_validated_input(url, str, max_length=self.URL_MAX_LENGTH)


class OptionGroupObject(Block):
    """
    Provides a way to group options in a select menu or multi-select menu. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#option_group

    Args:
        label (TextObject): A ``plain_text`` only :class:`TextObject` that defines the label shown above
            this group of options. Maximum length for the text in this field is 75 characters.
        options (List[OptionObject]): An array of :class:`OptionObject` that belong to this specific group.
            Maximum of 100 items.
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
