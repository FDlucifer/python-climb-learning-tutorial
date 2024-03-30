import asyncio

async def main():
    print("A")
    await other_function()
    print("B")

async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")

asyncio.run(main())