from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def __str__(self):
        return f'({self.x}, {self.y})'
