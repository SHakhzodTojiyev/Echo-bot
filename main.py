from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "5169023953:AAEKC2NwfY0jVFIYecODWflSaVmNdddU4bY"
bot = Bot(token=TOKEN)
dp  = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def inital_message(message:types.Message):
    chat_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username

    text = f"Assalomu alaykum {first_name}!\n Username: {username}"

    await bot.send_message(chat_id=chat_id, text=text)

@dp.message_handler()
async def sand_message(message:types.Message):
    text = f"Siz yuborgan habar: <b>{message.text}</b>"

    await message.answer(text, parse_mode="HTML")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)