from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.for_start import get_buttons

router = Router()
@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Привет {0.first_name}! Я крипто бот\nУ меня есть 3 кнопки".format(message.from_user),
                         reply_markup=get_buttons())

@router.message(F.text)
async def get_quantity(message: types.Message, state: FSMContext):
    data = message.text
    data = data.replace(',', '.')
    await state.update_data(quantity=data)