from enum import Enum


class Tag(str, Enum):
    MISC = 'Miscellaneous'
    AUTHENTICATION = 'Authentication'
    USER = 'Users'
    COUNTRY = 'Countries'
    STATE = 'States'
    LGA = 'LGAs'
    ETHNICITY = 'Ethnicity'
    LANGUAGE = 'Language'
    MACRO_NUTRIENT = 'Macro Nutrients'
    MICRO_NUTRIENT = 'Micro Nutrients'
    FOOD_ITEM = 'Food Item'


class Environment(str, Enum):
    TEST = 'test'
    DEVELOPMENT = 'development'
    PRODUCTION = 'production'
