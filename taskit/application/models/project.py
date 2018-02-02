from typing import List


class Project:
    def __init__(self, name: str, **kwargs) -> None:
        self.name = name
        self.uid = ""
        self.comments = ""
        self.__dict__.update(kwargs)
