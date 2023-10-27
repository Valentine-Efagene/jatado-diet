from .macro_nutrient_schema import MacroNutrientSchema


def deserialize_macro_nutrient(macro_nutrient) -> dict:
    return MacroNutrientSchema(**macro_nutrient)
