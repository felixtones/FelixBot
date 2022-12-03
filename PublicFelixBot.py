# Команды: start, help, language, bio, presets, menu, articles, nft, recording, linktree

import telebot
from telebot import TeleBot
from telebot import types

bot: TeleBot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = f'{message.from_user.first_name} {message.from_user.last_name}'
    bot.reply_to(message, "Приветсвую в моём боте помощнике, " + name)
    bot.reply_to(message, "Сейчас идёт его доработка! Но уже доступны команды: /start,  /menu,  /bio,  /presets,  /help ")

@bot.message_handler(commands=['nft'])
def working(message):
    bot.reply_to(message, "Эта команда ещё не доступна")

@bot.message_handler(commands=['help'])
def help(message):
    name = f'{message.from_user.first_name} {message.from_user.last_name}'
    bot.reply_to(message, name + '!' + ' Сейчас идёт доработка бота! Но уже доступны команды: /start,  /menu,  /bio,  /presets,  /help ')


@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    bio = types.KeyboardButton('bio')
    help = types.KeyboardButton('help')
    language = types.KeyboardButton('language')
    nft = types.KeyboardButton('NFT')
    linktree = types.KeyboardButton('linktree')
    markup.add(bio, help, language, nft, linktree)
    bot.send_message(message.chat.id, 'Переход в меню...', reply_markup=markup)

@bot.message_handler(commands=['presets'])
def presets(message):
    bot.reply_to(message, "Вы хотите получить мои бесплатные пресеты для Lightroom PC?")
    bot.reply_to(message, "Просто скажите ДА!")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('ДА', url='https://drive.google.com/drive/folders/1SuR9ym0TCLQDqgEOIqzsw9qxry8tylyV?usp=sharing'))
    bot.send_message(message.chat.id, 'Подготавливаю ссылку...', reply_markup=markup)

@bot.message_handler(commands=['bio'])
def bio(message):
    bot.reply_to(message, "My name is Dmitry Sofronov. But you can call me Felix Felton. I'm 21 years old. I am from Russia, the city of Kazan. I am a professional photographer in a variety of genres. I keep my blog on social networks, which is growing thanks to various aspects of creativity: text, visual component, writing projects, and now NFT. In addition, I am engaged in writing. I have already released my first two books, «Peroxide of Youth» and «5 Sacramentum» Now I am engaged in writing the third draft book «Boy-Verse» Returning to photography, I develop training courses, techniques, color schemes. I am experimenting, creating new subgenres of photography - for example, «Frizz Prism» and «Prismgraphy» - the concepts of «Half/Black and White Prismagraphy». The brightest of the created ones is the new direction «AFTERWARDS NEON». I am also involved in investing, I understand economics, history, law, but I am studying at a technical university in the field of robotics. I have been professionally engaged in robotics for 8 years. This is just the tip of the iceberg! In general, I am an intellectual, an aristocrat, a playboy, a philanthropist, but not yet a billionaire...")
    bot.reply_to(message, 'Nice to meet you!')
    photo = open('DSC00555.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['articles'])
def articles(message):
    bot.reply_to(message, "Выберете статью")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    dissapir = types.KeyboardButton('Куда я исчез?')
    experience = types.KeyboardButton('My experience in the NFT!')
    librery = types.KeyboardButton('Библиотека')
    markup.add(dissapir, experience, librery)
    bot.send_message(message.chat.id, 'Проверяю базу данных...', reply_markup=markup)

@bot.message_handler(commands=['recording'])
def recording(message):
    name = f'{message.from_user.language_code} {message.from_user.last_name}'
    id = f'{message.from_user.id}'
    bot.reply_to(message, name + '!' + 'Спасибо, что хотите обратиться ко мне, я очень ценю это!')
    bot.reply_to(message, 'Сейчас записаться на съёмку можно связавшись со мной @felixtones или через почту byfelixtones@gmail.com, написав ваш Telegram ID - ' + id)


@bot.message_handler(commands=['language'])
def language(message):
    langcode = f'{message.from_user.language_code}'
    bot.reply_to(message, 'Your language is ' + langcode + ' now')
    if langcode == 'ru':
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
       lang = types.KeyboardButton('eng')
       markup.add(lang)
       bot.send_message(message.chat.id, 'Do you want to switch the language to', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        lang = types.KeyboardButton('ru')
        markup.add(lang)
        bot.send_message(message.chat.id, 'Do you want to switch the language to', reply_markup=markup)

@bot.message_handler(commands=['linktree'])
def linktree(message):
    bot.reply_to(message, 'Добро пожаловать в мою Вселенную!')
    photo1 = open('EFPiW-u8zyM.jpg', 'rb')
    photo2 = open('s-05kCtbkJw.jpg', 'rb')
    photo3 = open('vQ-LrqWuVKI.jpg', 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)



#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
    #if message.text == "Да" or "Yes":
        #bot.reply_to(message, "Отправляю...") and bot.reply_to(message, "https://drive.google.com/drive/folders/1SuR9ym0TCLQDqgEOIqzsw9qxry8tylyV?usp=sharing")
	#elif message.text == 'Нет' or 'No':
		#bot.reply_to(message, 'Запрос отклонён')

bot.infinity_polling()
