import pytest
import random
import typing

from slack_blockkit.block_element import (
    ButtonElement,
    DangerButtonElement,
    DatepickerElement,
    DefaultButtonElement,
    ImageElement,
    OverflowElement,
    PlainTextInputElement,
    PrimaryButtonElement,
    RadioButtonGroupElement,
)
from slack_blockkit.composition_object import (
    ConfirmObject,
    MarkdownTextObject,
    OptionGroupObject,
    OptionObject,
    PlainTextObject,
    TextObject,
)
from slack_blockkit.layout_block import (
    ActionsBlock,
    ContextBlock,
    DividerBlock,
    FileBlock,
    ImageBlock,
    InputBlock,
    SectionBlock,
)
from slack_blockkit.utils import get_blocks
from slack_blockkit.view_payload import ViewPayload


def _get_options_list() -> typing.List[OptionObject]:
    return [
        OptionObject(text=PlainTextObject(text="Option"), value="Option")
        for _ in range(0, random.randint(3, 5))
    ]


@pytest.fixture
def text_object() -> TextObject:
    return TextObject(
        btype=TextObject.BTYPE_MARKDOWN, text="Sandy cheeks lives in a dome"
    )


@pytest.fixture
def plain_text_object() -> PlainTextObject:
    return PlainTextObject(text="Plain text object")


@pytest.fixture
def markdown_text_object() -> MarkdownTextObject:
    return MarkdownTextObject(text="Markdown text object", emoji=False, verbatim=False)


@pytest.fixture
def confirm_object() -> ConfirmObject:
    return ConfirmObject(
        title=PlainTextObject(text="Confirmation"),
        text=PlainTextObject(text="Confirmation"),
        confirm=PlainTextObject(text="Confirm"),
        deny=PlainTextObject(text="Deny"),
    )


@pytest.fixture
def button_element() -> ButtonElement:
    return ButtonElement(
        text="Login",
        action_id="17a",
        url="https://codededevils.org/cas/login/",
        value="Login",
        confirm=ConfirmObject(
            title=PlainTextObject(text="Confirmation"),
            text=PlainTextObject(text="Confirmation"),
            confirm=PlainTextObject(text="Confirm"),
            deny=PlainTextObject(text="Deny"),
        ),
    )


@pytest.fixture
def datepicker_element() -> DatepickerElement:
    return DatepickerElement(
        action_id="datepicker-vhs-event",
        placeholder=PlainTextObject("Date"),
        confirm=ConfirmObject(
            title=PlainTextObject(text="Confirmation"),
            text=PlainTextObject(text="Confirmation"),
            confirm=PlainTextObject(text="Confirm"),
            deny=PlainTextObject(text="Deny"),
        ),
    )


@pytest.fixture
def image_element() -> ImageElement:
    return ImageElement(
        image_url="https://codedevils.org/static/img/logo.png", alt_text="Logo"
    )


@pytest.fixture
def option_object() -> OptionObject:
    option = str(random.randint(0, 10))
    return OptionObject(
        text=PlainTextObject(text="Option {}".format(option)),
        value=option,
        url="https://codedevils.org/{}".format(option),
    )


@pytest.fixture
def option_group_object() -> OptionGroupObject:
    return OptionGroupObject(
        label=PlainTextObject(text="Option"), options=_get_options_list()
    )


@pytest.fixture
def overflow_element() -> OverflowElement:
    return OverflowElement(action_id="overflow-event-123", options=_get_options_list())


@pytest.fixture
def plaintext_input_element() -> PlainTextInputElement:
    return PlainTextInputElement(
        action_id="input-logo",
        placeholder=PlainTextObject(text="Input"),
        initial_value="Logo",
    )


@pytest.fixture
def radiobutton_group_element() -> RadioButtonGroupElement:
    options = _get_options_list()
    return RadioButtonGroupElement(
        action_id="radiobutton-id", options=options, intitial_option=options[0]
    )


@pytest.fixture
def actions_block() -> ActionsBlock:
    return ActionsBlock(
        elements=[
            RadioButtonGroupElement(
                action_id="action-block",
                options=[
                    OptionObject(
                        PlainTextObject(text="Action block 1"), value="action1"
                    ),
                    OptionObject(
                        PlainTextObject(text="Action block 2"), value="action2"
                    ),
                ],
            ),
            PlainTextInputElement(
                action_id="input1",
                placeholder=PlainTextObject(text="Input"),
                initial_value="Input",
            ),
            OverflowElement(
                action_id="overflow1",
                options=[
                    OptionObject(
                        PlainTextObject(text="Overflow block 1"), value="overflow1"
                    ),
                    OptionObject(
                        PlainTextObject(text="Overflow block 2"), value="overflow2"
                    ),
                ],
            ),
        ]
    )


@pytest.fixture
def context_block() -> ContextBlock:
    return ContextBlock(
        elements=[
            PlainTextInputElement(
                action_id="plaintext1", placeholder=PlainTextObject(text="Context")
            ),
            RadioButtonGroupElement(
                action_id="radiobutton1",
                options=[
                    OptionObject(
                        PlainTextObject(text="Radio button 1"), value="radio1"
                    ),
                    OptionObject(
                        PlainTextObject(text="Radio button 2"), value="radio2"
                    ),
                ],
            ),
        ]
    )


@pytest.fixture
def divider_block() -> DividerBlock:
    return DividerBlock()


@pytest.fixture
def file_block() -> FileBlock:
    return FileBlock(external_id="file0001")


@pytest.fixture
def image_block() -> ImageBlock:
    return ImageBlock(
        image_url="https://codedevils.org/static/img/logo.png",
        alt_text="Logo",
        title=PlainTextObject(text="Logo"),
    )


@pytest.fixture
def input_block() -> InputBlock:
    return InputBlock(
        label=PlainTextObject(text="Input Block"),
        element=ButtonElement(
            text=PlainTextObject(text="Element"), action_id="element1"
        ),
        hint=PlainTextObject(text="This is a hint"),
        optional=True,
    )


@pytest.fixture
def section_block() -> SectionBlock:
    return SectionBlock(
        text=PlainTextObject(text="Section"),
        fields=[
            TextObject(btype=TextObject.BTYPE_MARKDOWN, text="Section part 1"),
            TextObject(btype=TextObject.BTYPE_MARKDOWN, text="section part 2"),
            TextObject(btype=TextObject.BTYPE_MARKDOWN, text="section part 3"),
        ],
        accessory=ImageBlock(
            image_url="https://codedevils.org/static/img/logo.png",
            alt_text="Logo",
            title=PlainTextObject(text="Logo"),
        ),
    )


@pytest.fixture
def view_payload() -> ViewPayload:
    return ViewPayload(
        btype=ViewPayload.BTYPE_HOME,
        title=TextObject(btype=TextObject.BTYPE_PLAINTEXT, text="Home page"),
        blocks=get_blocks(PlainTextObject(text="This block"), DividerBlock()),
        close=TextObject(btype=TextObject.BTYPE_PLAINTEXT, text="Close?"),
    )


@pytest.fixture
def primary_button_element() -> PrimaryButtonElement:
    return PrimaryButtonElement(
        text=PlainTextObject(text="Primary button"),
        action_id="primary-action-1002",
        url="https://codedevils.org/primary",
        value="Primary",
    )


@pytest.fixture
def danger_button_element() -> DangerButtonElement:
    return DangerButtonElement(
        text=PlainTextObject(text="Danger button"),
        action_id="danger-action-1002",
        url="https://codedevils.org/danger",
        value="Danger",
    )


@pytest.fixture
def default_button_element() -> DefaultButtonElement:
    return DefaultButtonElement(
        text=PlainTextObject(text="Default button"),
        action_id="default-action-1002",
        url="https://codedevils.org/default",
        value="Default",
    )
