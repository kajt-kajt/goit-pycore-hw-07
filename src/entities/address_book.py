from collections import UserDict
from src.entities import Record

class AddressBook(UserDict):
    """
    Class for address book entity, extends dict, so has its main object in data field.
    Key for the dictionary would be name as str for easier search.
    """
    def add_record(self, record: Record):
        """
        Add record to address book. If such name already exists, record will be rewritten.
        """
        if not isinstance(record, Record):
            error_msg = f"Expecting object of type Record, but got {type(record).__name__} instead."
            raise ValueError(error_msg)
        self.data[str(record.name)] = record

    def find(self, name: str) -> Record:
        """
        Get record by name. Return None if record with such name does not exist.
        """
        return self.data.get(name)

    def delete(self, name:str) -> Record:
        """
        Delete record from address book by name and return it back. 
        Return None if record was not found.
        """
        return self.data.pop(name, None)
