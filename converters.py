from pydantic.validators import str_validator


def str_to_int(s: str):
    try:
        return int(s)
    except:
        return None


class StrToInt(str):
    @classmethod
    def __get_validators__(cls):
        yield str_validator
        yield str_to_int


def str_to_float(s: str):
    try:
        return float(s)
    except:
        return None


class StrToFloat(str):
    @classmethod
    def __get_validators__(cls):
        yield str_validator
        yield str_to_float
