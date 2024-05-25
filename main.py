from aiogram import Bot, Router, Dispatcher,types
import asyncio
import logging
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import logging

bot = Bot(token="7185736961:AAF-Z_oHfB3KZZ6GcoCai9elJDp1m9Ygv0U")
form_router = Router()
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

def reply_button():
    buttons = [
        [KeyboardButton(text="O'quv kurslar"), 
        KeyboardButton(text="Bizning afzalliklarimiz"), 
        KeyboardButton(text="kurs qo'shish")],

    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)



def reyly_buttons():
    buttons = [
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


class add_course(StatesGroup):
    name = State()
    price = State()
    full_info = State()
    teacher_info = State()













@form_router.message(Command('start'))
async def start_button(message: Message):
    print(message.chat.id)
    await message.answer(text="Assalomu alaykum", reply_markup=reply_button())




@form_router.message(F.text == "Bizning afzalliklarimiz")
async def info(message: Message, state: FSMContext):
    await message.answer(text="""
                BIZNING AFZALLIKLARIMIZ
        >> har oylik muntazam testlar 👍🏻
        >> kuchli o'quvchilarni ish bilan taminlash 💸
        >> va boshqalar
    """)
    state.clear()

@form_router.message(F.text == "kurs qo'shish")
async def name(message: Message, state: FSMContext):
    await message.answer(text="Kurs nomi")
    await state.set_state(add_course.name)

@form_router.message(add_course.name)
async def set_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text="Kurs narxi")
    await state.set_state(add_course.price)

@form_router.message(add_course.price)
async def set_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer(text="To'liq malumot")
    await state.set_state(add_course.full_info)

@form_router.message(add_course.full_info)
async def info_price(message: Message, state: FSMContext):
    await state.update_data(full_info=message.text)
    await message.answer(text="Kurs o'qituvchisi haqida malumot")
    await state.set_state(add_course.teacher_info)




@form_router.message(add_course.teacher_info, F.text == "Ha")
async def yes_button(message: Message, state: FSMContext):
    data = await state.get_data()
    text = f"""
    Kurs nomi: {data['name']}
    Kurs narxi: {data['price']}
    To'liq malumot: {data['full_info']}
    Kurs o'qituvchisi haqida malumot: {data['teacher_info']}
    """

    await bot.send_message(chat_id=5593831038, text=text)
    await state.clear()

@form_router.message(add_course.teacher_info, F.text == "Yo'q")
async def send_message(message: types.Message, state: FSMContext):
    await message.answer("malumot yuborilmadi")
    await state.clear() 




@form_router.message(add_course.teacher_info)
async def info_price(message: Message, state: FSMContext):
    await state.update_data(teacher_info=message.text)
    data = await state.get_data()
    text = f"""
    Kurs nomi: {data['name']}
    Kurs narxi: {data['price']}
    To'liq malumot: {data['full_info']}
    Kurs o'qituvchisi haqida malumot: {data['teacher_info']}

    HAMMA MALUMOT TO'GRIMI
    """

    await message.answer(text=text, reply_markup=reyly_buttons())




async def main():
    print("WELL DONE...")
    dp.include_router(form_router)
    await dp.start_polling(bot)


if __name__ == ("__main__"):
    asyncio.run(main())










