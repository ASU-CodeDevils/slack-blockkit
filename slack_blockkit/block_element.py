from datetime import date
from typing import List

from .block import Block
from .composition_object import (
    ConfirmObject,
    OptionObject,
    TextObject,
)
from slack_blockkit.utils import get_validated_input


class BlockElement(Block):
    """
    Defines a basic block element. For more information, see: https://api.slack.com/reference/block-kit/block-elements

    Args:
        btype (str): Synonymous with Slack's ``type`` parameter.
        action_id (str): The unique action ID.
    """

    def __init__(self, btype: str, action_id: str = None):
        # validate the action id
        self.action_id = get_validated_input(
            action_id, str, min_length=0, max_length=255
        )
        super().__init__(btype=btype)


class ButtonElement(BlockElement):
    """
    An interactive component that inserts a button. The button can be a trigger for anything from opening a simple link
    to starting a complex workflow. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#button

    Args:
        text (TextObject): A text object that defines the button's text. Can only be of type: plain_text.
            Maximum length for the text in this field is 75 characters.
        action_id (str):  	An identifier for this action. You can use this when you receive an interaction
            payload to identify the source of the action. Should be unique among all other action_ids used
            elsewhere by your app. Maximum length for this field is 255 characters.
        url (str): A URL to load in the user's browser when the button is clicked. Maximum length for this
            field is 3000 characters. If you're using url, you'll still receive an interaction payload and
            will need to send an acknowledgement response.
        value (str): The value to send along with the interaction payload. Maximum length for this field is
            2000 characters.
        style (str): Decorates buttons with alternative visual color schemes. Use this option with restraint.

            ``primary`` gives buttons a green outline and text, ideal for affirmation or confirmation actions.
            ``primary`` should only be used for one button within a set.

            ``danger`` gives buttons a red outline and text, and should be used when the action is destructive.
            Use ``danger`` even more sparingly than primary.

            If you don't include this field, the ``default`` button style will be used.

    """

    STYLE_PRIMARY = "primary"
    STYLE_DANGER = "danger"
    STYLE_DEFAULT = "default"

    def __init__(
        self,
        text: TextObject,
        action_id: str,
        url: str = None,
        value: str = None,
        style: str = "default",
        confirm: ConfirmObject = None,
    ):
        # validate input
        text.validate_text_block(
            max_length=75, required_type=TextObject.BTYPE_PLAINTEXT
        )
        self.validate_input("url", url, max_length=3000)
        self.validate_input("value", value, max_length=2000)
        self.validate_input(
            "style",
            style,
            equality_fields=[self.STYLE_DANGER, self.STYLE_DEFAULT, self.STYLE_PRIMARY],
        )

        self.text = text
        self.url = url
        self.value = value
        self.style = style
        self.confirm = confirm

        super().__init__(btype="button", action_id=action_id)


class PrimaryButtonElement(ButtonElement):
    """
    A :class:`ButtonElement` whose ``style`` is ``primary``.

    Args:
        text (TextObject): A text object that defines the button's text. Can only be of type: plain_text.
            Maximum length for the text in this field is 75 characters.
        action_id (str):  	An identifier for this action. You can use this when you receive an interaction
            payload to identify the source of the action. Should be unique among all other action_ids used
            elsewhere by your app. Maximum length for this field is 255 characters.
        url (str): A URL to load in the user's browser when the button is clicked. Maximum length for this
            field is 3000 characters. If you're using url, you'll still receive an interaction payload and
            will need to send an acknowledgement response.
        value (str): The value to send along with the interaction payload. Maximum length for this field is
            2000 characters.
    """

    def __init__(
        self,
        text: TextObject,
        action_id: str,
        url: str = None,
        value: str = None,
        confirm: ConfirmObject = None,
    ):
        super().__init__(
            style=ButtonElement.STYLE_PRIMARY,
            text=text,
            action_id=action_id,
            url=url,
            value=value,
            confirm=confirm,
        )


class DangerButtonElement(ButtonElement):
    """
    A :class:`ButtonElement` whose ``style`` is ``danger``.

    Args:
        text (TextObject): A text object that defines the button's text. Can only be of type: plain_text.
            Maximum length for the text in this field is 75 characters.
        action_id (str):  	An identifier for this action. You can use this when you receive an interaction
            payload to identify the source of the action. Should be unique among all other action_ids used
            elsewhere by your app. Maximum length for this field is 255 characters.
        url (str): A URL to load in the user's browser when the button is clicked. Maximum length for this
            field is 3000 characters. If you're using url, you'll still receive an interaction payload and
            will need to send an acknowledgement response.
        value (str): The value to send along with the interaction payload. Maximum length for this field is
            2000 characters.
    """

    def __init__(
        self,
        text: TextObject,
        action_id: str,
        url: str = None,
        value: str = None,
        confirm: ConfirmObject = None,
    ):
        super().__init__(
            style=ButtonElement.STYLE_DANGER,
            text=text,
            action_id=action_id,
            url=url,
            value=value,
            confirm=confirm,
        )


class DefaultButtonElement(ButtonElement):
    """
    A :class:`ButtonElement` whose ``style`` is ``default``.

    Args:
        text (TextObject): A text object that defines the button's text. Can only be of type: plain_text.
            Maximum length for the text in this field is 75 characters.
        action_id (str):  	An identifier for this action. You can use this when you receive an interaction
            payload to identify the source of the action. Should be unique among all other action_ids used
            elsewhere by your app. Maximum length for this field is 255 characters.
        url (str): A URL to load in the user's browser when the button is clicked. Maximum length for this
            field is 3000 characters. If you're using url, you'll still receive an interaction payload and
            will need to send an acknowledgement response.
        value (str): The value to send along with the interaction payload. Maximum length for this field is
            2000 characters.
    """

    def __init__(
        self,
        text: TextObject,
        action_id: str,
        url: str = None,
        value: str = None,
        confirm: ConfirmObject = None,
    ):
        super().__init__(
            style=ButtonElement.STYLE_DEFAULT,
            text=text,
            action_id=action_id,
            url=url,
            value=value,
            confirm=confirm,
        )


class DatepickerElement(BlockElement):
    """
    An element which lets users easily select a date from a calendar style UI. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#datepicker

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. You can use
            this when you receive an interaction payload to identify the source of the action. Should be unique
            among all other action_ids used elsewhere by your app. Maximum length for this field is 255 characters.
        placeholder (TextObject): A ``plain_text`` only text object that defines the placeholder text shown on the
            datepicker. Maximum length for the text in this field is 150 characters.
        initial_date (str): The initial date that is selected when the element is loaded. This should be in the format
            ``YYYY-MM-DD``.
        confirm (ConfirmObject): A :class:`ConfirmObject` that defines an optional confirmation dialog that appears
            after a date is selected.
    """

    def __init__(
        self,
        action_id: str,
        placeholder: TextObject,
        initial_date: str = None,
        confirm: ConfirmObject = None,
    ):
        # validate input
        placeholder.validate_text_block(
            max_length=150, required_type=TextObject.BTYPE_PLAINTEXT
        )

        # set date if not already set
        if not initial_date:
            initial_date = str(date.today())

        super().__init__(btype="datepicker", action_id=action_id)

        self.placeholder = placeholder
        self.initial_date = initial_date
        self.confirm = confirm


class ImageElement(BlockElement):
    """
    An element to insert an image as part of a larger block of content. If you want a block with only an image in it,
    you're looking for the image block. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#image

    Args:
        image_url (str): The URL of the image to be displayed.
        alt_text (str): A plain-text summary of the image. This should not contain any markup.
    """

    def __init__(self, image_url: str, alt_text: str):
        super().__init__(btype="image")
        self.image_url = image_url
        self.alt_text = alt_text


class OverflowElement(BlockElement):
    """
    This is like a cross between a button and a select menu - when a user clicks on this overflow button, they will be
    presented with a list of options to choose from. Unlike the select menu, there is no typeahead field, and the
    button always appears with an ellipsis ("…") rather than customisable text. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#overflow

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. You can use this when
            you receive an interaction payload to identify the source of the action. Should be unique among all other
            ``action_id`` used elsewhere by your app. Maximum length for this field is 255 characters.
        options (List[OptionObject]): An array of :class:`OptionObject` to display in the menu. Maximum number of
            options is 5, minimum is 2.
        confirm (ConfirmObject): A :class:`ConfirmObject` that defines an optional confirmation dialog that appears
            after a menu item is selected.
    """

    def __init__(
        self, action_id: str, options: List[OptionObject], confirm: ConfirmObject = None
    ):
        # validate input
        if options and (len(options) > 5 or len(options) < 2):
            raise AttributeError("Must have between 2 and 5 options (inclusive)")
        super().__init__(btype="overflow", action_id=action_id)
        self.options = options
        self.confirm = confirm


class PlainTextInputElement(BlockElement):
    """
    A plain-text input, similar to the HTML <input> tag, creates a field where a user can enter freeform data. It can
    appear as a single-line field or a larger textarea using the multiline flag. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#input

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. You can use this when
            you receive an interaction payload to identify the source of the action. Should be unique among all other
            ``action_id`` used elsewhere by your app. Maximum length for this field is 255 characters.
        placeholder (TextObject): Optionall A ``plain_text`` only text object that defines the placeholder text shown
            in the plain-text input. Maximum length for the text in this field is 150 characters.
        initial_value (str): Optional; The initial value in the plain-text input when it is loaded.
        multiline (bool): Optional; Indicates whether the input will be a single line (``False``) or a larger textarea
            (``True``). Defaults to ``False``.
        min_length (int): The minimum length of input that the user must provide. If the user provides less, they will
            receive an error. Maximum value is 3000.
        max_length (int): The maximum length of input that the user can provide. If the user provides more, they will
            receive an error.
    """

    def __init__(
        self,
        action_id: str,
        placeholder: TextObject = None,
        initial_value: str = None,
        multiline: bool = False,
        min_length: int = 0,
        max_length: int = 0,
    ):
        # validate input
        if placeholder:
            placeholder.validate_text_block(
                max_length=150, required_type=TextObject.BTYPE_PLAINTEXT
            )

        if min_length != 0 or max_length != 0:
            if min_length > max_length:
                raise AttributeError(
                    f"max_length ({max_length}) must be greater than min_length ({min_length})"
                )
            if min_length < 0 or min_length > 3000:
                raise AttributeError(
                    f"min_length ({min_length}) must be between 0 and 3000 (inclusive)"
                )
            if max_length < 0 or max_length > 3000:
                raise AttributeError(
                    f"max_length ({max_length}) must be between 0 and 3000 (inclusive)"
                )

        super().__init__(btype="plain_text_input", action_id=action_id)

        self.placeholder = placeholder
        self.initial_value = initial_value
        self.multiline = multiline
        self.min_length = min_length
        self.max_length = max_length


class RadioButtonGroupElement(BlockElement):
    """
    A radio button group that allows a user to choose one item from a list of possible options. For more information,
    see: https://api.slack.com/reference/block-kit/block-elements#radio

    Args:
        action_id (str): An identifier for the action triggered when a menu option is selected. You can use this when
            you receive an interaction payload to identify the source of the action. Should be unique among all other
            ``action_id`` used elsewhere by your app. Maximum length for this field is 255 characters.
        options (List[OptionObject]): An array of :class:`OptionObject`.
        initial_option (OptionObject): An :class:`OptionObject` that exactly matches one of the options within options.
            This option will be selected when the radio button group initially loads.
        confirm (ConfirmObject): A :class:`ConfirmObject` that defines an optional confirmation dialog that appears
            after clicking one of the radio buttons in this element.
    """

    def __init__(
        self,
        action_id: str,
        options: List[OptionObject],
        intitial_option: OptionObject = None,
        confirm: ConfirmObject = None,
    ):
        # validate input
        if intitial_option and intitial_option not in options:
            raise AttributeError("initial_option must be an option within options")
        super().__init__(btype="radio_buttons", action_id=action_id)

        self.options = options
        self.initial_option = intitial_option
        self.confirm = confirm
