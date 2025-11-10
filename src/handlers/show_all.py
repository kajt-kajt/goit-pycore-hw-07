def show_all(_, contacts: dict[str, str]) -> str:
    """
    Outputs all the contents of in-memory database of contacts.
    """
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)
