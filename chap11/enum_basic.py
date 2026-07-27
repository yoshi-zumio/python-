from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

# Season = Enum('Season', 'SPRING SUMMER AUTUMN WINTER')

def process_season(season: Season):
    print(season)

process_season(Season.SUMMER)
process_season(4)
