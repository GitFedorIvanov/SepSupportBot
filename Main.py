command_prefix = "/task"

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import os

# Задаем токен бота при запуске
TOKEN = os.getenv("tg_token")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command(command_prefix[1:]))
async def new_topic(message: types.Message):
    # Игнорируем сообщения от самого бота
    if message.from_user.id == (await bot.get_me()).id:
        return

    # Извлекаем текст после команды /NewTopic
    topic_name = message.text[len(command_prefix):].strip()

    if not topic_name:
        await message.reply(f"Пожалуйста, укажите название топика после команды. Пример: {command_prefix} Нет связи с AP")
        return

    if message.chat.type != "supergroup":
        await message.reply("Эта команда работает только в супергруппах.")
        return

    try:
        # Создаем новый топик
        topic = await bot.create_forum_topic(chat_id=message.chat.id, name=topic_name)
        await message.reply(f"Создан новый запрос: {topic.name}")


    except Exception as e:
        await message.reply(f"Ошибка при создании топика: {e}")


async def main():
    # Запуск поллинга
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())