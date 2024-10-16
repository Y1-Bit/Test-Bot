from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.misc.exchange import get_exchange_rate
from tgbot.misc.states import UserState

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message, state: FSMContext):
    await message.reply("Добрый день. Как вас зовут?")
    await state.set_state(UserState.waiting_for_name)


@user_router.message(UserState.waiting_for_name)
async def user_get_name(message: Message, state: FSMContext):
    user_name = message.text
    exchange_rate = get_exchange_rate()
    await message.reply(
        f"Рад знакомству, {user_name}! Курс доллара сегодня {exchange_rate}р"
    )
    await state.clear()
