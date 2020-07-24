"""
Tests block elements.
"""
from slack_blockkit.block_element import (
    DatepickerElement,
    ImageElement,
    OverflowElement,
    PlainTextInputElement,
    PrimaryButtonElement,
    RadioButtonGroupElement,
)


def test_primary_button_element(primary_button_element: PrimaryButtonElement):
    rendered = primary_button_element.render()
    assert rendered == {
        "type": primary_button_element.btype,
        "style": primary_button_element.style,
        "text": primary_button_element.text.render(),
        "url": primary_button_element.url,
        "action_id": primary_button_element.action_id,
        "value": primary_button_element.value,
        "block_id": primary_button_element.block_id,
    }


def test_default_button_element(default_button_element: PrimaryButtonElement):
    rendered = default_button_element.render()
    assert rendered == {
        "type": default_button_element.btype,
        "style": default_button_element.style,
        "text": default_button_element.text.render(),
        "url": default_button_element.url,
        "action_id": default_button_element.action_id,
        "value": default_button_element.value,
        "block_id": default_button_element.block_id,
    }


def test_danger_button_element(danger_button_element: PrimaryButtonElement):
    rendered = danger_button_element.render()
    assert rendered == {
        "type": danger_button_element.btype,
        "style": danger_button_element.style,
        "text": danger_button_element.text.render(),
        "url": danger_button_element.url,
        "action_id": danger_button_element.action_id,
        "value": danger_button_element.value,
        "block_id": danger_button_element.block_id,
    }


def test_datepicker_element(datepicker_element: DatepickerElement):
    rendered = datepicker_element.render()
    assert rendered == {
        "type": datepicker_element.btype,
        "block_id": datepicker_element.block_id,
        "action_id": datepicker_element.action_id,
        "placeholder": datepicker_element.placeholder.render(),
        "initial_date": datepicker_element.initial_date,
        "confirm": datepicker_element.confirm.render(),
    }


def test_overflow_element(overflow_element: OverflowElement):
    rendered = overflow_element.render()
    options_rendered = [item.render() for item in overflow_element.options]
    assert rendered == {
        "type": overflow_element.btype,
        "block_id": overflow_element.block_id,
        "action_id": overflow_element.action_id,
        "options": options_rendered,
    }


def test_image_element(image_element: ImageElement):
    rendered = image_element.render()
    assert rendered == {
        "type": image_element.btype,
        "block_id": image_element.block_id,
        "image_url": image_element.image_url,
        "alt_text": image_element.alt_text,
    }


def test_plaintext_input_element(plaintext_input_element: PlainTextInputElement):
    rendered = plaintext_input_element.render()
    assert rendered == {
        "type": plaintext_input_element.btype,
        "block_id": plaintext_input_element.block_id,
        "action_id": plaintext_input_element.action_id,
        "initial_value": plaintext_input_element.initial_value,
        "max_length": plaintext_input_element.max_length,
        "min_length": plaintext_input_element.min_length,
        "multiline": plaintext_input_element.multiline,
        "placeholder": plaintext_input_element.placeholder.render(),
    }


def test_radiobutton_group_element(radiobutton_group_element: RadioButtonGroupElement):
    rendered = radiobutton_group_element.render()
    options_rendered = [item.render() for item in radiobutton_group_element.options]
    assert rendered == {
        "type": radiobutton_group_element.btype,
        "block_id": radiobutton_group_element.block_id,
        "action_id": radiobutton_group_element.action_id,
        "options": options_rendered,
        "initial_option": radiobutton_group_element.initial_option.render(),
    }
