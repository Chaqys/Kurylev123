import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнование")
    for number in range(1,5):
        await asyncio.sleep(power)
        print(f"Силча {name}, поднял {number} шар")
    print(f"Силач {name} закончил соревнование")
async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 4))
    task_2 = asyncio.create_task(start_strongman('Denis', 8))
    task_3 = asyncio.create_task(start_strongman('Apollon', 10))
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())