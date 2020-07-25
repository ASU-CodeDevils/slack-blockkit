import uuid

from typing import List

from .block import Block
from .composition_object import TextObject
from .block_element import BlockElement


class LayoutBlock(Block):
    """
    Defines a basic layout block. For more information, see: https://api.slack.com/reference/block-kit/blocks

    Args:
        btype (str): Synonymous with Slack's ``type`` parameter.
        block_id (str): A string acting as a unique identifier for a block. You can use this ``block_id`` when you
            receive an interaction payload to identify the source of the action. If not specified, a ``block_id``
            will be generated. Maximum length for this field is 255 characters.

            If not ``block_id`` is specified, a ``block_id`` is set to a random UUID v4.
    """

    def __init__(self, btype: str, block_id: str = None):
        # generate a block ID if none is passed
        if block_id and len(block_id) > 255:
            raise AttributeError(
                "block_id cannot be greater than 255 characters, but is {}".format(block_id)
            )
        self.block_id = block_id if block_id else self.generate_block_id()
        super().__init__(btype=btype)

    @staticmethod
    def generate_block_id() -> str:
        """
        Generates a UUID (v4) to be used as a block ID.

        Returns:
            str: A random UUID (v4) as a string.
        """
        return str(uuid.uuid4())


class ActionsBlock(LayoutBlock):
    """
    A block that is used to hold interactive elements. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#actions

    Args:
        elements (List[BlockElement]): An array of interactive element objects - buttons, select menus, overflow menus,
            or date pickers. There is a maximum of 5 elements in each action block.
        block_id (str): A string acting as a unique identifier for a block. You can use this ``block_id`` when you
            receive an interaction payload to identify the source of the action. If not specified, a ``block_id``
            will be generated. Maximum length for this field is 255 characters.
    """

    def __init__(self, elements: List[BlockElement], block_id: str = None):
        # validate_input
        if len(elements) > 5:
            raise AttributeError("cannot have more than 5 elements in action blocks")

        super().__init__(btype="actions", block_id=block_id)
        self.elements = elements


class ContextBlock(LayoutBlock):
    """
    Displays message context, which can include both images and text. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#context

    Args:
        elements (List[BlockElement]): An array of :class:`ImageElement` and :class:`TextObjects`. Maximum number of
            items is 10.
        block_id (str): A string acting as a unique identifier for a block. You can use this ``block_id`` when you
            receive an interaction payload to identify the source of the action. If not specified, a ``block_id``
            will be generated. Maximum length for this field is 255 characters.
    """

    def __init__(self, elements: list, block_id: str = None):
        # validate input
        if len(elements) > 10:
            raise AttributeError("cannot have more than 10 elements in context blocks")

        super().__init__(btype="context", block_id=block_id)
        self.elements = elements


class DividerBlock(LayoutBlock):
    """
    A content divider, like an ``<hr>``, to split up different blocks inside of a message. The divider block is nice
    and neat, requiring only a type.For more information, see: https://api.slack.com/reference/block-kit/blocks#divider

    Args:
        block_id (str): A string acting as a unique identifier for a block. You can use this ``block_id`` when you
            receive an interaction payload to identify the source of the action. If not specified, a ``block_id``
            will be generated. Maximum length for this field is 255 characters.
    """

    def __init__(self, block_id: str = None):
        super().__init__(btype="divider", block_id=block_id)


class FileBlock(LayoutBlock):
    """
    Displays a remote file. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#file

    Args:
        external_id (str): The external unique ID for this file.
        source (str): At the moment, ``source`` will always be remote for a *remote* file.
        block_id (str): A string acting as a unique identifier for a block. You can use this ``block_id`` when you
            receive an interaction payload to identify the source of the action. If not specified, a ``block_id``
            will be generated. Maximum length for this field is 255 characters.
    """

    def __init__(self, external_id: str, source: str = "remote", block_id: str = None):
        super().__init__(btype="file", block_id=block_id)
        self.external_id = external_id
        self.source = source


class ImageBlock(LayoutBlock):
    """
    A simple image block, designed to make those cat photos really pop. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#image

    Args:
        image_url (str): The URL of the image to be displayed. Maximum length for this field is 3000 characters.
        alt_text (str): A plain-text summary of the image. This should not contain any markup. Maximum length for
            this field is 2000 characters.
        title (TextObject): An optional title for the image in the form of a :class:`TextObject` that can only be
            of type: ``plain_text``. Maximum length for the text in this field is 2000 characters.
        block_id (str): A string acting as a unique identifier for a block. You can use this ``block_id`` when you
            receive an interaction payload to identify the source of the action. If not specified, a ``block_id``
            will be generated. Maximum length for this field is 255 characters.
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

    Args:
        label (TextObject): A label that appears above an input element in the form of a :class:`TextObject` that
            must have type of ``plain_text``. Maximum length for the text in this field is 2000 characters.
        element (BlockElement): An plain-text input element, a select menu element, a multi-select menu element, or a
            datepicker.
        block_id (str): A string acting as a unique identifier for a block. You can use this ``block_id`` when you
            receive an interaction payload to identify the source of the action. If not specified, a ``block_id``
            will be generated. Maximum length for this field is 255 characters.
        hint (TextObject): An optional hint that appears below an input element in a lighter grey. It must be a
            :class:`TextObject` with a type of ``plain_text``. Maximum length for the text in this field is 2000
            characters.
        optional (bool): A boolean that indicates whether the input element may be empty when a user submits the modal.
            Defaults to ``False``.
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

    Args:
        text (TextObject): The text for the block, in the form of a :class:`TextObject`. Maximum length for the text
            in this field is 3000 characters. This field is not required if a valid array of fields objects is provided
            instead.
        block_id (str): A string acting as a unique identifier for a block. You can use this ``block_id`` when you
            receive an interaction payload to identify the source of the action. If not specified, a ``block_id``
            will be generated. Maximum length for this field is 255 characters.
        fields (List[TextObject]): An array of :class:`TextObject`. Any text objects included with fields will be
            rendered in a compact format that allows for 2 columns of side-by-side text. Maximum number of items is 10.
            Maximum length for the text in each item is 2000 characters.
        accessory (BlockElement): One of the available :class:`ElementObject`.
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
