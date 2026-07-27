import asyncio
import random


async def heavy(name: str, sec: int) -> str:
    print(f'{name} start...')
    await asyncio.sleep(sec)
    # if random.randint(0, 1) == 0:
    #     raise ValueError(f'{name} occurs error.')
    print(f'{name} end...')
    return f'{name}: {sec} sec'
