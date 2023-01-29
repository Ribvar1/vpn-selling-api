import re

from app.constants import UUID_REGEX


def camel_to_snake(name: str) -> str:
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def is_valid_uuid4(uuid_str: str) -> bool:
    return bool(re.fullmatch(UUID_REGEX, uuid_str))
