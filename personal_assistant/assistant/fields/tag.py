import re
from . import Field


class Tag(Field):
    def is_valid(self, value):
        if not 0 < len(value) <= 25:
            raise ValueError("Tag is too long. 25 symbols max")
        if not re.search(
            r"^[a-zA-Z0-9 .,_-]*$",
            value
        ):
            raise ValueError(
                "Incorrect character used. Accepted characters: "
                "capital and small letters, digits, period(.), "
                "hyphen(-), underscore(_), comma(,) and space."
            )
        return True
