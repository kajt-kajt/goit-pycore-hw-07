from src.handlers.input_error import input_error

@input_error
def show_phone(args: list[str], contacts: dict[str: str]) -> str:
    """
    Returns phone for given name.
    Returns an error message if contact with such name is absent.
    """
    name = args[0]
    return contacts[name]
