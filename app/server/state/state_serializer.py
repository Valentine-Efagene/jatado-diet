from .state_schema import StateSchema


def deserialize_state(state) -> dict:
    return StateSchema(**state)
