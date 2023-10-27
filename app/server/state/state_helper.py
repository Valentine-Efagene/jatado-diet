from .state_schema import StateSchema


def deserialize_state(state) -> dict:
    # return None if state == None else StateSchema(**state)
    return StateSchema(**state)
