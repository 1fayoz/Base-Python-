# asynxrom

# import asyncio
# import time

# async def async_task(number):
#     print(f"this is tack number: {number} start")
#     time.sleep(2)
#     print(f"this is tack number: {number}  finish")

# async def main():
#     start_time = time.time()
#     asyncio.gather(async_task(1), async_task(2))
#     end_time = time.time()
#     print(f"total time{end_time - start_time}")

# asyncio.run(main())

# uyga vazifa shunga oxsha narsa qib kelish 


# import asyncio
# import time

# async def asynk(num):
#     print (f"this is number{num} start")
#     await asyncio.sleep(2)
#     print (f"this is number{num} finish")

# async def en():
#     start_time = time.time()
#     asyncio.gather(asynk(1), asynk(2))
#     end_time = time.time()
#     print( end_time - start_time)

# asyncio.run(en())


# ls 

import asyncio

async def example(name, delay):
    print(f"Hello, {name}! This is an asynchronous function.")
    await asyncio.sleep(delay)
    print(f"{name}, the asynchronous function has completed after {delay} seconds.")

async def main():
    task1 = example("Task 1", 3)
    task2 = example("Task 2", 2)

    await asyncio.gather(task1, task2)

asyncio.run(main())

















































































































































# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import ParseMode
# from aiogram import executor

# API_TOKEN = "6911292891:AAGmZQmNCcnuMrOkvyOPzLUynXAHpXfxuGs"  # Bu joyga o'z botingizning API tokenini yozing

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)


# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     welcome_message = "Salom! Men harf va sonlarni hisoblovchi botman. Xabar yuboring, va men harf va sonlarni hisoblab qaytaraman!"
#     await message.answer(welcome_message)


# @dp.message_handler(func=lambda message: True)
# async def count_letters_and_digits(message: types.Message):
#     """
#     This handler will be called for any other messages
#     """
#     text = message.text
#     letter_count = sum(c.isalpha() for c in text)
#     digit_count = sum(c.isdigit() for c in text)

#     result_message = f"Xabarda {letter_count} ta harf va {digit_count} ta son bor."
#     await message.reply(result_message, parse_mode=ParseMode.MARKDOWN)


# if __name__ == '__main__':
#     from aiogram import executor

#     executor.start_polling(dp, skip_updates=True)









































































































































































































































