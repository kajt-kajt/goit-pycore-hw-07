from src.handlers.input_error import input_error

@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Adds new entry to contacts dictionary. 
    Returns a warning if contact with such name already exists, but anyway rewrites it.
    "args" should contain 2 values.
    """
    warning = ""
    name, phone = args
    if name in contacts:
        warning = f"WARNING: rewriting existing contact '{name}'=>'{contacts[name]}'!\n"
    contacts[name] = phone
    return warning + "Contact added."
