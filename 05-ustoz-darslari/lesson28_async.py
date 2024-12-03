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


# # 3
# import asyncio
# import random

# async def prepare_order(name: str, preparing_time:int):
#     print(f"we started preparing {name} in {preparing_time}")
#     await asyncio.sleep(preparing_time)
#     print(f"we finished preparing {name} in {preparing_time}")

# async def main():
#     print("Started...")
#     orders = ["Burger", "Lavash", "Hotdog", "Osh"]
    
#     order_list = [prepare_order(order, random.randint(1,10)) for order in orders]
#     await asyncio.gather(*order_list)
#     print("...Ended")

# if __name__ == "__main__":
#     asyncio.run(main(), debug=True)


# # 4
# import asyncio

# async def fetch_data(name:str, delay: int):
#     print(f"Fetiching {name} in {delay}")
#     await asyncio.sleep(delay)
#     print(f"Finished {name} in {delay}")

# async def process_data(data:dict) -> None:
#     print("Started...")
#     keys = list(data.keys())
#     values = list(data.values())
#     data_of = [fetch_data(keys[i], values[i]) for i in range(len(data))]
#     await asyncio.gather(*data_of)
#     print("...Ended")


# apis = {
#     "Review Api": 2,
#     "User Api": 5,
#     "Product Api": 4,
#     "Owner Api": 3,
#     "Orders Api": 6
# }

# if __name__ == "__main__":
#     asyncio.run(process_data(apis), debug=True)
    
    
# 5
import asyncio

async def fetch_data(name:str, delay: int):
    print(f"Fetiching {name} in {delay}")
    await asyncio.sleep(delay)
    print(f"Finished {name} in {delay}")

async def process_data(data:dict) -> None:
    print(f"Started...{data}")
    for k, v in data.items():
        apis[k] = v
        await asyncio.sleep(2)
        
    print(f"...Ended {apis}")


async def main():
    new_apis = {
        "Review Api": 2,
        "User Api": 5,
        "Product Api": 4
    }
    
    process_task = process_data(new_apis)
    fetch_tasks = [fetch_data(name, delay) for name, delay in apis.items()]
    
    await asyncio.gather(process_task, *fetch_tasks)    

apis = {
    "Review Api": 2,
    "User Api": 5,
    "Product Api": 4,
    "Owner Api": 3,
    "Orders Api": 6
}

if __name__ == "__main__":
    asyncio.run(process_data(apis), debug=True)