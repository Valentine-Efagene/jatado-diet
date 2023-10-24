from .state_schema import StateSchema


def serialize_state(state) -> dict:
    return StateSchema(**state)
