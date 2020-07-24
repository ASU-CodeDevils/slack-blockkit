"""
Test composition objects.
"""

from slack_blockkit.composition_object import (
    PlainTextObject,
    MarkdownTextObject,
    ConfirmObject,
    OptionGroupObject,
    OptionObject,
    TextObject,
)


def test_plain_text_object(plain_text_object: PlainTextObject):
    assert plain_text_object.render() == {
        "type": TextObject.BTYPE_PLAINTEXT,
        "block_id": plain_text_object.block_id,
        "text": plain_text_object.text,
    }


def test_markdown_text_object(markdown_text_object: MarkdownTextObject):
    assert markdown_text_object.render() == {
        "type": markdown_text_object.btype,
        "block_id": markdown_text_object.block_id,
        "text": markdown_text_object.text,
        "emoji": markdown_text_object.emoji,
        "verbatim": markdown_text_object.verbatim,
    }


def test_confirm_object(confirm_object: ConfirmObject):
    assert confirm_object.render() == {
        "block_id": confirm_object.block_id,
        "title": confirm_object.title.render(),
        "text": confirm_object.text.render(),
        "confirm": confirm_object.confirm.render(),
        "deny": confirm_object.deny.render(),
    }


def test_option_object(option_object: OptionObject):
    assert option_object.render() == {
        "block_id": option_object.block_id,
        "text": option_object.text.render(),
        "value": option_object.value,
        "url": option_object.url,
    }


def test_option_group_object(option_group_object: OptionGroupObject):
    assert option_group_object.render() == {
        "label": option_group_object.label.render(),
        "options": [item.render() for item in option_group_object.options],
    }
