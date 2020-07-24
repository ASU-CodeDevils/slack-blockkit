"""
Test block utils.
"""

from slack_blockkit.utils import get_blocks
from slack_blockkit.utils.blocks import (
    get_checkmark,
    get_information_block,
    get_task_block,
    get_text_block_with_accessory,
    get_text_block_with_image,
)
from slack_blockkit.block_element import PrimaryButtonElement
from slack_blockkit.composition_object import MarkdownTextObject, PlainTextObject


def test_get_blocks():
    text1 = PlainTextObject(text="Text 1")
    text2 = PlainTextObject(text="Text 2")
    text3 = PlainTextObject(text="Text 3")
    blocks = get_blocks(text1, text2, text3)
    assert blocks == [text1.render(), text2.render(), text3.render()]


def test_get_checkmark():
    assert get_checkmark(task_completed=True) == ":white_check_mark:"
    assert get_checkmark(task_completed=False) == ":white_large_square:"


def test_get_information_block():
    link = "https://codedevils.org"
    text = "Visit our website"
    info_block = get_information_block(link=link, text=text)
    info_block.pop("block_id")
    comp_block = MarkdownTextObject(
        text=":information_source: *<{}|{}>*".format(link, text)
    ).render()
    comp_block.pop("block_id")
    assert info_block == comp_block


def test_get_text_block_with_accessory(
    plain_text_object: PlainTextObject, primary_button_element: PrimaryButtonElement
):
    text_accessory_block = get_text_block_with_accessory(
        text_object=plain_text_object, accessory=primary_button_element
    )
    assert text_accessory_block == {
        "type": "section",
        "block_id": text_accessory_block["block_id"],
        "text": text_accessory_block["text"],
        "accessory": primary_button_element.render(),
    }


def test_get_text_block_with_image():
    text = "Logo"
    image_url = "https://codedevils.org"
    alt_text = "logo"

    text_with_image = get_text_block_with_image(
        text=text, image_url=image_url, alt_text=alt_text
    )
    assert text_with_image == {
        "type": "section",
        "block_id": text_with_image["block_id"],
        "text": text_with_image["text"],
        "accessory": text_with_image["accessory"],
    }

    # check the accessory is a rendered image block
    accessory = text_with_image["accessory"]
    assert accessory["type"] == "image"
    assert accessory["image_url"] == image_url
    assert accessory["alt_text"] == alt_text


def test_get_task_block():
    text = "Complete this objective"
    info_link = "https://codedevils.org/todo/1"
    info_text = "Complete"
    task_block = get_task_block(text=text, info_link=info_link, info_text=info_text)
    assert task_block == [
        {
            "type": task_block[0]["type"],
            "block_id": task_block[0]["block_id"],
            "text": task_block[0]["text"],
            "emoji": task_block[0]["emoji"],
            "verbatim": task_block[0]["verbatim"]
        },
        {
            "type": task_block[1]["type"],
            "block_id": task_block[1]["block_id"],
            "text": task_block[1]["text"],
            "emoji": task_block[1]["emoji"],
            "verbatim": task_block[1]["verbatim"]
        }
    ]
