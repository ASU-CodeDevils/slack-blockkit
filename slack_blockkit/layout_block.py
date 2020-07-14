from .block import Block
from .composition_object import TextObject
from .block_element import BlockElement


class LayoutBlock(Block):
    """
    Defines a basic layout block. For more information, see: https://api.slack.com/reference/block-kit/blocks
    """

    def __init__(self, btype: str, block_id: str = None):
        if block_id and len(block_id) > 255:
            raise AttributeError(
                f"block_id cannot be greater than 255 characters, but is {block_id}"
            )

        self.btype = btype
        self.block_id = block_id

    def render(self) -> dict:
        block = {"type": self.btype}

        if self.block_id:
            block.update({"block_id": self.block_id})

        return block


class ActionsBlock(LayoutBlock):
    """
    A block that is used to hold interactive elements. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#actions
    """

    def __init__(self, elements: list, block_id: str = None):
        # validate_input
        if len(elements) > 5:
            raise AttributeError("cannot have more than 5 elements in action blocks")

        super().__init__(btype="actions", block_id=block_id)
        self.elements = elements

    def render(self) -> dict:
        block = {"type": self.btype, "elements": self.elements}

        if self.block_id:
            block.update({"block_id": self.block_id})

        return block


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

    def render(self) -> dict:
        block = {"type": self.btype, "elements": self.elements}

        if self.block_id:
            block.update({"block_id": self.block_id})

        return block


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

    def render(self) -> dict:
        block = {
            "type": self.btype,
            "external_id": self.external_id,
            "source": self.source,
        }

        if self.block_id:
            block.update({"block_id": self.block_id})

        return block


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
                max_length=200, required_type=TextObject.BTYPE_PLAIN_TEXT
            )

        # initialize the parent
        super().__init__(btype="image", block_id=block_id)

        # set values once validation has passed
        self.image_url = image_url
        self.alt_text = alt_text
        self.title = title

    def render(self) -> dict:
        block = {
            "type": self.btype,
            "image_url": self.image_url,
            "alt_text": self.alt_text,
        }

        # add optional fields if specified
        if self.title:
            block.update({"title": self.title.render()})
        if self.block_id:
            block.update({"block_id": self.block_id})

        return block


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
            max_length=2000, required_type=TextObject.BTYPE_PLAIN_TEXT
        )
        if hint:
            hint.validate_text_block(
                max_length=2000, required_type=TextObject.BTYPE_PLAIN_TEXT
            )

        super().__init__(btype="input", block_id=block_id)

        self.label = label
        self.element = element
        self.hint = hint
        self.optional = optional

    def render(self) -> dict:
        block = {
            "type": self.btype,
            "label": self.label,
            "element": self.element,
            "optional": self.optional,
        }

        if self.block_id:
            block.update({"block_id", self.block_id})
        if self.hint:
            block.update({"hint": self.hint})

        return block


class SectionBlock(LayoutBlock):
    """
    Basic section block. For more information, see: https://api.slack.com/reference/block-kit/blocks#section
    """

    def __init__(
        self,
        text: TextObject,
        block_id: str = None,
        fields: list = None,
        accessory: BlockElement = None,
    ):
        super().__init__(btype="section", block_id=block_id)

        # field validation
        # text can be no longer than 3000 characters
        if text.get_text_length() > 3000:
            raise AttributeError(
                f"text cannot be more than 3000 characters, but got {text.get_text_length()}"
            )

        if block_id and len(block_id) > 255:
            raise AttributeError(
                f"block_id cannot be more than 255 characters, but got {len(block_id)}"
            )

        self.text = text
        self.block_id = block_id
        self.fields = fields
        self.accessory = accessory

    def render(self) -> dict:
        block = {
            "type": self.btype,
            "text": self.text.render(),
        }

        if self.block_id:
            block.update({"block_id": self.block_id})
        if self.fields:
            block.update({"fields": self.fields})
        if self.accessory:
            block.update({"accessory": self.accessory.render()})

        return block
