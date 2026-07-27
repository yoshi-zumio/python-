import asyncio
from coro import heavy

result = asyncio.run(heavy('hoge', 2))

# イベントループの場合
# loop = asyncio.new_event_loop()
# result = loop.run_until_complete(
#     heavy('hoge', 2))

print(result)
