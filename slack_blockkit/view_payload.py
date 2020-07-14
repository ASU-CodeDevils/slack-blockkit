from .block import Block
from .composition_object import TextObject


class ViewPayload(Block):
    """
    Defines a view payload. For more information, see: https://api.slack.com/reference/surfaces/views
    """

    BTYPE_MODAL = "modal"
    BTYPE_HOME = "home"

    def __init__(
        self,
        btype: str,
        title: TextObject,
        blocks: list,
        close: TextObject = None,
        submit: TextObject = None,
        private_metadata: str = None,
        callback_id: str = None,
        clear_on_close: bool = False,
        notify_on_close: bool = False,
        external_id: str = None,
    ):

        # type validation
        # type must be either home or modal
        if btype != self.BTYPE_HOME and btype != self.BTYPE_MODAL:
            raise AttributeError(
                f"Invalid btype. Type must be {self.BTYPE_HOME} or {self.BTYPE_MODAL}: {btype}"
            )

        # close must be plain text and 24 characters or less
        if close:
            if not close.is_plain_text():
                raise AttributeError("close must be plain text")
            if close.get_text_length() > 24:
                raise AttributeError(
                    f"close text must be 24 characters or less, but length "
                    f"is {close.get_text_length()}"
                )

        # submit must be plain text, 24 characters or less, and must exist if there is an input block within the blocks
        # array
        if submit:
            if not submit.is_plain_text():
                raise AttributeError("submit must be plain text")
            if submit.get_text_length() > 24:
                raise AttributeError(
                    f"submit text must be 24 characters or less, but length "
                    f"is {submit.get_text_length()}"
                )

        # private_metadata must be 3000 characters or less
        if private_metadata and len(private_metadata) > 3000:
            raise AttributeError(
                f"private_metadata must be 3000 characters or less. Currently {len(private_metadata)}"
            )

        # callbacl_id must be 255 characters or less
        if callback_id and len(callback_id) > 255:
            raise AttributeError(
                f"callback_id must be 3000 characters or less. Currently {len(callback_id)}"
            )

        self.btype = btype
        # titles are used only for modals
        if self.btype == self.BTYPE_MODAL:
            self.title = title
        self.blocks = blocks
        self.close = close
        self.submit = submit
        self.private_metadata = private_metadata
        self.callback_id = callback_id
        self.clear_on_close = clear_on_close
        self.notify_on_close = notify_on_close
        self.external_id = external_id

    def render(self) -> dict:
        # required parameters
        block = {
            "type": self.btype,
            "title": self.title.render(),
            "blocks": self.blocks,
        }

        # optional parameters
        if self.close:
            block.update({"close": self.close.render()})
        if self.submit:
            block.update({"submit": self.submit.render()})
        if self.private_metadata:
            block.update({"private_metadata": self.private_metadata})
        if self.callback_id:
            block.update({"callback_id": self.callback_id})
        if not self.clear_on_close:
            block.update({"clear_on_close": self.clear_on_close})
        if not self.notify_on_close:
            block.update({"notify_on_close": self.notify_on_close})
        if self.external_id:
            block.update({"external_id": self.external_id})

        return block
