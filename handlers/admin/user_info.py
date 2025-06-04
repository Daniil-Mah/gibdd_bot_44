"""Вывод информации о пользователе"""

from aiogram.types import CallbackQuery
from database.models import User, Admin

user_info_id = [User.username]

@dp.callback_query_handler(text='')  
async def load_test(callback_query: types.CallbackQuery):  
    await callback_query.answer()  
    callback_data = user_info_id
    print(callback_data) 