from Teacher import teacher
class TEC:
    
    def __init__(self) -> None:
        self.teachers: list[teacher] = []

    def to_dict(self):
        return {
            'teachers': [t.to_dict() for t in self.teachers]
        }
    
    def find_teacher(self, name: str, lastname: str):
        for teacher in self.teachers:
            if teacher.name == name and teacher.lastname == lastname:
                return teacher
        return None
    def add_teacher(self, teacher: teacher):
        old_teacher = self.find_teacher(teacher.name, teacher.lastname)
        if old_teacher is None:
            self.teachers.append(teacher)
            return
        
        old_teacher.courses = teacher.courses
    
    def remove_teacher(self, teacher: teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)
            return True
        return False
    
    def get_teachers(self):
        return self.teachers
    
