from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_buttons():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Курс ETH/USDT",
        callback_data="eth_rate")
    )
    builder.add(types.InlineKeyboardButton(
        text='Обмен ETH на USDT',
        callback_data='eth_to_usdt'
    ))
    builder.add(types.InlineKeyboardButton(
        text='Обмен USDT на ETH',
        callback_data='usdt_to_eth'
    ))

    return builder.as_markup()