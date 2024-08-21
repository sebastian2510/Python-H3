from Base_Person import base_person
class teacher(base_person):
    def __init__(self, name, lastname, courses) -> None:
        super().__init__(name, lastname)
        self.courses = courses
    
    def to_dict(self):
        return self.__dict__
    