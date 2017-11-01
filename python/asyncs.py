import asyncio


async def something(i):
    print('started {}'.format(i))

    # await acts like yield from generators
    await asyncio.sleep(3)

    print('finished {}'.format(i))


loop = asyncio.get_event_loop()
for i in range(5):
    asyncio.ensure_future(something(i))
loop.run_forever()

