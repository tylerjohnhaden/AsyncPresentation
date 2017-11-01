import aiohttp
import asyncio


async def guesses():
    for i in range(1 + (2 ** 21)):
        yield i


async def attempt(client, guess):
    async with client.get('http://localhost:7777/{0}'.format(guess)) as resp:
        print('guessing .. {0}'.format(guess))
        return await resp.text()


async def main():
    async with aiohttp.ClientSession() as client:
        async for i in guesses():
            # runs successively without blocking
            data = await attempt(client, guess=i)
            if 'success' in data:
                print(data)
                return


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

