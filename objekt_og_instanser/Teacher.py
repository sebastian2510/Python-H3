from Base_Person import base_person
class teacher(base_person):
    def __init__(self, name, lastname, courses) -> None:
        super().__init__(name, lastname)
        self.courses = courses
    
    def to_dict(self):
        return self.__dict__
    
    def full_name(self) -> str:
        return f"{self.name} {self.lastname}"
    
    def first_name_prop(self, name):
        self.name = name

    def last_name_prop(self, lastname):
        self.lastname = lastname
    