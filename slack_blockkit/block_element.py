from datetime import date

from .block import Block
from .composition_object import (
    ConfirmObject,
    OptionGroupObject,
    OptionObject,
    TextObject,
)


class BlockElement(Block):
    """
    Defines a basic block element. For more information, see: https://api.slack.com/reference/block-kit/block-elements
    """

    def __init__(self, btype: str, action_id: str = None):
        # validate the action id
        if action_id and len(action_id) > 255:
            raise AttributeError(
                f"action_id cannot be more than 255 characters long, but is {len(action_id)}"
            )

        self.btype = btype
        self.action_id = action_id

    def render(self) -> dict:
        block = {"type": self.btype}

        if self.action_id:
            block.update({"action_id": self.action_id})

        return block


class ButtonElement(BlockElement):
    STYLE_PRIMARY = "primary"
    STYLE_DANGER = "danger"
    STYLE_DEFAULT = "default"

    """
    An interactive component that inserts a button. The button can be a trigger for anything from opening a simple link
    to starting a complex workflow. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#button
    """

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
            max_length=75, required_type=TextObject.BTYPE_PLAIN_TEXT
        )
        self.validate_input("url", url, max_length=3000)
        self.validate_input("value", value, max_length=2000)
        self.validate_input(
            "style",
            style,
            equality_fields=[self.STYLE_DANGER, self.STYLE_DEFAULT, self.STYLE_PRIMARY],
        )

        super().__init__(btype="button", action_id=action_id)

        self.text = text
        self.url = url
        self.value = value
        self.style = style
        self.confirm = confirm

    def render(self) -> dict:
        block = {
            "type": self.btype,
            "text": self.text.render(),
            "action_id": self.action_id,
        }

        if self.url:
            block.update({"url": self.url})
        if self.value:
            block.update({"value": self.value})
        if self.style:
            block.update({"style": self.style})
        if self.confirm:
            block.update({"confirm": self.confirm.render()})

        return block


class DatepickerElement(BlockElement):
    """
    An element which lets users easily select a date from a calendar style UI. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#datepicker
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
            max_length=150, required_type=TextObject.BTYPE_PLAIN_TEXT
        )

        # set date if not already set
        if not initial_date:
            initial_date = str(date.today())

        super().__init__(btype="datepicker", action_id=action_id)

        self.placeholder = placeholder
        self.initial_date = initial_date
        self.confirm = confirm

    def render(self) -> dict:
        block = {
            "type": self.btype,
            "action_id": self.action_id,
            "placeholder": self.placeholder.render(),
            "initial_date": self.initial_date,
        }

        if self.confirm:
            block.update({"confirm": self.confirm.render()})

        return block


class ImageElement(BlockElement):
    """
    An element to insert an image as part of a larger block of content. If you want a block with only an image in it,
    you're looking for the image block. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#image
    """

    def __init__(self, image_url: str, alt_text: str):
        super().__init__(btype="image")
        self.image_url = image_url
        self.alt_text = alt_text

    def render(self) -> dict:
        return {
            "type": self.btype,
            "image_url": self.image_url,
            "alt_text": self.alt_text,
        }


class OverflowElement(BlockElement):
    """
    This is like a cross between a button and a select menu - when a user clicks on this overflow button, they will be
    presented with a list of options to choose from. Unlike the select menu, there is no typeahead field, and the
    button always appears with an ellipsis ("…") rather than customisable text. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#overflow
    """

    def __init__(
        self, action_id: str, options: [OptionObject], confirm: ConfirmObject = None
    ):
        # validate input
        if len(options) > 5 or len(options) < 2:
            raise AttributeError("Must have between 2 and 5 options (inclusive)")
        super().__init__(btype="overflow", action_id=action_id)
        self.options = options
        self.confirm = confirm

    def render(self) -> dict:
        block = {
            "type": self.btype,
            "action_id": self.action_id,
            "options": OptionGroupObject.expand_options_group(self.options),
        }

        if self.confirm:
            block.update({"confirm": self.confirm.render()})

        return block


class PlainTextInputElement(BlockElement):
    """
    A plain-text input, similar to the HTML <input> tag, creates a field where a user can enter freeform data. It can
    appear as a single-line field or a larger textarea using the multiline flag. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#input
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
                max_length=150, required_type=TextObject.BTYPE_PLAIN_TEXT
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

    def render(self) -> dict:
        block = {
            "type": self.btype,
            "action_id": self.action_id,
            "multiline": self.multiline,
        }

        if self.placeholder:
            block.update({"placeholder": self.placeholder.render()})
        if self.initial_value:
            block.update({"initial_value": self.initial_value})
        if self.min_length != 0:
            block.update({"min_length": self.min_length})
        if self.max_length != 0:
            block.update({"max_length": self.max_length})

        return block


class RadioButtonGroupElement(BlockElement):
    """
    A radio button group that allows a user to choose one item from a list of possible options. For more information,
    see: https://api.slack.com/reference/block-kit/block-elements#radio
    """

    def __init__(
        self,
        action_id: str,
        options: [OptionObject],
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

    def render(self) -> dict:
        block = {
            "type": self.btype,
            "action_id": self.action_id,
            "options": OptionGroupObject.expand_options_group(self.options),
        }

        if self.initial_option:
            block.update({"initial_option": self.initial_option.render()})
        if self.confirm:
            block.update({"confirm": self.confirm.render()})

        return block
