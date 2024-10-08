class calculator:

    def __init__(self, vector):
        self.vector = vector


    def __add__(self, object) -> None:
        self.vector = [x + object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]


    def __mul__(self, object) -> None:
        self.vector = [x * object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]


    def __sub__(self, object) -> None:
        self.vector = [x - object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]


    def __truediv__(self, object) -> None:
        if object == 0:
            raise ZeroDivisionError("Cant devide by 0")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]
