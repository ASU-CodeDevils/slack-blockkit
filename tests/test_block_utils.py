"""
Test block utils.
"""

from slack_blockkit.utils.blocks import get_blocks

from slack_blockkit.composition_object import PlainTextObject


def test_get_blocks():
    text1 = PlainTextObject(text="Text 1")
    text2 = PlainTextObject(text="Text 2")
    text3 = PlainTextObject(text="Text 3")
    blocks = get_blocks(text1, text2, text3)
    assert blocks == [
        text1.render(),
        text2.render(),
        text3.render()
    ]
