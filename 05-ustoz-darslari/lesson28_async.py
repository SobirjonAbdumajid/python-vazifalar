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

    
# # 2
# import asyncio

# async def async_example(number: int):
#     print(f"Starting example function {number}")
#     await asyncio.sleep(2)
#     print(f"Ending example function {number}")

# async def main():
#     print("Hello...")
#     tasks = [async_example(i) for i in range(1, 6)]
#     await asyncio.gather(*tasks)
#     print("...World")

# if __name__ == "__main__":
#     asyncio.run(main(), debug=True)


# 3
import asyncio
import random

async def prepare_order(name: str, preparing_time:int):
    print(f"we started preparing {name} in {preparing_time}")
    await asyncio.sleep(preparing_time)
    print(f"we finished preparing {name} in {preparing_time}")

async def main():
    print("Started...")
    orders = ["Burger", "lavash", "Hotdog"]
    
    order_list = [prepare_order(order, random.randint(1,10)) for order in orders]
    await asyncio.gather(*order_list)
    print("...Ended")

if __name__ == "__main__":
    asyncio.run(main(), debug=True)