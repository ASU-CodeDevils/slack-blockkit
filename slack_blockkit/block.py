class RenderMixin:
    """Provides a render method for blocks and similar payload structures."""

    def render(self) -> dict:
        """
        Renders the block in a ``dict`` format appropriate for using within message payloads.

        Returns:
            dict: The block as a dict.
        """
        # extract the values and their keys who are not None
        vars_dict = {
            key: value for key, value in vars(self).items() if value is not None
        }

        # type is a reserved keyword, so here we change the name of btype to type
        if "btype" in vars_dict:
            vars_dict["type"] = vars_dict.pop("btype")

        # iterate through dict and render blocks
        for key, value in vars_dict.items():

            # render individual blocks
            if isinstance(value, Block):
                vars_dict[key] = value.render()

            # loop through list and render all blocks
            elif isinstance(value, list):
                updated = []
                for item in value:
                    if isinstance(item, Block):
                        item = item.render()
                    updated.append(item)
                vars_dict[key] = updated

            # render all values in dict using dict comprehension if the value is a Block
            elif isinstance(value, dict):
                rendered_items = {
                    key: pair.render()
                    for key, pair in value.items()
                    if isinstance(pair, Block)
                }
                if rendered_items:
                    value.update(rendered_items)
                vars_dict[key] = value

        return vars_dict


class Block(RenderMixin):
    """
    Base block class.

    Args:
        btype (str): Synonymous with Slack's ``type`` parameter.
    """

    def __init__(self, btype: str):
        self.btype = btype

    @staticmethod
    def validate_input(
        input_name: str, input_value, max_length: int = 0, equality_fields: list = None
    ):

        if input_value and isinstance(input, str):
            # if max length is specified, check that the value does not exceed the length
            if max_length != 0 and len(input_value) > max_length:
                raise AttributeError(
                    f"{input_name} cannot be greater than {max_length} characters, "
                    f"but it {len(input_value)}"
                )

            # if equality fields are specified, check that the string equals one of those fields
            if equality_fields and input_value not in equality_fields:
                raise AttributeError(
                    f"{input_name} needs to be one of the following values: "
                    f'{",".join(equality_fields)}'
                )
