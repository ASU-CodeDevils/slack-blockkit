import uuid

from typing import List

from .block import Block
from .composition_object import TextObject
from .block_element import BlockElement


class LayoutBlock(Block):
    """
    Defines a basic layout block. For more information, see: https://api.slack.com/reference/block-kit/blocks
    """

    def __init__(self, btype: str, block_id: str = None):
        self.btype = btype
        # generate a block ID if none is passed
        if block_id and len(block_id) > 255:
            raise AttributeError(
                f"block_id cannot be greater than 255 characters, but is {block_id}"
            )
        self.block_id = block_id if block_id else self.generate_block_id()
        super().__init__(btype=btype)
    
    @staticmethod
    def generate_block_id():
        return str(uuid.uuid4())


class ActionsBlock(LayoutBlock):
    """
    A block that is used to hold interactive elements. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#actions
    """

    def __init__(self, elements: List[BlockElement]):
        # validate_input
        if len(elements) > 5:
            raise AttributeError("cannot have more than 5 elements in action blocks")

        super().__init__(btype="actions")
        self.elements = elements


class ContextBlock(LayoutBlock):
    """
    Displays message context, which can include both images and text. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#context
    """

    def __init__(self, elements: list, block_id: str = None):
        # validate input
        if len(elements) > 10:
            raise AttributeError("cannot have more than 10 elements in context blocks")

        super().__init__(btype="context", block_id=block_id)
        self.elements = elements


class DividerBlock(LayoutBlock):
    """
    Defines a divider block. For more information, see: https://api.slack.com/reference/block-kit/blocks#divider
    """

    def __init__(self, block_id: str = None):
        super().__init__(btype="divider", block_id=block_id)


class FileBlock(LayoutBlock):
    """
    Displays a remote file. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#file
    """

    def __init__(self, external_id: str, source: str = "remote", block_id: str = None):
        super().__init__(btype="file", block_id=block_id)
        self.external_id = external_id
        self.source = source


class ImageBlock(LayoutBlock):
    """
    A simple image block, designed to make those cat photos really pop. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#image
    """

    def __init__(
        self,
        image_url: str,
        alt_text: str,
        title: TextObject = None,
        block_id: str = None,
    ):
        # validate input
        self.validate_input("image_url", image_url, max_length=3000)
        self.validate_input("alt_text", alt_text, max_length=2000)
        if title:
            title.validate_text_block(
                max_length=200, required_type=TextObject.BTYPE_PLAINTEXT
            )

        # initialize the parent
        super().__init__(btype="image", block_id=block_id)

        # set values once validation has passed
        self.image_url = image_url
        self.alt_text = alt_text
        self.title = title


class InputBlock(LayoutBlock):
    """
    A block that collects information from users - it can hold a plain-text input element, a select menu element,
    a multi-select menu element, or a datepicker. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#input
    """

    def __init__(
        self,
        label: TextObject,
        element: BlockElement,
        block_id: str = None,
        hint: TextObject = None,
        optional: bool = False,
    ):
        # validate input
        label.validate_text_block(
            max_length=2000, required_type=TextObject.BTYPE_PLAINTEXT
        )
        if hint:
            hint.validate_text_block(
                max_length=2000, required_type=TextObject.BTYPE_PLAINTEXT
            )

        super().__init__(btype="input", block_id=block_id)

        self.label = label
        self.element = element
        self.hint = hint
        self.optional = optional


class SectionBlock(LayoutBlock):
    """
    Basic section block. For more information, see: https://api.slack.com/reference/block-kit/blocks#section
    """

    def __init__(
        self,
        text: TextObject,
        block_id: str = None,
        fields: List[TextObject] = None,
        accessory: BlockElement = None,
    ):
        super().__init__(btype="section", block_id=block_id)

        # field validation
        # text can be no longer than 3000 characters
        if text.get_text_length() > 3000:
            raise AttributeError(
                f"text cannot be more than 3000 characters, but got {text.get_text_length()}"
            )

        self.text = text
        self.fields = fields
        self.accessory = accessory
