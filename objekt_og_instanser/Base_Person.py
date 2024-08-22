from abc import ABC, abstractmethod
class Ibase_person(ABC):

    @property
    @abstractmethod
    def first_name_prop(self, name):
        pass

    @property
    @abstractmethod
    def last_name_prop(self, lastname):
        pass

    @abstractmethod
    def full_name(self) -> str:
        pass


class base_person(Ibase_person):
    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname
    
    def full_name(self) -> str:
        return f"{self.name} {self.lastname}"
    

    def first_name_prop(self, name):
        return self.name
