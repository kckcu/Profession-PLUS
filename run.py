import asyncio
import logging
import sys
from os import getenv
from aiogram import F
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
TOKEN = '7657653083:AAFRDKRNu_avU5UKe3gU9C7baa2Ip4PrJQk'


bot = Bot(token=TOKEN)
dp = Dispatcher()



async def main():
    await dp.start_polling(bot)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAANEZx4z1F93mh4aOCpc95ZBD5a68q0AApvqMRtZafFIzyo8CyC6H6kBAAMCAAN4AAM2BA",
    caption="""<b>Привет!☺️</b>\n\nНаша команда <u><b>Profession PLUS</b></u> проводит профориентации и занятия по подготовке к экзаменам для детей сирот. "Наша цель - помочь определиться подросткам, чем они хотят заниматься по жизни и помочь им достигнуть своей цели.\n\nИнтересно? Читай подробнее о нас и регистрируйся на мероприятие!🔥🤙\n\n/about_us - Тут ты можешь ознакомиться с тем, как мы проводим мероприятия и что тебя ждет на них\n/take_part - Прочитал? Принимай участие!\n/support - Если остались какие-либо вопросы или предложения, пиши нам :)""", 
        parse_mode='HTML') 

@dp.message(Command("about_us"))
async def about_us(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="На главную", callback_data="start")]
    ])
    await message.answer("В этом году мы сдали ЕГЭ и поступили в вуз. Поступление - это очень интересный, увлекательный, но в то же время и очень непростой этап в нашей жизни. Нас поддерживали родители, которые помогали нам и давали советы. Но немаловажным аспектом при выборе вуза явилось посещение дней открытых дверей и мероприятий, организованных приемной комиссией вуза. К сожалению, есть дети, которые лишены родительской поддержки. Это воспитанники детских домов и интернатов. И у нас возникла мысль: а можем ли мы, студенты, помочь таким детям в выборе правильного жизненного пути, своего призвания, профессии и вуза и подготовки к ним?\n\nПроведение студентами профориентационных и образовательных мероприятий (например, интенсивов по подготовке к экзаменам), мастер-классов по своей профессии, как один из вариантов - в рамках студенческой практики, позволит детям из детских домов и интернатов узнать лучше о той или иной профессии, вузе, программе обучения, перспективах трудоустройства и востребованности специальности, занять достойное место в обществе и найти свой жизненный путь.\n\nМы - студенты МАИ, имеем достаточно опыта в подготовке к ЕГЭ, а также много знакомых с различных факультетов нашего вуза, которые с радостью расскажут вам о перспективах в различных отраслях\n\nМы будем выкладывать даты ближайших мероприятий в детских домах, ты можешь подать заявку на участие и приехать по адресу. При этом при подаче заявки тебе нужно будет указать свой адрес своего детдома. Так мы собираем статистику по тем местам, где живут наиболее заинтерисованные в своем будущем подростки и стараемся проводить больше обучающих встреч и профориентаций в таких местах!",reply_markup=keyboard)

@dp.message(Command("support"))
async def about_us(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="На главную", callback_data="stat")]
    ])
    await message.answer("💫Мы очень ценим обратную свзязь и будем рады ответить на возникшие вопросы или выслушать предложения.\n Можете написать нам:\n\n ✏️<u>Жучкова Екатерина</u> - @deiteryy\n\n✏️<u>Никитина Анастасия </u>- @niknastacy\n\n✏️<u>Юлия Павлова</u> - @Lea_Owo\n\n✏️<u>Гузова Виктория</u> - @guuuzova_v",parse_mode="HTML",reply_markup=keyboard)

@dp.callback_query(F.data == "start")
async def start_callback(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="AgACAgIAAxkBAANEZx4z1F93mh4aOCpc95ZBD5a68q0AApvqMRtZafFIzyo8CyC6H6kBAAMCAAN4AAM2BA",
        caption="""<b>Привет!☺️</b>\n\nНаша команда <u><b>Profession PLUS</b></u> проводит профориентации и занятия по подготовке к экзаменам для детей сирот. "Наша цель - помочь определиться подросткам, чем они хотят заниматься по жизни и помочь им достигнуть своей цели.\n\nИнтересно? Читай подробнее о нас и регистрируйся на мероприятие!🔥🤙\n\n/about_us - Тут ты можешь ознакомиться с тем, как мы проводим мероприятия и что тебя ждет на них\n/take_part - Прочитал? Принимай участие!\n/support - Если остались какие-либо вопросы или предложения, пиши нам :)""",
        parse_mode='HTML'
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Начать", callback_data="start")]
    ])
    await callback_query.answer()

class Reg(StatesGroup):
    date = State()
    f_name = State()
    l_name = State()
    address = State()

@dp.callback_query(F.data == "cancel")
async def cancel(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="На главную", callback_data="start")]
    ])
    await callback_query.message.answer("Регистрация завершена. Если хотите зарегистрироваться снова, используйте команду /take_part.", reply_markup=keyboard)
    await callback_query.answer()

@dp.message(Command("take_part"))
async def reg_date(message: Message, state: FSMContext):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Завершить регистрацию", callback_data="cancel")]
    ])
    await state.set_state(Reg.date)
    await message.answer("⚠️<b>Если вы хотите досрочно завершить регистрацию на каком-либо этапе - нажмите '<u>Завершить регистрацию</u>', при желании полностью пройти регистрацию введите все данные, они будут запрашиваться в следующих сообщениях</b>\n\n Введите дату в формате <u>dd.mm.yy</u> интересного вам мероприятия:\n\n✏️<u>03.11.24</u> - Профориентация. Направление - <b>Прикладная математика</b> 17:00 - 18:00\n\n✏️<u>10.11.24</u> - Подготовкa <b>ЕГЭ Профильная математика</b> Решение 18 задач 16:00-18:00.\n\n✏️<u>17.11.24</u> Профориентация. Направление - <b>Экономика</b> 15:00 - 16:00",parse_mode = "HTML",reply_markup=keyboard)

@dp.message(Reg.date)
async def reg_f_name(message: Message, state: FSMContext):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Завершить регистрацию", callback_data="cancel")]
    ])
    await state.update_data(date=message.text)
    await state.set_state(Reg.f_name)
    await message.answer("Введите ваше имя",reply_markup=keyboard)

@dp.message(Reg.f_name)
async def reg_l_name(message: Message, state: FSMContext):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Завершить регистрацию", callback_data="cancel")]
    ])
    await state.update_data(f_name=message.text)
    await state.set_state(Reg.l_name)
    await message.answer("Введите вашу фамилию",reply_markup=keyboard)

@dp.message(Reg.l_name)
async def reg_n(message: Message, state: FSMContext):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Завершить регистрацию", callback_data="cancel")]
    ])
    await state.update_data(l_name=message.text)
    await state.set_state(Reg.address)
    await message.answer("Введите адрес вашего детдома",reply_markup=keyboard)

@dp.message(Reg.address)
async def reg_n(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо за регистрацию, ждем вас :)\nПроверьте свои данные:\nДата:{data["date"]}\nИмя:{data["f_name"]}\nФамилия:{data["l_name"]}\nАдресс:{data["address"]}')
    await state.clear()

@dp.callback_query(F.data == "start")
async def start_callback(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="AgACAgIAAxkBAANEZx4z1F93mh4aOCpc95ZBD5a68q0AApvqMRtZafFIzyo8CyC6H6kBAAMCAAN4AAM2BA",
        caption="""<b>Привет!☺️</b>\n\nНаша команда <u><b>Profession PLUS</b></u> проводит профориентации и занятия по подготовке к экзаменам для детей сирот. "Наша цель - помочь определиться подросткам, чем они хотят заниматься по жизни и помочь им достигнуть своей цели.\n\nИнтересно? Читай подробнее о нас и регистрируйся на мероприятие!🔥🤙\n\n/about_us - Тут ты можешь ознакомиться с тем, как мы проводим мероприятия и что тебя ждет на них\n/take_part - Прочитал? Принимай участие!\n/support - Если остались какие-либо вопросы или предложения, пиши нам :)""",
        parse_mode='HTML'
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Начать", callback_data="start")]
    ])
    await callback_query.answer()

@dp.callback_query(F.data == "stat")
async def start_callback(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="AgACAgIAAxkBAANEZx4z1F93mh4aOCpc95ZBD5a68q0AApvqMRtZafFIzyo8CyC6H6kBAAMCAAN4AAM2BA",
        caption="""<b>Привет!☺️</b>\n\nНаша команда <u><b>Profession PLUS</b></u> проводит профориентации и занятия по подготовке к экзаменам для детей сирот. "Наша цель - помочь определиться подросткам, чем они хотят заниматься по жизни и помочь им достигнуть своей цели.\n\nИнтересно? Читай подробнее о нас и регистрируйся на мероприятие!🔥🤙\n\n/about_us - Тут ты можешь ознакомиться с тем, как мы проводим мероприятия и что тебя ждет на них\n/take_part - Прочитал? Принимай участие!\n/support - Если остались какие-либо вопросы или предложения, пиши нам :)""",
        parse_mode='HTML'
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Начать", callback_data="stat")]
    ])
    await callback_query.answer()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

     

@dp.message(F.photo)
async def photo(message: Message):
    photo_data = message.photo[-1]
    await message.answer(f'{photo_data}')
