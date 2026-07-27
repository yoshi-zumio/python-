rank = '甲'

match rank:
    case '甲':
        print('大変よいです。')
    case '乙':
        print('よいです。')
    case '丙':
        print('がんばりましょう。')
    case _:
        print('？？？')
