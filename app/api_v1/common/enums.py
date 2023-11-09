from enum import Enum


class Tag(str, Enum):
    MISC = 'Miscellaneous'
    AUTHENTICATION = 'Authentication'
    USER = 'Users'
    COUNTRY = 'Countries'
    STATE = 'States'
    LGA = 'LGAs'
    RECIPE_UNIT_SCHEME = 'Recipe Unit Scheme'
    ACTION = 'Actions'
    ETHNICITY = 'Ethnicity'
    LANGUAGE = 'Language'
    NUTRIENT = 'Nutrients'
    FOOD_ITEM = 'Food Item'


class Environment(str, Enum):
    TEST = 'test'
    DEVELOPMENT = 'development'
    PRODUCTION = 'production'
