from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, EMPTY_KEYBOARD
from config import token
import datetime as dt

bot = Bot(token=token)

LESSONS_TIMES = {dt.datetime(2021, 9, 21, 12, 40, 0),
                 dt.datetime(2021, 9, 21, 13, 35, 0),
                 dt.datetime(2021, 9, 23, 11, 40, 0),
                 dt.datetime(2021, 9, 24, 8, 40, 0),
                 dt.datetime(2021, 9, 24, 9, 35, 0)}


# ---------------------------------- Главное меню ----------------------------------
@bot.on.chat_message(text=['Стартуем', 'стартуем'])
@bot.on.chat_message(payload={'cmd': 'start'})
async def main_menu(message: Message):
    keyboard = Keyboard().add(Text('Абоба', {'cmd': 'aboba'}))\
        .add(Text('Мы поняли', {'cmd': 'understand'})).row()\
        .add(Text('Умные вещи', {'cmd': 'physics'})).row()\
        .add(Text('Время до следующего урока физики', {'cmd': 'time'})).row()\
        .add(Text('Help', {'cmd': 'help'}), color=KeyboardButtonColor.PRIMARY).row()\
        .add(Text('До свидания, Олег Борисович!', {'cmd': 'end'}), color=KeyboardButtonColor.POSITIVE)
    await message.answer('Главное меню получается', keyboard=keyboard)


# Абоба
@bot.on.chat_message(payload={'cmd': 'aboba'})
async def aboba(message: Message):
    await message.answer(aboba_text)


# Мы поняли
@bot.on.chat_message(payload={'cmd': 'understand'})
async def understand(message: Message):
    await message.answer('Не поняли? ... Ну понятно? Ещё объяснить? Давайте другой пример приведу ... Сложно, да?')


# Время до следующего урока физики
@bot.on.chat_message(payload={'cmd': 'time'})
async def time(message: Message):
    correct = set()
    now = dt.datetime.now()
    today = dt.datetime(2021, 9, 20 + now.weekday(), now.hour, now.minute, now.second)
    for lesson in LESSONS_TIMES:
        if lesson > today:
            correct.add(lesson-today)
    await message.answer(f'Fisting ass через: {min(correct)}')


# До свидания
@bot.on.chat_message(payload={'cmd': 'end'})
async def end(message: Message):
    await message.answer('До свидания, ребята', keyboard=EMPTY_KEYBOARD)


# ---------------------------------- Умные вещи ----------------------------------
@bot.on.chat_message(payload={'cmd': 'physics'})
async def physics(message: Message):
    keyboard = Keyboard().add(Text('Прямолинейное движение', {'cmd': '1'}))\
        .add(Text('Криволинейное движение', {'cmd': '2'})).row()\
        .add(Text('Динамика', {'cmd': '3'}))\
        .add(Text('Гидростатика', {'cmd': '4'})).row()\
        .add(Text('Работа, энергия, мощность', {'cmd': '5'}))\
        .add(Text('Термодинамика', {'cmd': '6'})).row()\
        .add(Text('Назад', {'cmd': 'назад'}), color=KeyboardButtonColor.POSITIVE)
    await message.answer('Сегодня у нас тема...', keyboard=keyboard)


# Прямолинейное движение
@bot.on.chat_message(payload={'cmd': '1'})
async def f1(message: Message):
    await message.answer(attachment='photo-207458451_457239022')


# Криволинейное движение
@bot.on.chat_message(payload={'cmd': '2'})
async def f2(message: Message):
    await message.answer(attachment='photo-207458451_457239023')


# Динамика
@bot.on.chat_message(payload={'cmd': '3'})
async def f3(message: Message):
    await message.answer(attachment='photo-207458451_457239024')


# Гидростатика
@bot.on.chat_message(payload={'cmd': '4'})
async def f4(message: Message):
    await message.answer(attachment='photo-207458451_457239025')


# Работа, энергия, мощность
@bot.on.chat_message(payload={'cmd': '5'})
async def f5(message: Message):
    await message.answer(attachment='photo-207458451_457239026')


# Термодинамика
@bot.on.chat_message(payload={'cmd': '6'})
async def f6(message: Message):
    await message.answer(attachment='photo-207458451_457239027')


# Назад
@bot.on.chat_message(payload={'cmd': 'назад'})
async def back(message: Message):
    await message.answer('Меняю направление вектора...')
    await main_menu(message)


# ---------------------------------- Help ----------------------------------
aboba_text = 'Я вам запрещаю сдавать ЕГЭ не на 100 баллов'
commands = ['(!) Текст Абобы откатывается при каждом перезапуске Олега Борисовича',
            'Забиндить Абобу: /aboba текст',
            'Посмотреть текст Абобы: /aboba_info']


@bot.on.chat_message(payload={'cmd': 'help'})
async def help_cmd(message: Message):
    await message.answer('\n'.join(commands))


@bot.on.chat_message(text=['/aboba <text>', '/aboba'])
async def aboba_bind(message: Message, text=None):
    global aboba_text
    if text is not None:
        await message.answer(f'Новый текст Абобы: {text}')
        aboba_text = text
    else:
        await message.answer('Чел, ты зафейлил: Текст не указан')


@bot.on.chat_message(text=['/aboba_info'])
async def aboba_info(message: Message):
    await message.answer(f'Текущий текст Абобы: {aboba_text}')


bot.run_forever()
