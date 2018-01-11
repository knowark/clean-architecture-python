from typing import List


class Project:
    def __init__(self, name: str) -> None:
        self.name = name
        self.uid = ""
        self.stage_ids = []  # type: List[str]
        self.comments = ""
