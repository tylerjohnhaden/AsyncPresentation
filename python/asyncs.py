import asyncio


async def async_function(i):
    print('started {}'.format(i))

    # await acts like yield from generators
    await asyncio.sleep(3)

    print('finished {}'.format(i))


loop = asyncio.get_event_loop()
for i in range(5):
    asyncio.ensure_future(async_function(i))
loop.run_forever()
