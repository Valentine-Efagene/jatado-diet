from .country_schema import CountrySchema


def serialize_country(country) -> dict:
    return CountrySchema(**country)
