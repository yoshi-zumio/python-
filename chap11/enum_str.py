# from enum import Enum

# class Command(Enum):
#     ATTACK = 'attack'
#     MAGIC = 'magic'
#     DEFEND = 'defend'
#     ESCAPE = 'escape'

from enum import StrEnum, auto

class Command(StrEnum):
    ATTACK = auto()
    MAGIC = auto()
    DEFEND = auto()
    ESCAPE = auto()

comm = input('次の行動を入力してください：')

match comm:
    case Command.ATTACK:
        print('攻撃します')
    case Command.MAGIC:
        print('魔法を使います')
    case Command.DEFEND:
        print('防御します')
    case Command.ESCAPE:
        print('逃げます')
    case _:
        print('無効な行動です')
