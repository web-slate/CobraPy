import asyncio
from math_operations import add

async def perform_addition(a, b):
    result = add(a, b)
    print(f"Addition Result: {result}")

async def main():
    tasks = [perform_addition(i, i+1) for i in range(10)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
