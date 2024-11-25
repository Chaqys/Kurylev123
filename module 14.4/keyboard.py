from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = 'Рассчитать')],
        [KeyboardButton(text = 'Информация')],
        [KeyboardButton(text = 'Купить')]
    ], resize_keyboard = True
)
ikb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')],
        [InlineKeyboardButton(text = 'Формула расчёта', callback_data = 'formulas')]
    ]
)
ikb_2 = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Kalori Dengesi', callback_data = 'product_buying')],
        [InlineKeyboardButton(text = 'Fit Kalori', callback_data = 'product_buying')],
        [InlineKeyboardButton(text = 'Enerji Dengesi', callback_data = 'product_buying')],
        [InlineKeyboardButton(text = 'Kalori Kontrol', callback_data = 'product_buying')]
    ]
)