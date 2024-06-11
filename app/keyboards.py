from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

reply_main_unauthorized = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Register')],
    [KeyboardButton(text='Login')]
], resize_keyboard=True)

reply_reg_phone = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Request My phone', request_contact=True)]
], resize_keyboard=True)


reply_main_authorized = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='kajslfdkjs')]
])
