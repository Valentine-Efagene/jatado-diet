from .macro_nutrient_schema import MacroNutrient


def deserialize_macro_nutrient(macro_nutrient) -> dict:
    return MacroNutrient(**macro_nutrient)
