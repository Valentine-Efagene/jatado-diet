from .nutrient_schema import NutrientSchema


def deserialize_nutrient(nutrient) -> dict:
    # return None if nutrient == None else NutrientSchema(**nutrient)
    return NutrientSchema(**nutrient)
