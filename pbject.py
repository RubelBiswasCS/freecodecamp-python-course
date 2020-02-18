
class Student:
    def __init__(self, name, iid, cgpa):
        self.name=name
        self.iid=iid
        self.cgpa=cgpa

    def on_limit(self):
        if self.cgpa >= 3.5:
            return True
        else :
            return False

