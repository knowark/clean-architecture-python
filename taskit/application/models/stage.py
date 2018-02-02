class Stage:
    def __init__(self, name: str, **kwargs) -> None:
        self.name = name
        self.uid = ""
        self.closure = False
        self.__dict__.update(kwargs)
