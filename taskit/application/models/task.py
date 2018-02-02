from datetime import datetime


class Task:
    def __init__(self, name: str, **kwargs) -> None:
        self.name = name
        self.uid = ""
        self.due_date = datetime.now()
        self.priority = 1
        self.project_id = ""
        self.stage = ""
        self.comments = ""
        self.__dict__.update(kwargs)
