import httpx
import time
from datetime import datetime
import asyncio


def multiple_elements():
    return 4, 5, 6, 7


w, x, y, z = multiple_elements()
print(w, x, y, z)
lst = list(multiple_elements())
print(lst)


async def crypto_checker():
    try:
        url = 'https://api.coinranking.com/v1/public/coin/1/history/7d?base=USD'
        request = httpx.get(url)
        # print(json.dumps(request.json()))
        data = dict(request.json())
        print(type(data))
        status = data['status']
        change = data['data']['change']
        history = data['data']['history']
        for item in history:
            # price = data['data']['history'][0]['price']
            price = item['price']
            # Convert the timestamp from milliseconds to seconds then datetime to human readable format
            # timestamp = data['data']['history'][0]['timestamp'] / 1000
            timestamp = item['timestamp'] / 1000
            converted_timestamp = datetime.fromtimestamp(timestamp)
            actual_date = converted_timestamp.date()
            real_time = converted_timestamp.time()
            print(status, change, price, actual_date, real_time)

        return status, change, history

    except Exception as e:
        print(f"error: {e}")


async def main():
    res = asyncio.gather(crypto_checker(), return_exceptions=True)

    return res


if __name__ == '__main__':
    # status, change, price, date, actual_time = asyncio.run(main())
    n = asyncio.run(main())


