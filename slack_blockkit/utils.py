from typing import List

from .block import Block
from .block_element import BlockElement, ImageElement
from .composition_object import TextObject
from .layout_block import SectionBlock

Blocks = List[dict]


def get_blocks(*blocks) -> Blocks:
    """
    Takes arguments of `Block` objects and generates a list of blocks ready to be inserted into
    a message payload.

    :param args: An argument list of Block objects. Objects will be inserted top to bottom as they
        appear in this list.
    :return: A list of the dict representations of block objects.
    :rtype: Blocks
    """
    block_list = []
    attribute_error_index = 0

    for block in blocks:
        # want only blocks in the block builder. since the util class has other methods that return
        # dicts, this will also allow dicts to be inserted
        if not isinstance(block, (Block, dict)):
            raise AttributeError(
                "Block at argument {index} improperly formatted".format(
                    index=attribute_error_index
                )
            )

        block_list.append(block.render() if isinstance(block, Block) else block)
        attribute_error_index += 1

    return block_list


def get_checkmark(task_completed: bool) -> str:
    """
    Returns a check mark emoji indicating the completed task status. If the task is complete, then a white check
    mark is returned. If not, an empty white square is.

    :param task_completed: Whether or not the task was complete.
    :type task_completed: bool
    :return: A checkmark emoji string based on whether or not the task was completed.
    :rtype: str
    """
    if task_completed:
        return ":white_check_mark:"
    return ":white_large_square:"


def get_information_block(info_link: str, info_text: str) -> dict:
    """
    Returns an information block, which is a section with an info icon followed by linked text.

    :param info_link: The link the block redirects the user to.
    :type info_link: str
    :param info_text: The link text.
    :type info_text: str
    :return: A dict in the format of a context block.
    :rtype: dict
    """
    information = f":information_source: *<{info_link}|{info_text}>*"
    return TextObject(btype=TextObject.BTYPE_MARKDOWN, text=information).render()


def get_text_block_with_accessory(text_object: TextObject, accessory: BlockElement) -> dict:
    """
    Returns a text block with an accessory.

    :param text_object: The text block object.
    :type text_object: TextObject
    :param accessory: The accessory object.
    :type accessory: LayoutBlock
    :return: The text block with an accessory layout block.
    :rtype: dict
    """
    return SectionBlock(text=text_object, accessory=accessory).render()


def get_text_block_with_image(text: str, image_url: str, alt_text: str) -> dict:
    """
    Returns a text block with an image to the right of it.

    :param text: The text in the text block.
    :type text: str
    :param image_url: The URL to the image.
    :type image_url: str
    :param alt_text: Alternate text (appears on image hover).
    :type alt_text: str
    :return: The block as a dict.
    :rtype: dict
    """
    text_object = TextObject(btype=TextObject.BTYPE_MARKDOWN, text=text)
    image_element = ImageElement(image_url=image_url, alt_text=alt_text)
    return get_text_block_with_accessory(
        text_object=text_object, accessory=image_element
    )


def get_task_block(text: str, info_link: str, info_text: str) -> list:
    """
    Returns a task block, which is comprised of a paragraph of text followed by an information link at the bottom.

    :param text: Markdown-supported text to display in the paragraph.
    :type text: str
    :param info_link: The link associated with the task block.
    :type info_link: str
    :param info_text: The link text.
    :type info_text: str
    :return: An array of blocks formatted for a block payload.
    :rtype: list
    """
    return [
        TextObject(btype=TextObject.BTYPE_MARKDOWN, text=text).render(),
        get_information_block(info_link=info_link, info_text=info_text),
    ]
