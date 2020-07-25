import json

from typing import List, Type

from slack_blockkit.block import Block

Blocks = List[dict]


def get_validated_input(
    value,
    ptype: Type,
    min_length: int = None,
    max_length: int = None,
    required: bool = False,
    equality_fields: list = None,
    btype_fields: list = None,
):
    """
    Validates an input using a max length and equality field constraint. If either are not met, then
    this method raises an attribute error.

    Args:
        value: The value of the input.
        ptype (Type): The value's type.
        min_length (int): The min length the input value can be, defaults to None. If None, min length is not
            validated.
        max_length (int): The max length the input value can be, defaults to None. If None, max length is not
            validated.
        required (bool): Whether this param is required.
        equality_fields (list): A list of fields that the input value must be equal to, defaults to None. If not
            specified, the validation is not made.
        btype_fields (list): A list of btype fields that the object must match if it is a Block.
    Raises:
        AttributeError: Raised if any of the above criteria are not met.
    """
    if not value and required:
        raise AttributeError("value {} is required".format(value))

    if value:
        # parameter type
        if not isinstance(value, ptype):
            raise AttributeError("value {} not type {}".format(value, ptype))

        # min/max length
        if min_length or max_length:
            length = value if not isinstance(value, str) else len(value)
            if min_length and length < min_length:
                raise AttributeError(
                    "value {} is less than min length {}".format(value, min_length)
                )
            if max_length and length > max_length:
                raise AttributeError(
                    "value {} exceeds max length {}".format(value, max_length)
                )

        # equality fields
        if equality_fields and value not in equality_fields:
            raise AttributeError(
                "value {} must match one of the fields: {}".format(
                    value, ",".join(equality_fields)
                )
            )

        return value


def get_blocks(*blocks) -> Blocks:
    """
    Takes arguments of `Block` objects and generates a list of blocks ready to be inserted into
    a message payload.

    Args:
        blocks: An argument list of Block objects. Objects will be inserted top to bottom as they
            appear in this list.
    Return:
        A list of the dict representations of block objects.
    Raises:
        AttributeError: If one of more of the blocks is an invalid block format.
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


def test_blocks_online(*blocks):
    """
    Utility that take a set of blocks and opens up the online slack blockkit builder. This will print out a message
    with a URL. Copy the URL into a browser and it will open the Slack Block Builder with the blocks you entered
    as parameters.

    Example:
        >>> from slack_blockkit.layout_block import SectionBlock
        >>> from slack_blockkit.composition_object import PlainTextObject
        >>> from slack_blockkit.utils import test_blocks_online
        >>> ...
        >>> section1 = SectionBlock(text=PlainTextObject(text="Section 1"))
        >>> section2 = SectionBlock(text=PlainTextObject(text="Section 2"))
        >>> test_blocks_online(section1, section2)
    Args:
        blocks: A list of block or dict objects.
    Raises:
        AttributeError: If one of more of the blocks is an invalid block format.
    """
    base_url = "https://app.slack.com/block-kit-builder/#{}"

    block_list = get_blocks(*blocks)
    block_arg = {"blocks": block_list}
    formatted_query = json.dumps(block_arg)

    url = base_url.format(formatted_query)

    print("Copy and paste the following url into your browser:\n\n\t{}\n\n".format(url))
