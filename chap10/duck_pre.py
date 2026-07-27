from abc import abstractmethod, ABC

class Figure(ABC):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @abstractmethod
    def get_area(self) -> float:
        pass

class Triangle(Figure):
    def get_area(self) -> float:
        return self.width * self.height / 2

class Rectangle(Figure):
    def get_area(self) -> float:
        return self.width * self.height

class Japan:
    def get_area(self) -> float:
        return 378000

def show_area(figure: Figure) -> None:
    print(f'{figure.__class__.__name__}の面積は{figure.get_area()}です。')

if __name__ == '__main__':
    show_area(Triangle(10, 15))
    show_area(Rectangle(10, 15))
    show_area(Japan())
