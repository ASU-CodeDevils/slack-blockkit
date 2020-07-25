__version__ = "0.0.5"
__version_info__ = tuple(
    [
        int(num) if num.isdigit() else num
        for num in __version__.replace("-", ".", 1).split(".")
    ]
)

from slack_blockkit.block import Block  # noqa F401
