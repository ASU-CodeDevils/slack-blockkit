from slack_blockkit.block_element import BlockElement, ImageElement
from slack_blockkit.composition_object import MarkdownTextObject, TextObject
from slack_blockkit.layout_block import SectionBlock


def get_checkmark(task_completed: bool) -> str:
    """
    Returns a check mark emoji indicating the completed task status. If the task is complete, then a white check
    mark is returned. If not, an empty white square is.

    Args:
        task_completed (bool): Whether or not the task was complete.
    Returns:
        str: A checkmark emoji string based on whether or not the task was completed.
    """
    return ":white_check_mark:" if task_completed else ":white_large_square:"


def get_information_block(link: str, text: str) -> dict:
    """
    Returns an information block, which is a section with an info icon followed by linked text.

    Args:
        link (str): The link the block redirects the user to.
        text (str): The link text.
    Returns:
        dict: A dict in the format of a context block.
    """
    information = ":information_source: *<{link}|{text}>*".format(link=link, text=text)
    return MarkdownTextObject(text=information).render()


def get_text_block_with_accessory(text_object: TextObject, accessory: BlockElement) -> dict:
    """
    Returns a text block with an accessory.

    Args:
        text_object (TextObject): The text block object.
        accessory (LayoutBlock): The accessory object.
    Returns:
        dict: The text block with an accessory layout block.
    """
    return SectionBlock(text=text_object, accessory=accessory).render()


def get_text_block_with_image(text: str, image_url: str, alt_text: str) -> dict:
    """
    Returns a text block with an image to the right of it.

    Args:
        text (str): The text in the text block.
        image_url (str): The URL to the image.
        alt_text (str): Alternate text (appears on image hover).
    Returns:
        dict: The block as a dict.
    """
    text_object = MarkdownTextObject(text=text)
    image_element = ImageElement(image_url=image_url, alt_text=alt_text)
    return get_text_block_with_accessory(
        text_object=text_object, accessory=image_element
    )


def get_task_block(text: str, info_link: str, info_text: str) -> list:
    """
    Returns a task block, which is comprised of a paragraph of text followed by an information link at the bottom.

    Args:
        text (str): Markdown-supported text to display in the paragraph.
        info_link (str): The link associated with the task block.
        info_text (str): The link text.
    Returns:
        list: An array of blocks formatted for a block payload.
    """
    return [
        MarkdownTextObject(text=text).render(),
        get_information_block(link=info_link, text=info_text),
    ]
