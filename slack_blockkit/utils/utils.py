from typing import List, Type

from slack_blockkit.block import Block

Blocks = List[dict]


def get_validated_input(value, ptype: Type, min_length: int = None, max_length: int = None, required: bool = False,
        equality_fields: list = None, btype_fields: list = None):
    """
    Validates an input using a max length and equality field constraint. If either are not met, then
    this method raises an attribute error.

        :param value: The value of the input.
        :param ptype: The type the ``value`` is expected to be.
        :param min_length: The min length the input value can be, defaults to None. If None, min length is not
            validated.
        :type min_length: int
        :param max_length: The max length the input value can be, defaults to None. If None, max length is not
            validated.
        :type max_length: int
        :param required: Whether this param is required.
        :type required: bool.
        :param equality_fields: A list of fields that the input value must be equal to, defaults to None. If not
            specified, the validation is not made.
        :type equality_fields: list
        :param btype_fields: A list of btype fields that the object must match if it is a Block.
        :type btype_fields: list
        :return: The value.
        :except AttributeError: Raised if the criteria is not met.
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
                raise AttributeError("value {} is less than min length {}".format(value, min_length))
            if max_length and length > max_length:
                raise AttributeError("value {} exceeds max length {}".format(value, max_length))
        
        # equality fields
        if equality_fields and value not in equality_fields:
            raise AttributeError("value {} must match one of the fields: {}".format(value, ",".join(equality_fields)))

        return value


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
