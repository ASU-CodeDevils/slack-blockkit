"""
Test layout blocks.
"""

from slack_blockkit.layout_block import (
    ActionsBlock,
    ContextBlock,
    DividerBlock,
    FileBlock,
    ImageBlock,
    InputBlock,
    SectionBlock,
)


def test_actions_block(actions_block: ActionsBlock):
    rendered = actions_block.render()
    assert rendered == {
        "type": actions_block.btype,
        "block_id": actions_block.block_id,
        "elements": [item.render() for item in actions_block.elements],
    }


def test_context_block(context_block: ContextBlock):
    assert context_block.render() == {
        "type": context_block.btype,
        "block_id": context_block.block_id,
        "elements": [item.render() for item in context_block.elements],
    }


def test_divider_block(divider_block: DividerBlock):
    assert divider_block.render() == {
        "type": divider_block.btype,
        "block_id": divider_block.block_id,
    }


def test_file_block(file_block: FileBlock):
    assert file_block.render() == {
        "type": file_block.btype,
        "block_id": file_block.block_id,
        "external_id": file_block.external_id,
        "source": file_block.source,
    }


def test_image_block(image_block: ImageBlock):
    assert image_block.render() == {
        "type": image_block.btype,
        "block_id": image_block.block_id,
        "image_url": image_block.image_url,
        "alt_text": image_block.alt_text,
        "title": image_block.title.render(),
    }


def test_input_block(input_block: InputBlock):
    assert input_block.render() == {
        "type": input_block.btype,
        "block_id": input_block.block_id,
        "label": input_block.label.render(),
        "element": input_block.element.render(),
        "hint": input_block.hint.render(),
        "optional": input_block.optional,
    }


def test_section_block(section_block: SectionBlock):
    assert section_block.render() == {
        "type": section_block.btype,
        "block_id": section_block.block_id,
        "text": section_block.text.render(),
        "fields": [item.render() for item in section_block.fields],
        "accessory": section_block.accessory.render(),
    }
