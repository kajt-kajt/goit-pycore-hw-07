from src.entities import Name, Phone

class Record:
    """
    Class representing a single record in address book with name and a list of phone numbers.
    """
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"{self.name}: {'; '.join(str(p) for p in self.phones)}"

    def __repr__(self):
        return f"Record({str(self)})"

    def add_phone(self, phone: str):
        """
        Add phone number to list for this record
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """
        Remove phone number from list for this record
        """
        self.phones = [phone_record for phone_record in self.phones if str(phone_record) != phone]

    def edit_phone(self, old_phone: str, new_phone: str):
        """
        Find phone number record in the list and update it with new value
        """
        for phone_record in self.phones:
            if str(phone_record) == old_phone:
                phone_record.update(new_phone)

    def find_phone(self, phone: str) -> Phone:
        """
        Find phone number in the list
        """
        result = None
        for phone_record in self.phones:
            if str(phone_record) == phone:
                result = phone_record
                break
        return result

    def get_phones(self) -> str:
        """
        Output all phone numbers in record
        """
        return '; '.join(str(p) for p in self.phones)
