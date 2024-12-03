# # 1
# import asyncio

# async def async_example(number: int) -> str:
#     print(type(number))
#     await asyncio.sleep(0.5)
#     return str(number)

# async def main():
#     print("Hello...")
#     await async_example(3)
#     print("...World")

# if __name__ == "__main__":
#     asyncio.run(main(), debug=True)

    
# 2
import asyncio

async def async_example(number: int) -> str:
    print(f"Starting example function {number}")
    await asyncio.sleep(0.5)
    print(f"Ending example function {number}")
    return str(number)

async def main():
    print("Hello...")
    await async_example(3)
    print("...World")

if __name__ == "__main__":
    asyncio.run(main(), debug=True)

    