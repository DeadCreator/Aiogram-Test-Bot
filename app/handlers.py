from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()


class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Welcome, {message.from_user.first_name}',
                         reply_markup=kb.reply_main_unauthorized)


@router.message(F.text == 'Register')
async def reg_start(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Enter Your name', reply_markup=None)


@router.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Enter Your phone number', reply_markup=kb.reply_reg_phone)


@router.message(Reg.number)
async def reg_phone(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Thanks! Your name is {data["name"]}, and Your phone number is {data["number"]}',
                         reply_markup=kb.reply_main_authorized)
    await state.clear()
