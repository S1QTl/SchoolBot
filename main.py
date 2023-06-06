from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart, StateFilter, Text
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.methods import SendPhoto
from Buttons2class import *
from Buttons1class import *
from Buttons3class import *
from Buttons4class import *
from Cue import *
bot: Bot = Bot(token='6042653605:AAHIztBW2H1EPLSTThAQyQgU4aWWKsA52kA', parse_mode='HTML')  # регестрируем бота
dp: Dispatcher = Dispatcher(bot=bot)
score = {}



class FSMFillForm(StatesGroup):
    answ7 = State()
    answ8 = State()
    answ9 = State()
    answur = State()
    PHOTO = State()
    cl3answer4 = State()
    cl3answer6 = State()
    cl3answer11 = State()
    cl4answer7 = State()
    cl4answer11 = State()
@dp.message(CommandStart())
async def start(message: Message):
    game = InlineKeyboardButton(text='играть', callback_data='game')
    callb = InlineKeyboardButton(text='обратная связь', callback_data='callb')
    clue = InlineKeyboardButton(text='подсказки', callback_data='clue')
    key_b1 = InlineKeyboardMarkup(inline_keyboard=[[game], [clue], [callb]])
    await message.answer('Здравствуй, дорогой друг! Сегодня ты сможешь поиграть в небольшую игру, '
                            'а также проверить свои знания. '
                            'Ты готов? Если да, то давай начнем!', reply_markup=key_b1)


@dp.callback_query(lambda x: x.data =='callb')
async def callb(callback: CallbackQuery):
    await callback.message.answer('дорогой друг! Если у тебя возникли проблемы или пожелания по работе бота,'
                                  'пиши @slvanay_vv или @NikitaKozhemaka')

@dp.callback_query(lambda x: x.data == 'menu')
async def start(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    game = InlineKeyboardButton(text='играть', callback_data='game')
    clue = InlineKeyboardButton(text='подсказки', callback_data='clue')
    key_b = InlineKeyboardMarkup(inline_keyboard=[[game], [clue]])
    await callback.message.answer(
        'Здравствуй, дорогой друг! Сегодня ты сможешь поиграть в небольшую игру, '
        'а также проверить свои знания. '
        'Ты готов? Если да, то давай начнем!', reply_markup=key_b)

@dp.callback_query(lambda x: x.data == 'clue')
async def category_cue(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    cue7 = InlineKeyboardButton(text='7лет(1класс)', callback_data='cue7')
    cue8 = InlineKeyboardButton(text='8лет(2класс)', callback_data='cue8')
    cue9 = InlineKeyboardButton(text='9лет(3класс)', callback_data='cue89')
    cue10 = InlineKeyboardButton(text='10лет(4класс)', callback_data='cue10')
    key_b = InlineKeyboardMarkup(inline_keyboard=[[cue7, cue8], [cue9, cue10]])
    await callback.message.answer('Дорогой друг! Если тебе нужна небольшая подсказка или вспомнить материал, '
                                  'то ты можешь это сделать) Выбери свою возрастную категорию"',
                                  reply_markup=key_b)


@dp.callback_query(lambda x: x.data == 'cue7')
async def category_cue(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    menu = InlineKeyboardButton(text='Главное меню', callback_data='menu')
    key_menu = InlineKeyboardMarkup(inline_keyboard=[[menu]])
    await bot.send_photo(callback.from_user.id, photo=cue11)
    await bot.send_photo(callback.from_user.id, photo=cue12)
    await bot.send_photo(callback.from_user.id, photo=cue13)
    await bot.send_photo(callback.from_user.id, photo=cue14)
    await bot.send_photo(callback.from_user.id, photo=cue15)
    await bot.send_photo(callback.from_user.id, photo=cue16)
    await bot.send_photo(callback.from_user.id, photo=cue17)
    await callback.message.answer('главное меню' , reply_markup=key_menu)


@dp.callback_query(lambda x: x.data == 'cue8')
async def category_cue(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    menu = InlineKeyboardButton(text='Главное меню', callback_data='menu')
    key_menu = InlineKeyboardMarkup(inline_keyboard=[[menu]])
    await bot.send_photo(callback.from_user.id, photo=cue21)
    await bot.send_photo(callback.from_user.id, photo=cue22)
    await bot.send_photo(callback.from_user.id, photo=cue23)
    await bot.send_photo(callback.from_user.id, photo=cue24)
    await bot.send_photo(callback.from_user.id, photo=cue25)
    await bot.send_photo(callback.from_user.id, photo=cue26)
    await bot.send_photo(callback.from_user.id, photo=cue27)
    await bot.send_photo(callback.from_user.id, photo=cue28)
    await callback.message.answer('главное меню' , reply_markup=key_menu)


@dp.callback_query(lambda x: x.data == 'cue9')
async def category_cue(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    menu = InlineKeyboardButton(text='Главное меню', callback_data='menu')
    key_menu = InlineKeyboardMarkup(inline_keyboard=[[menu]])
    await bot.send_photo(callback.from_user.id, photo=cue31)
    await bot.send_photo(callback.from_user.id, photo=cue32)
    await bot.send_photo(callback.from_user.id, photo=cue33)
    await bot.send_photo(callback.from_user.id, photo=cue34)
    await bot.send_photo(callback.from_user.id, photo=cue35)
    await bot.send_photo(callback.from_user.id, photo=cue36)
    await bot.send_photo(callback.from_user.id, photo=cue37)
    await callback.message.answer('главное меню' , reply_markup=key_menu)


@dp.callback_query(lambda x: x.data == 'cue10')
async def category_cue(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    menu = InlineKeyboardButton(text='Главное меню', callback_data='menu')
    key_menu = InlineKeyboardMarkup(inline_keyboard=[[menu]])
    await bot.send_photo(callback.from_user.id, photo=cue41)
    await bot.send_photo(callback.from_user.id, photo=cue42)
    await bot.send_photo(callback.from_user.id, photo=cue43)
    await bot.send_photo(callback.from_user.id, photo=cue44)
    await bot.send_photo(callback.from_user.id, photo=cue45)
    await bot.send_photo(callback.from_user.id, photo=cue46)
    await bot.send_photo(callback.from_user.id, photo=cue47)
    await bot.send_photo(callback.from_user.id, photo=cue48)
    await bot.send_photo(callback.from_user.id, photo=cue49)
    await callback.message.answer('главное меню' , reply_markup=key_menu)

@dp.callback_query(lambda x: x.data == 'game')
async def category(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    age7 = InlineKeyboardButton(text='7лет(1класс)', callback_data='age7')
    age8 = InlineKeyboardButton(text='8лет(2класс)', callback_data='age8')
    age9 = InlineKeyboardButton(text='9лет(3класс)', callback_data='age9')
    age10 = InlineKeyboardButton(text='10лет(4класс)', callback_data='age10')
    key_b = InlineKeyboardMarkup(inline_keyboard=[[age7, age8], [age9, age10]])
    await callback.message.answer('теперь выбери категорию', reply_markup=key_b)


@dp.callback_query(lambda x: x.data == 'age7')
async def answer1(callback: CallbackQuery):
    score[callback.from_user.id] = 0
    print(score)
    await callback.message.answer('<b>1. Найдите слово, в котором букв больше, чем звуков.</b>',
                                  reply_markup=cl1answ1)


@dp.callback_query(lambda x: x.data in ['a11', 'a12', 'a12', 'a14'])
async def answer2(callback: CallbackQuery):
    if callback.data == 'a14':
        score[callback.from_user.id] += 1
        print(score)
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('2.Укажите, между какими числами стоит число 17', reply_markup=cl1answ2)


@dp.callback_query(lambda x: x.data in ['a21', 'a22', 'a23', 'a24'])
async def answer3(callback: CallbackQuery):
    if callback.data == 'a22':
        score[callback.from_user.id] += 1
        print(score)
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('3. Какой город является столицей России?', reply_markup=cl1answ3)


@dp.callback_query(lambda x: x.data in ['st', 'mos', 'nov', 'kal'])
async def answer4(callback: CallbackQuery):
    if callback.data == 'mos':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('4. Какой орган помогает определить вкус пищи?', reply_markup=cl1answ4)


@dp.callback_query(lambda x: x.data in ['a41', 'a42', 'a43', 'a44'])
async def answer5(callback: CallbackQuery):
    if callback.data == 'a44':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('5. Найдите слово, которое обозначает действие предмета.', reply_markup=cl1answ5)


@dp.callback_query(lambda x: x.data in ['a51', 'a52', 'a53', 'a54'])
async def answer6(callback: CallbackQuery):
    if callback.data == 'a51':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('6.В какое время года можно наблюдать листопад?', reply_markup=cl1answ6)


@dp.callback_query(lambda x: x.data in ['a61', 'a62', 'a63', 'a64'])
async def answer7(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'a61':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('7. Решите задачу:\n На аэродроме было 8 самолётов  Ил-86 и 9 самолетов Ту-134.'
                                  '\n Прилетели ещё 3 самолёта. \n Сколько самолётов всего на аэродроме?\n '
                                  'введите только число ')
    await state.set_state(FSMFillForm.answ7)


@dp.message(StateFilter(FSMFillForm.answ7), lambda x: len(x.text) == 2)
async def answer8( message: Message):
    if message.text == '20':
        score[message.from_user.id] += 1
        print(score)
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('8. Найдите слово, в котором пропущена буква о.', reply_markup=cl1answ8)



@dp.callback_query(lambda x: x.data in ['a81','a82','a83','a84'])
async def answer9(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'a83':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('9. Прочитайте текст и выполните задание.'
                                    '\n                             Курочка.'
                                    '\nХодила курочка с цыплятами по двору. Вдруг пошел дождик. Курочка'
                                    ' скорей на землю присела, все перышки растопырила и заквохтала: «Квох-'
                                    ' квох-квох-квох!» Это значит: прячьтесь скорей. И все цыплята залезли к ней'
                                    ' под крылышки, зарылись в ее теплые перышки. Кто совсем спрятался, у кого'
                                    'только ножки видны, у кого головка торчит, а у кого только глаз '
                                    'выглядывает.'
                                    ' А два цыпленка не послушались своей мамы и не спрятались. Стоят, пищат'
                                    ' и удивляются: что это такое им на головку капает?'
                                    '\nСколько цыплят не послушали маму?')
    await state.set_state(FSMFillForm.answ9)


@dp.message(StateFilter(FSMFillForm.answ9),lambda x: len(x.text) == 1)
async def answer10(message: Message, state: FSMContext ):
    if message.text == '2':
        score[message.from_user.id] += 1
        print(score)
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('10. Какое слово лишнее в ряду?', reply_markup=cl1answ10)
    await state.clear()


@dp.callback_query(lambda x: x.data == 'age8')
async def class2answ1(callback: CallbackQuery):
    score[callback.from_user.id] = 0
    print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('1. В каких приведённых ниже народных сказках один из персонажей – лиса?',
                                  reply_markup=cl2answ1)


@dp.callback_query(lambda x: x.data in ['gus', 'col', 'kasha', 'strah'])
async def class2answ2(callback: CallbackQuery):
    if callback.data == 'col':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('2. Найдите группу родственных слов.',reply_markup=cl2answ2)

@dp.callback_query(lambda x: x.data in ['gr1', 'gr2', 'gr3', 'gr4'])
async def class2answ3(callback: CallbackQuery):
    if callback.data == 'gr3':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('3. Решите задачу. Садовник в первый день обрезал 24 куста, а во второй день — '
                                  '37 кустов. После этого ему осталось обрезать ещё 10 кустов. '
                                  '\nСколько всего кустов нужно было обрезать садовнику?', reply_markup=cl2answ3)


@dp.callback_query(lambda x: x.data in ['s61','s71', 's59', 's44'])
async def class2answ4(callback: CallbackQuery):
    if callback.data == 's71':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('4. Найдите ряд, в котором все слова начинаются с согласного звука'
                                  , reply_markup=cl2answ4)


@dp.callback_query(lambda x: x.data in ['ecr', 'ded', 'ruk', 'chudo'])
async def class2answ5(callback: CallbackQuery):
    if callback.data == 'ruk':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('5. Что относится к живой природе?'
                                  , reply_markup=cl2answ5)


@dp.callback_query(lambda x: x.data in ['kar', 'snow', 'rust'])
async def class2answ6(callback: CallbackQuery):
    if callback.data == 'rust':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('6. Прочитай загадку С. Маршака, выбери отгадку.'
                                                        '\nВсегда шагаем мы вдвоём,'
                                                        '\nПохожи мы, как братья,'
                                                        '\nМы за обедом – под столом,'
                                                        '\nА ночью – под кроватью.'

                                  , reply_markup=cl2answ6)


@dp.callback_query(lambda x: x.data in ['tap', 'socks', 'perch', 'chair'])
async def class2answ7(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'tap':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('7. Решите уравнение.'
                                  '\n12 + х = 71')
    await state.set_state(FSMFillForm.answur)


@dp.message(StateFilter(FSMFillForm.answur), lambda x: len(x.text) >=1)
async def class2answer7(message: Message, state: FSMContext):
    if message.text == '59':
        score[message.from_user.id] += 1
        print(score)
    await bot.delete_message(message.from_user.id, message.message_id)
    rectangle = 'https://avatars.mds.yandex.net/get-images-cbir/9083101/vpWrevLZMq-SWpD_yGLXxg2361/ocr'
    await bot.send_photo(message.from_user.id, photo=rectangle)
    await message.answer('8. Какая фигура изображена на фото?', reply_markup=cl2answ8)
    await state.clear()


@dp.callback_query(lambda x: x.data in ['sqwr', 'rect', 'trngl', 'romb'])
async def class2answer8(callback: CallbackQuery):
    if callback.data == 'recr':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('9. По какому номеру нужно звонить чтобы вызвать скорую помощь?',
                                  reply_markup=cl2answ9)


@dp.callback_query(lambda x: x.data in ['s01', 's02', 's03', 's04'])
async def class2answer9(callback: CallbackQuery):
    if callback.data == 's03':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('10. На какой цвет светофора можно переходить дорогу?',reply_markup=cl2answ10)


@dp.callback_query(lambda x: x.data == 'age9')
async def class3answer1(callback: CallbackQuery):
    score[callback.from_user.id] = 0
    print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('1.Какое вещество воздуха нужно органам тела для работы?'
                                  , reply_markup=cl3answ1)


@dp.callback_query(lambda x: x.data in ['kisl', 'gaz', 'azot'])
async def class3answer2(callback: CallbackQuery):
    if callback.data == 'kisl':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('2. Что из перечисленного вредит здоровью?'
                                  ,reply_markup=cl3answ2)


@dp.callback_query(lambda x: x.data in ['morning', 'games', 'tv', 'pe'])
async def class3answer3(callback: CallbackQuery):
    if callback.data == 'tv':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('3. Укажите, о чём идёт речь.'
                                    '\nЭто самостоятельная часть речи, '
                                    'которая с другими словами пишется раздельно '
                                    'и служит для связи слов в предложении и словосочетании.'
                                  ,reply_markup=cl3answ3)


@dp.callback_query(lambda x: x.data in ['chisl', 'pris', 'chast', 'pred'])
async def class3answer4(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'pred':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('4. Напишите проверочное слово к слову крикливый. Подсказка: в этом слове 4 буквы.'
                                  '\nНапишите слово с Большой буквы')
    await state.set_state(FSMFillForm.cl3answer4)


@dp.message(StateFilter(FSMFillForm.cl3answer4), lambda x: len(x.text) >=1 )
async def class3answer5(message: Message, state: FSMContext):
    if message.text == 'Крик':
        score[message.from_user.id] += 1
        print(score)
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('5. Сколько в 8 сантиметров миллиметров? ', reply_markup=cl3answ5)
    await state.clear()

@dp.callback_query(lambda x: x.data in ['s8', 's18', 's80', 's800'])
async def class3answer6(callback: CallbackQuery, state: FSMContext):
    if callback.data == 's80':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('6.  Решите пример. Сколько будет 308+492?'
                                  '\nНапишите только число')
    await state.set_state(FSMFillForm.cl3answer6)


@dp.message(StateFilter(FSMFillForm.cl3answer6), lambda x: len(x.text) >= 1)
async def class3answer7(message: Message, state: FSMContext):
    if message.text == '800':
        score[message.from_user.id] += 1
        print(score)
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('7. Найдите продолжение пословицы. Тише едешь … ', reply_markup=cl3answ7)
    await state.clear()

@dp.callback_query(lambda x: x.data in ['today', 'batter', 'mind', 'next'])
async def class3answer8(callback: CallbackQuery):
    if callback.data == 's80':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('8. Выберите, что из списка относится к повествовательному предложению.'
                                  , reply_markup=cl3answ8)


@dp.callback_query(lambda x: x.data in ['wthr', 'gold', 'may', 'happy'])
async def class3answer9(callback: CallbackQuery):
    if callback.data == 'gold':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('9. В субботу туристы проехали 126км, а в воскресенье – на 31км больше.'
                                  '\nСколько километров проехали туристы за 2 дня?'
                                  '\n Введите только число'
                                  , reply_markup=cl3answ9)


@dp.callback_query(lambda x: x.data in ['s283', 's192', 's90', 's219'])
async def class3answer10(callback: CallbackQuery):
    if callback.data == 's283':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('10. Какие растения обитают в воде?'
                                  , reply_markup=cl3answ10)


@dp.callback_query(lambda x: x.data in ['moh', 'vodor', 'paporotnik', 'berez'])
async def class3answer11(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'vodor':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('11. Решите задачу. Масса ящика – 2 кг, а яблоки, которые находятся в нем в 6 раз тяжелее. '
                         '\nКакова масса ящика вместе с яблоками?' 
                        '\nВ ответе напишите число без единицы измерения.'
)
    await state.set_state(FSMFillForm.cl3answer11)


@dp.message(StateFilter(FSMFillForm.cl3answer11), lambda x: len(x.text) >= 0)
async def class3answer12(message: Message, state: FSMContext):
    if message.text =='14':
        score[message.from_user.id] += 1
        print(score)
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('12. Укажите слово с приставкой по-'
                                  , reply_markup=cl3answ12)
    await state.clear()


@dp.callback_query(lambda x: x.data == 'age10')
async def class4answer1(callback: CallbackQuery):
    score[callback.from_user.id] = 0
    print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('1.сниноним к слову пенять?',reply_markup=cl4answ1)


@dp.callback_query(lambda x: x.data in ['a411', 'a412', 'a413', 'a414'])
async def class4answer2(callback: CallbackQuery):
    if callback.data == 'a414':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('2. Для нахождения периметра п'
                                  'рямоугольника со сторонами 4см и 8см используют формулу….'
                                  ,reply_markup=cl4answ2)


@dp.callback_query(lambda x: x.data in ['a421','a422', 'a423', 'a424'])
async def class4answer3(callback: CallbackQuery):
    if callback.data == 'a423':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('3.Пергамент - это материал для письма из :',reply_markup=cl4answ3)


@dp.callback_query(lambda x: x.data in ['a431','a432', 'a433', 'a434'])
async def class4answer4(callback: CallbackQuery):
    if callback.data == 'a432':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('4. В каком падеже существительные 1-го склонения имеют окончание –и?'
                                  , reply_markup=cl4answ4)


@dp.callback_query(lambda x: x.data in ['a441','a442', 'a443', 'a444'])
async def class4answer5(callback: CallbackQuery):
    if callback.data == 'a442':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('5.Сколько лет в одном веку', reply_markup=cl4answ5)


@dp.callback_query(lambda x: x.data in ['a451', 'a452', 'a453', 'a454'])
async def class4answer6(callback: CallbackQuery):
    if callback.data == 'a453':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('6. Укажите порядок расположения полос на Государственном флаге Российской Федерации '
                                  , reply_markup=cl4answ6)




@dp.callback_query(lambda x: x.data in  ['a461', 'a462', 'a463', 'a464'])
async def class4answer7(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'a464':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('7. Переведите 5ч 15 мин в минуты. '
                                  '\nВ ответе запишите только число.')
    await state.set_state(FSMFillForm.cl4answer7)


@dp.message(StateFilter(FSMFillForm.cl4answer7), lambda x: len(x.text) >= 1)
async def class3answer8(message: Message, state: FSMContext):
    if message.text =='315':
        score[message.from_user.id] += 1
        print(score)
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('8. С каким глаголом не пишется слитно?'
                                  , reply_markup=cl4answ8)
    await state.clear()


@dp.callback_query(lambda x: x.data in ['a481', 'a482', 'a483', 'a484'])
async def class4answer9(callback: CallbackQuery):
    if callback.data == 'a482':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('9. Определите жанр произведения А.С. Пушкина «Няне».'
                                  , reply_markup=cl4answ9)


@dp.callback_query(lambda x: x.data in ['a491', 'a492', 'a493', 'a494'])
async def class4answer10(callback: CallbackQuery):
    if callback.data == 'a492':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('10. Солнце – это'
                                  , reply_markup=cl4answ10)


@dp.callback_query(lambda x: x.data in ['planet', 'galactic', 'cosm', 'telo'])
async def class4answer11(callback: CallbackQuery, state: FSMContext ):
    if callback.data == 'galactic':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('11. Как называются горы, которые разделяют Европу и Азию?'
                                  '\nВведите только название с большой буквы')
    await state.set_state(FSMFillForm.cl4answer11)



@dp.message(StateFilter(FSMFillForm.cl4answer11), lambda x: len(x.text) >= 1)
async def class4answer12(message: Message, state: FSMContext):
    if message.text == 'Уральские':
        score[message.from_user.id] += 1
        print(score)
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('12. К какой басне подходит пословица «Делу – время, а потехе – час»?'
                         , reply_markup=cl4answ12)
    await state.clear()


@dp.callback_query(lambda x: x.data in ['a4121', 'a4122', 'a4123', 'a4124'])
async def class4answer13(callback: CallbackQuery):
    if callback.data == 'a4124':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.message.answer('13.  Дочь родилась в 1965 году. Она на 25 лет младше мамы.'
                                  '\n В каком году родилась мама?'
                                  , reply_markup=cl4answ13)


@dp.callback_query(lambda x: x.data in ['a101', 'a102', 'a103', 'a104', 'a105'
                                        , 'green', 'yellow', 'red'
                                        , 'poh', 'posud', 'flour', 'poni'
                                        ,'a4131', 'a4132', 'a4133', 'a4134'])
async def end(callback: CallbackQuery):
    menu = InlineKeyboardButton(text='Главное меню', callback_data='menu')
    key_menu = InlineKeyboardMarkup(inline_keyboard=[[menu]])
    if callback.data == 'a105':
        score[callback.from_user.id] += 1
        print(score)
    if callback.data == 'green':
        score[callback.from_user.id] += 1
        print(score)
    if callback.data == 'poh':
        score[callback.from_user.id] += 1
        print(score)
    if callback.data == 'a4132':
        score[callback.from_user.id] += 1
        print(score)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    if score[callback.from_user.id] >= 8:
        await callback.message.answer('Ты молодец! Продолжай в том же духе. Если тебе понравилось, '
                                      'то можешь проверить свои знания в других категориях.',reply_markup=key_menu)
    if 5 <= score[callback.from_user.id] < 8:
        await callback.message.answer('Умничка! Тебе нужно немного потрудиться, '
                                      'чтобы побить свой рекорд. Главное не сдавайся, '
                                      'ведь учеба требует много сил и энергии!',reply_markup=key_menu)
    if score[callback.from_user.id] < 5:
        await callback.message.answer('Неплохой результат. Я уверена, что ты можешь лучше если немного постараешься. '
                                      ,reply_markup=key_menu)


if __name__ == '__main__':
    dp.run_polling(bot)
