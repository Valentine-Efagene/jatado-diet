from .country_schema import CountrySchema


def deserialize_country(country) -> dict:
    return CountrySchema(**country)
