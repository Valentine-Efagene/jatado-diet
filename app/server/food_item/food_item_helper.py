from .food_item_schema import FoodItem


def deserialize_food_item(food_item) -> dict:
    return FoodItem(**food_item)
