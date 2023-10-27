from .micro_nutrient_schema import MicroNutrientSchema


def deserialize_micro_nutrient(micro_nutrient) -> dict:
    # return None if micro_nutrient == None else MicroNutrientSchema(**micro_nutrient)
    return MicroNutrientSchema(**micro_nutrient)
