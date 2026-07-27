class Top:
    def hoge(self) -> None:
        print('Top')

class MiddleA(Top):
    def hoge(self) -> None:
        print('MiddleA')

class MiddleB:
    def hoge(self) -> None:
        print('MiddleB')

class Low(MiddleA, MiddleB):
    pass

if __name__ == '__main__':
    lo = Low()
    lo.hoge()
    print(Low.mro())
