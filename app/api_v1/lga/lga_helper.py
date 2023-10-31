from .lga_schema import LgaSchema


def deserialize_lga(lga) -> dict:
    return LgaSchema(**lga)
