import asyncio

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from dotenv import load_dotenv

from utils import get_crypt

router = Router()
load_dotenv()

class Dialog(StatesGroup):
    quantity = State()

@router.callback_query(F.data == "eth_rate")
async def send_eth_rate(callback: types.CallbackQuery):
    await callback.message.answer(f'1 ETH стоит - {await get_crypt()} USDT')
    await callback.answer()

@router.callback_query(F.data == 'eth_to_usdt')
async def exchange_eth_to_usdt(callback: types.callback_query, state: FSMContext):
    await callback.message.answer('Введите сумму для перевода в течении 10 секунд')
    await asyncio.sleep(10)
    await state.set_state(Dialog.quantity)

    input_data = await state.get_data()
    try:
        await callback.message.answer(f"Вы ввели {float(input_data['quantity'])}, скоро я смогу отправить тебе ссылку на перевод как только меня доработают")
    except KeyError:
        await callback.message.answer('Вы ничего не ввели, для обмена нажмите на кнопку')
    except ValueError:
        await callback.message.answer('Введенное значение должно быть числом')

    await state.clear()
    await callback.answer()


@router.callback_query(F.data == 'usdt_to_eth')
async def exchange_eth_to_usdt(callback: types.callback_query, state: FSMContext):
    await callback.message.answer('Введите сумму для перевода в течении 10 секунд')
    await asyncio.sleep(10)
    await state.set_state(Dialog.quantity)

    input_data = await state.get_data()

    try:
        await callback.message.answer(f"Вы ввели {float(input_data['quantity'])}, скоро я смогу отправить тебе ссылку на перевод как только меня доработают")
    except KeyError:
        await callback.message.answer('Вы ничего не ввели, для обмена нажмите на кнопку')
    except ValueError:
        await callback.message.answer('Введенное значение должно быть числом')

    await state.clear()
    await callback.answer()