import json
import os
from Company import TEC
from Teacher import teacher
class FileClass:
    filename: str = "firm.json"

    @staticmethod
    def read_file():
        if not os.path.exists(FileClass.filename):
            with open(FileClass.filename, "w") as file:
                json.dump(TEC().to_dict(), file, indent=4)
            return TEC()
        with open(FileClass.filename, "r") as file:
            content = file.read().strip()
            if not content:
                return TEC()
            if content == "{}":
                return TEC()
            # Return as TEC object
            firm = TEC()
            data = json.loads(content)
            for t in data['teachers']:
                teacher_obj = teacher(t['name'], t['lastname'], t['courses'])
                firm.add_teacher(teacher_obj)
            return firm
        
    @staticmethod
    def write_file(data: TEC):
        try:
            with open(FileClass.filename, "w") as file:
                json.dump(data.to_dict(), file, indent=4)
        except Exception as e:
            print(f"Fejl: {e}")
            os.abort()


