from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart, StateFilter, Text
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)

bot: Bot = Bot(token='6139129751:AAHrxcotJ7h6XSVAWnfbwfRL6i6lhnUG-zI') # регестрируем бота
dp: Dispatcher = Dispatcher(bot=bot)

@dp.message(CommandStart())
async def start(message : Message):
    bag = InlineKeyboardButton(text='Ручная кладь👜',callback_data='bag')
    plane = InlineKeyboardButton(text='Время вылета✈️',callback_data='plane')
    luggage = InlineKeyboardButton(text='Багаж👜',callback_data='luggage')
    reg = InlineKeyboardButton(text='Регистрация✈️',callback_data='reg')
    key_b =InlineKeyboardMarkup(inline_keyboard=[[bag,luggage],[plane,reg]])
    await message.answer('Привет, я чат-бот авиакомпании S7 Airlines!'
                         '\nЯ отвечу на твои вопросы по поводу предстоящего путешествия!'
                         '\nСкажи, с чем возникли трудности?',reply_markup=key_b)

@dp.callback_query(lambda x: x.data =='bag')
async def bag(callback: CallbackQuery):
    await callback.message.answer('Что можно взять в ручная кладь:'
                                  '\n- сумку или чемодан 55*23*40см, для пассажиров экономического класса весом до 10 кг,  для пассажиров бизнес-класса - 15 кг'
                                  '\n-рюкзак или дамская сумка до 5 кг'
                                  '\n-костыли, трости, ходунки, складное кресло-коляска'
                                  '\n-люльку для переноски ребенка до 2 лет  55*23*40см'
                                  '\n- запечатанные товары DutyFree до 3 кг'
                                  '\n-букет цветов, портплед, верхняя одежда'
                                    '\nС запрещенными предметами для перевозки вы можете ознакомиться здесь helpcenter.s7.ru')

@dp.callback_query(lambda x: x.data == 'luggage')
async def luggage(callback: CallbackQuery):
    await callback.message.answer('Сдавайте багаж на регистрации и получайте в конечном пункте, если путешествуете с пересадкой нашей авиакомпанией!'
                                  '\nПодробнее вы можете ознакомиться по ссылке helpcenter.s7.ru')


@dp.callback_query(lambda x: x.data =='plane')
async def plane(callback: CallbackQuery):
    # p3017 = InlineKeyboardButton(text='3017',callback_data='p3017')
    # p3018 = InlineKeyboardButton(text='3018',callback_data='p3018')
    # key_b = InlineKeyboardMarkup(inline_keyboard=[[p3017],[p3018]])
    await callback.message.answer('Укажите номер вашего рейса для получения ответа.\n'
                                  '\nТакже вы можете установить наше приложение S7 Airlines и всегда быть в курсе начала и окончания регистрации, доступна онлайн-регистрация, уведомления о стойках выдачи багажа и бонусная система.'
                                  '\n доступные рейсы:3017, 1018')
                                  #,reply_markup=key_b )


@dp.message(lambda x:x.text =='3017')
async def p3017(message: Message):
    await message.answer('Москва-Иркутск время вылета 21:35. Время полета 5ч 45минут'
                                  '\nОбращаем Ваше внимание - возможны изменения.')


@dp.message(lambda x:x.text =='3018')
async def p3018(message: Message):
    await message.answer('Иркутск-Москва время вылета 9:35. Время полета 6ч 20 мин'
                                  '\nОбращаем Ваше внимание - возможны изменения')


@dp.callback_query(lambda x:x.data =='reg')
async def reg(callback: CallbackQuery):
    await callback.message.answer('Регистрация на рейс начинается за 32 часа до вылета и заканчивается за 40 минут до вылета. '
                                  '\nВы можете пройти ее в аэропорту вылета или через наше приложение S7 Airlines.')


if __name__ == '__main__':
    dp.run_polling(bot)