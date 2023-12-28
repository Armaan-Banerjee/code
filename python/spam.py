import requests
import asyncio
import time

async def spam():
    url = "http://192.168.1.112:8000/comments/all"
    deltas = []
    for i in range(1000):
        time_before = time.time()
        requests.get(url)
        time_after = time.time()
        deltas.append(time_after - time_before)

    return deltas

async def main():
    results = await asyncio.gather(spam())
    print("max time: ")
    print(max(results[0]))
    print("min time:")
    print(min(results[0]))
    print("average time:")
    print(sum(results[0]) / len(results[0]))

asyncio.run(main())
