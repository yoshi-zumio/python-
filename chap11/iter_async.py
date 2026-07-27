import asyncio
from typing import AsyncIterator
from aiohttp import ClientSession

class MyAsyncClazz:
    def __init__(self, data: list[str]) -> None:
        self.data = data  # URLのリスト
        self.__current = 0

    # 非同期イテレーター（自分自身を返す）
    def __aiter__(self) -> AsyncIterator[str]:
        return self

    # 非同期イテレーターの本体を実装
    async def __anext__(self) -> str:
        # 配列末尾でイテレーターを終了
        if self.__current == len(self.data):
            raise StopAsyncIteration
        print(f'Fetching: {self.data[self.__current]}')
        # URLリストの先頭から順にアクセス
        async with ClientSession() as session:
            async with session.get(self.data[self.__current]) as response:
                self.__current += 1
                return await response.text()


async def main() -> None:
    # 非同期イテレーターによるループ（async for）
    async for data in MyAsyncClazz([
        'https://codezine.jp',
        'https://wings.msn.to',
        'https://www.web-deli.com',
    ]):
        print(data[:1000])

asyncio.run(main())
