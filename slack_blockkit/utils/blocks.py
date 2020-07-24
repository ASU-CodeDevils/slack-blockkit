from slack_blockkit.block_element import BlockElement, ImageElement
from slack_blockkit.composition_object import MarkdownTextObject, TextObject
from slack_blockkit.layout_block import SectionBlock


def get_checkmark(task_completed: bool) -> str:
    """
    Returns a check mark emoji indicating the completed task status. If the task is complete, then a white check
    mark is returned. If not, an empty white square is.

    :param task_completed: Whether or not the task was complete.
    :type task_completed: bool
    :return: A checkmark emoji string based on whether or not the task was completed.
    :rtype: str
    """
    return ":white_check_mark:" if task_completed else ":white_large_square:"


def get_information_block(link: str, text: str) -> dict:
    """
    Returns an information block, which is a section with an info icon followed by linked text.

    :param link: The link the block redirects the user to.
    :type link: str
    :param text: The link text.
    :type text: str
    :return: A dict in the format of a context block.
    :rtype: dict
    """
    information = ":information_source: *<{link}|{text}>*".format(link=link, text=text)
    return MarkdownTextObject(text=information).render()


def get_text_block_with_accessory(
    text_object: TextObject, accessory: BlockElement
) -> dict:
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
    text_object = MarkdownTextObject(text=text)
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
        MarkdownTextObject(text=text).render(),
        get_information_block(link=info_link, text=info_text),
    ]
