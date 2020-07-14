from abc import ABC


class Block(ABC):
    def render(self) -> dict:
        """
        Renders a block as a dict. The formatting is used to insert into a message payload.

        :return: The block as a dict.
        :rtype: dict
        """
        pass

    @staticmethod
    def validate_input(
        input_name: str, input_value, max_length: int = 0, equality_fields: list = None
    ):
        """
        Validates an input using a max length and equality field constraint. If either are not met, then
        this method raises an attribute error.

        :param input_name: The name of the input field. Used to display with the attribute error message.
        :type input_name: str
        :param input_value: The value of the input.
        :param max_length: The max length the input value can be, defaults to 0. If 0, max length is not validated.
        :type max_length: int
        :param equality_fields: A list of fields that the input value must be equal to, defaults to None. If not
            specified, the validation is not made.
        :type equality_fields: list
        :return: None
        :except AttributeError: Raised if the criteria is not met.
        """

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

    def __dict__(self):
        return self.render()

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)
