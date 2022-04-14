from aiogram.dispatcher.filters import Command, Text
from aiogram.types import  Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Zhanr tanda!", reply_markup=menu)

@dp.message_handler(Text(equals=["Комедия", "Мелодрама", "Фантастика"]))
async def get_food(message: Message):
    await message.answer(f"Choosen {message.text}.Кумао/Thanks", reply_markup=ReplyKeyboardRemove())