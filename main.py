import telebot
from telebot import types

# main variables
TOKEN = ""
bot = telebot.TeleBot(TOKEN)


# handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, чем я могу тебе помочь?', reply_markup=main_markup)


@bot.message_handler(commands=['help'])
def start_handler(message):
    bot.send_message(message.from_user.id, "Напиши 'Привет'")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?", reply_markup=main_markup)
    elif message.text == "О компании":
        bot.send_message(message.from_user.id, "Здесь будет информация о компании", reply_markup=main_markup)
    elif message.text == "Наши проекты":
        bot.send_message(message.from_user.id, "Выберите проект для подробной информации", reply_markup=projects)
    elif message.text == "Социальные сети":
        social = types.InlineKeyboardMarkup()
        social_btn1 = types.InlineKeyboardButton(text='VK', url='https://vk.com/semles1')
        social.add(social_btn1)
        bot.send_message(message.chat.id, "Мы в социальных сетях:", reply_markup=social)
    elif message.text == "Пожертвовать":
        url = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text='Пожертвовать',
                                             url='https://vk.com/donate_app?mid=-165446511&ref=group_menu')
        url.add(url_btn)
        bot.send_message(message.chat.id, "Нажми на кнопку, чтобы оставить пожертвование.", reply_markup=url)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# markups
main_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
main_markup_btn1 = types.KeyboardButton('О компании')
main_markup_btn2 = types.KeyboardButton('Наши проекты')
main_markup_btn3 = types.KeyboardButton('Социальные сети')
main_markup_btn4 = types.KeyboardButton('Пожертвовать')
main_markup.add(main_markup_btn1, main_markup_btn2, main_markup_btn3, main_markup_btn4)

projects = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
projects_btn1 = types.KeyboardButton('Проект1')
projects_btn2 = types.KeyboardButton('Проект2')
projects.add(projects_btn1)


bot.polling(none_stop=True, interval=0)
