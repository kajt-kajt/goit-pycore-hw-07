from src.handlers.input_error import input_error
from src.entities import AddressBook

@input_error
def change_contact(args: list[str], contacts: AddressBook) -> str:
    """
    Rewrites record for existing name.
    Returns an error message if contact with given name does not exist.
    "args" should contain 2 values.
    """
    name, phone = args
    if name not in contacts:
        return f"ERROR: contact '{name}' does not exist!"
    contacts[name] = phone
    return "Contact updated."
