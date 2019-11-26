# coding=utf-8
import telebot
from emoji import emojize
import redis
from redis import StrictRedis

r = redis.from_url('redis://h:pb75f7d4e39e3203fa456be4b497fdc9caf807cc493d2c9ab54a969338780b8ab@ec2-34-246-8-129.eu-west-1.compute.amazonaws.com:30799')

TOKEN = '1060519841:AAF-mUfKpKKrSYc5r-rCxOaRoBPZ1lPgLzc'
bot = telebot.TeleBot(TOKEN)

heart = emojize(':heart:', use_aliases=True)
right = emojize(':right_arrow:', use_aliases=True)
left = emojize(':left_arrow:', use_aliases=True)
ledger = emojize(':ledger:', use_aliases=True)
phone = emojize(':speech_balloon:', use_aliases=True)
faqq = emojize(':page_facing_up:', use_aliases=True)
info = emojize(':information:', use_aliases=True)
house = emojize(':house:', use_aliases=True)

r.set(int(0), "Лера\nhttps://telegra.ph/file/fb134b7947d17e4522981.png"
              "\n\nStatus: ")

r.set(int(1), "Софи\nhttps://telegra.ph/file/2848b75621de5868a9814.png"
              "\n\nStatus: ")

r.set(int(2), "Виктория\nhttps://telegra.ph/file/59880dca747f0556b3948.png"
              "\n\nStatus: ")

r.set(int(3), "Лиза\nhttps://telegra.ph/file/ca80128b279ebe9baa75c.png"
              "\n\nStatus: ")

r.set(int(4), "Ангелина\nhttps://telegra.ph/file/8a5f9b05dd12382f02079.png"
              "\n\nStatus: ")

r.set(int(5), "Анастасия\nhttps://telegra.ph/file/1fdee4e1121774358a69b.png"
              "\n\nStatus: ")

r.set(int(6), "Эмилия\nhttps://telegra.ph/file/f84d6473133f070f0c07f.png"
              "\n\nStatus: ")

r.set(int(7), "Кристина\nhttps://telegra.ph/file/f35095123620006a9949b.png"
              "\n\nStatus: ")

r.set(int(100), "Лера\nhttps://telegra.ph/file/fb134b7947d17e4522981.png")
r.set(int(101), "Софи\nhttps://telegra.ph/file/2848b75621de5868a9814.png")
r.set(int(102), "Виктория\nhttps://telegra.ph/file/59880dca747f0556b3948.png")
r.set(int(103), "Лиза\nhttps://telegra.ph/file/ca80128b279ebe9baa75c.png")
r.set(int(104), "Ангелина\nhttps://telegra.ph/file/8a5f9b05dd12382f02079.png")
r.set(int(105), "Анастасия\nhttps://telegra.ph/file/1fdee4e1121774358a69b.png")
r.set(int(106), "Эмилия\nhttps://telegra.ph/file/f84d6473133f070f0c07f.png")
r.set(int(107), "Кристина\nhttps://telegra.ph/file/f35095123620006a9949b.png")

r.set(str('status' + '0'), "На вызове")
r.set(str('status' + '1'), "На вызове")
r.set(str('status' + '2'), "На вызове")
r.set(str('status' + '3'), "На вызове")
r.set(str('status' + '4'), "На вызове")
r.set(str('status' + '5'), "На вызове")
r.set(str('status' + '6'), "На вызове")
r.set(str('status' + '7'), "На вызове")

r.set(str('statuse' + '0'), "Busy")
r.set(str('statuse' + '1'), "Busy")
r.set(str('statuse' + '2'), "Busy")
r.set(str('statuse' + '3'), "Busy")
r.set(str('statuse' + '4'), "Busy")
r.set(str('statuse' + '5'), "Busy")
r.set(str('statuse' + '6'), "Busy")
r.set(str('statuse' + '7'), "Busy")

r.set(str('url' + '0'), "https://telegra.ph/Milana-11-23")
r.set(str('url' + '1'), "https://telegra.ph/Sofi-11-23")
r.set(str('url' + '2'), "https://telegra.ph/Oksana-11-23-2")
r.set(str('url' + '3'), "https://telegra.ph/Katya-11-23-3")
r.set(str('url' + '4'), "https://telegra.ph/Angelina-11-23-2")
r.set(str('url' + '5'), "https://telegra.ph/Natali-11-23-2")
r.set(str('url' + '6'), "https://telegra.ph/EHmiliya-11-23")
r.set(str('url' + '7'), "https://telegra.ph/Kristina-11-23-8")

r.set('price0', int(2500))
r.set('price1', int(2500))
r.set('price2', int(2500))
r.set('price3', int(2500))
r.set('price4', int(2500))
r.set('price5', int(2500))
r.set('price6', int(2500))
r.set('price7', int(3700))


@bot.message_handler(commands=['start'])
def start_command(message):
    r.set(str('Username') + str(message.chat.id), str(message.from_user.username))
    r.set(str('ChatID') + str(message.chat.id), str(message.chat.id))
    r.set((str('nomershluhi') + str(message.chat.id)), int(0))
    r.set((str('Nomerokna') + str(message.chat.id)), int(0))
    r.set('language' + str(message.chat.id), 'ukr')
    bot.send_message(message.chat.id,'...')
    menu(message)


def menu(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except:
        bot.clear_step_handler_by_chat_id(message.chat.id)
        language = r.get('language' + str(message.chat.id)).decode('utf-8')
        user = r.get(str('Username') + str(message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " перешел в меню")
        bot.send_message(936806920, "@" + str(user) + " перешел в меню")
        centum = telebot.types.InlineKeyboardMarkup()
        if str(language) == 'ukr':
            centum.row(
                telebot.types.InlineKeyboardButton(ledger + "Открыть каталог" + ledger, callback_data="kataloog")
            )
            centum.row(
                telebot.types.InlineKeyboardButton(phone + "Обратная связь" + phone, callback_data="support")
            )
            centum.row(
                telebot.types.InlineKeyboardButton(faqq + "F.A.Q" + faqq, callback_data="faq")
            )
            centum.row(
                telebot.types.InlineKeyboardButton("Language", callback_data="language")
            )
            if str(message.chat.id) == "697601461":
                centum.row(
                    telebot.types.InlineKeyboardButton("Відправити меседж мамонту", callback_data="messtomamont")
                )
            if str(message.chat.id) == "854450608":
                centum.row(
                    telebot.types.InlineKeyboardButton("Відправити меседж мамонту", callback_data="messtomamont")
                )
            bot.send_message(message.chat.id,
                             heart + "Рады видеть тебя в нашем оазисе "
                                     "удовольствия" + heart + "\nЕсли впервые с нами, нажми на F.A.Q для "
                                                              "ознакомления с правилами сервиса",
                             reply_markup=centum)
        else:
            centum.row(
                telebot.types.InlineKeyboardButton(ledger + "Open catalog" + ledger, callback_data="kataloog")
            )
            centum.row(
                telebot.types.InlineKeyboardButton(phone + "Support" + phone, callback_data="support")
            )
            centum.row(
                telebot.types.InlineKeyboardButton(faqq + "F.A.Q" + faqq, callback_data="faq")
            )
            centum.row(
                telebot.types.InlineKeyboardButton("Язык", callback_data="language")
            )
            bot.send_message(message.chat.id,
                             "Welcome\n\n" + heart + "We are glad to see you in our oasis pleasure" + heart,
                             reply_markup=centum)
    else:
        bot.clear_step_handler_by_chat_id(message.chat.id)
        language = r.get('language' + str(message.chat.id)).decode('utf-8')
        user = r.get(str('Username') + str(message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " перешел в меню")
        bot.send_message(936806920, "@" + str(user) + " перешел в меню")
        centum = telebot.types.InlineKeyboardMarkup()
        if str(language) == 'ukr':
            centum.row(
                telebot.types.InlineKeyboardButton(ledger + "Открыть каталог" + ledger, callback_data="kataloog")
            )
            centum.row(
                telebot.types.InlineKeyboardButton(phone + "Обратная связь" + phone, callback_data="support")
            )
            centum.row(
                telebot.types.InlineKeyboardButton(faqq + "F.A.Q" + faqq, callback_data="faq")
            )
            centum.row(
                telebot.types.InlineKeyboardButton("Language", callback_data="language")
            )
            if str(message.chat.id) == "697601461":
                centum.row(
                    telebot.types.InlineKeyboardButton("Відправити меседж мамонту", callback_data="messtomamont")
                )
            if str(message.chat.id) == "854450608":
                centum.row(
                    telebot.types.InlineKeyboardButton("Відправити меседж мамонту", callback_data="messtomamont")
                )
            bot.send_message(message.chat.id,
                             heart + "Рады видеть тебя в нашем оазисе "
                                     "удовольствия" + heart + "\nЕсли впервые с нами, нажми на F.A.Q для "
                                                              "ознакомления с правилами сервиса",
                             reply_markup=centum)
        else:
            centum.row(
                telebot.types.InlineKeyboardButton(ledger + "Open catalog" + ledger, callback_data="kataloog")
            )
            centum.row(
                telebot.types.InlineKeyboardButton(phone + "Support" + phone, callback_data="support")
            )
            centum.row(
                telebot.types.InlineKeyboardButton(faqq + "F.A.Q" + faqq, callback_data="faq")
            )
            centum.row(
                telebot.types.InlineKeyboardButton("Язык", callback_data="language")
            )
            bot.send_message(message.chat.id,
                             "Welcome\n\n" + heart + "We are glad to see you in our oasis pleasure" + heart,
                             reply_markup=centum)


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('kataloog'):
        bot.answer_callback_query(query.id)
        katalog(query.message)
    if data.startswith('menu'):
        bot.answer_callback_query(query.id)
        menu(query.message)
    if data.startswith('pay'):
        bot.answer_callback_query(query.id)
        adress(query.message)
    if data.startswith('support'):
        bot.answer_callback_query(query.id)
        support(query.message)
    if data.startswith('faq'):
        bot.answer_callback_query(query.id)
        faq(query.message)
    if data.startswith('bitcoin'):
        bot.answer_callback_query(query.id)
        bitcoin(query.message)
    if data.startswith('language'):
        bot.answer_callback_query(query.id)
        language = r.get('language' + str(query.message.chat.id)).decode('utf-8')
        if str(language) == 'ukr':
            r.set('language' + str(query.message.chat.id), 'eng')
        else:
            r.set('language' + str(query.message.chat.id), 'ukr')
        menu(query.message)

    if data.startswith('back'):
        bot.answer_callback_query(query.id)
        if int(r.get((str("nomershluhi") + str(query.message.chat.id)))) > 0:
            r.decr((str("nomershluhi") + str(query.message.chat.id)), 1)
        else:
            r.set((str("nomershluhi") + str(query.message.chat.id)), int(7))
        katalog(query.message)
    if data.startswith('go'):
        bot.answer_callback_query(query.id)
        if int(r.get((str("nomershluhi") + str(query.message.chat.id)))) < 7:
            r.incr((str("nomershluhi") + str(query.message.chat.id)), 1)
        else:
            r.set((str("nomershluhi") + str(query.message.chat.id)), int(0))
        katalog(query.message)
    if data.startswith('whorestatus1'):
        bot.answer_callback_query(query.id)
        number_of_whore = r.get((str('nomershluhi') + str(query.message.chat.id))).decode('utf-8')
        r.set(str('status' + number_of_whore), "На вызове")
        r.set(str('statuse' + number_of_whore), "Busy")
        katalog(query.message)
    if data.startswith('whorestatus2'):
        bot.answer_callback_query(query.id)
        number_of_whore = r.get((str('nomershluhi') + str(query.message.chat.id))).decode('utf-8')
        r.set(str('status' + number_of_whore), "Свободна")
        r.set(str('statuse' + number_of_whore), "Free")
        katalog(query.message)
    if data.startswith('whorestatus3'):
        bot.answer_callback_query(query.id)
        number_of_whore = r.get((str('nomershluhi') + str(query.message.chat.id))).decode('utf-8')
        r.set(str('status' + number_of_whore), "Не работает")
        r.set(str('statuse' + number_of_whore), "Does not work")
        katalog(query.message)

    if data.startswith('messtomamont'):
        bot.answer_callback_query(query.id)
        messtomamont(query.message)


def katalog(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    number_of_whore = r.get((str('nomershluhi') + str(message.chat.id))).decode('utf-8')
    whore = r.get(number_of_whore).decode('utf-8')
    status = r.get('status' + str(number_of_whore)).decode('utf-8')
    statuse = r.get('statuse' + str(number_of_whore)).decode('utf-8')
    urlinfo = r.get('url' + str(number_of_whore)).decode('utf-8')
    katalogarrows = telebot.types.InlineKeyboardMarkup()
    user = r.get(str('Username') + str(message.chat.id)).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        katalogarrows.row(
            telebot.types.InlineKeyboardButton(left, callback_data="back"),
            telebot.types.InlineKeyboardButton(right, callback_data="go")
        )
        if str(status) == 'Свободна':
            katalogarrows.row(
                telebot.types.InlineKeyboardButton(heart + "Заказать" + heart, callback_data="pay")
            )
        katalogarrows.row(
            telebot.types.InlineKeyboardButton(info + " Инфо", url=str(urlinfo)),
            telebot.types.InlineKeyboardButton(house + " На главную", callback_data="menu")
        )
        if str(message.chat.id) == "697601461":
            katalogarrows.row(
                telebot.types.InlineKeyboardButton("На вызове", callback_data='whorestatus1'),
                telebot.types.InlineKeyboardButton("Свободна", callback_data='whorestatus2'),
                telebot.types.InlineKeyboardButton("Не работает", callback_data='whorestatus3')

            )
        if str(message.chat.id) == "936806920":
            katalogarrows.row(
                telebot.types.InlineKeyboardButton("На вызове", callback_data='whorestatus1'),
                telebot.types.InlineKeyboardButton("Свободна", callback_data='whorestatus2'),
                telebot.types.InlineKeyboardButton("Не работает", callback_data='whorestatus3')

            )
        bot.send_message(message.chat.id, str(whore) + status, reply_markup=katalogarrows)
    else:
        katalogarrows.row(
            telebot.types.InlineKeyboardButton(left, callback_data="back"),
            telebot.types.InlineKeyboardButton(right, callback_data="go")
        )
        if str(statuse) == 'Free':
            katalogarrows.row(
                telebot.types.InlineKeyboardButton(heart + "Order" + heart, callback_data="pay")
            )
        katalogarrows.row(
            telebot.types.InlineKeyboardButton(info + " Open info", url=str(urlinfo)),
            telebot.types.InlineKeyboardButton(house + " Main page", callback_data="menu")
        )
        if str(message.chat.id) == "697601461":
            katalogarrows.row(
                telebot.types.InlineKeyboardButton("Busy", callback_data='whorestatus1'),
                telebot.types.InlineKeyboardButton("Free", callback_data='whorestatus2'),
                telebot.types.InlineKeyboardButton("Does not work", callback_data='whorestatus3')
            )
        if str(message.chat.id) == "854450608":
            katalogarrows.row(
                telebot.types.InlineKeyboardButton("Busy", callback_data='whorestatus1'),
                telebot.types.InlineKeyboardButton("Free", callback_data='whorestatus2'),
                telebot.types.InlineKeyboardButton("Does not work", callback_data='whorestatus3')
            )
        bot.send_message(message.chat.id, str(whore) + statuse, reply_markup=katalogarrows)

def adress(message):
    bot.delete_message(message.chat.id, message.message_id)
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        bot.send_message(message.chat.id, "Отправьте боту ваш адрес")
    else:
        bot.send_message(message.chat.id, "Enter your adress")
    print (str(message.message_id))
    r.set('messid' + str(message.chat.id), str(message.message_id))
    bot.register_next_step_handler(message, numphone)


def numphone(message):
    r.set('adress' + str(message.chat.id), str(message.text))
    bot.delete_message(message.chat.id, message.message_id)
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id - 1, text='Введите номер телефона для связи с вами \nНа '
                                                                       'него будет звонить девушка по приезду на '
                                                                       'адрес')
    else:
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id - 1,
                              text="Enter the phone number to contact you \nThe girl on arrival will call to you")
    bot.register_next_step_handler(message, amounthourses)


def amounthourses(message):
    bot.delete_message(message.chat.id, message.message_id)
    r.set('numphone' + str(message.chat.id), str(message.text))
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id - 2,
                              text="Введите количество часов")
    else:

        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id - 2, text="Enter the number of hours")
    bot.register_next_step_handler(message, price)


def price(message):
    messid = r.get('messid' + str(message.chat.id)).decode('utf-8')
    messid = int(messid)
    messid += 1
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        try:
            amount = int(message.text)
        except:
            bot.delete_message(message.chat.id, message.message_id)
            bot.edit_message_text(chat_id=message.chat.id, message_id=str(messid), text="Введите числом")
            bot.register_next_step_handler(message, price)
        else:
            number_of_whore = r.get((str('nomershluhi') + str(message.chat.id))).decode('utf-8')
            pricebefore = r.get('price' + str(number_of_whore))
            priceuah = int(pricebefore) * int(amount)
            r.set('price' + str(message.chat.id), priceuah)
            order(message)
    else:
        try:
            amount = int(message.text)
        except:
            bot.delete_message(message.chat.id, message.message_id)
            bot.edit_message_text(chat_id=message.chat.id, message_id=str(messid), text="Please enter a number")
            bot.register_next_step_handler(message, price)
        else:
            number_of_whore = r.get((str('nomershluhi') + str(message.chat.id))).decode('utf-8')
            pricebefore = r.get('price' + str(number_of_whore))
            priceuah = int(pricebefore) * int(amount)
            r.set('price' + str(message.chat.id), priceuah)
            order(message)


def order(message):
    messid = r.get('messid' + str(message.chat.id)).decode('utf-8')
    messid = int(messid)
    messid += 1
    bot.delete_message(message.chat.id, messid)
    bot.delete_message(message.chat.id, message.message_id)
    number_of_whore = r.get((str('nomershluhi') + str(message.chat.id))).decode('utf-8')
    phone = r.get('numphone' + str(message.chat.id)).decode('utf-8')
    adres = r.get('adress' + str(message.chat.id)).decode('utf-8')
    name = r.get(int(number_of_whore) + int(100)).decode('utf-8')
    priceuah = r.get('price' + str(message.chat.id)).decode('utf-8')
    mamont = r.get(str('Username') + str(message.chat.id)).decode('utf-8')
    keyboard = telebot.types.InlineKeyboardMarkup()
    messto = telebot.types.InlineKeyboardMarkup()
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        keyboard.row(
            telebot.types.InlineKeyboardButton("Оплатить UAH", url='https://telegra.ph/Oplata-11-15'),
            telebot.types.InlineKeyboardButton("Оплатить Bitcoin", callback_data='bitcoin')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton("Отменить заказ", callback_data='kataloog')
        )
    else:
        keyboard.row(
            telebot.types.InlineKeyboardButton("Pay UAH", url='https://telegra.ph/Oplata-11-15'),
            telebot.types.InlineKeyboardButton("Pay Bitcoin", callback_data='bitcoin')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton("Cancel order", callback_data='kataloog')
        )
    bot.send_message(message.chat.id,
                     "Сверьте данные и оплатите услугу \nДевушка приедет в течение 30-40 минут после оплаты и оповестит "
                     "вас звонком\n\nДевушка: " +
                     str(name) +
                     "\nАдрес: " + str(adres) +
                     "\nНомер телефона: " + str(phone) +
                     "\nЦена: " + str(priceuah) + "UAH", reply_markup=keyboard)
    bot.send_message(697601461,
                     "Заявка создана\n"
                     "\nМамонт: @" + str(mamont) +
                     "\nID: " + str(message.chat.id) +
                     "\nШлюха: " + name +
                     "\nНомер телефона: " + str(phone) +
                     "\nАдрес: " + str(adres))
    bot.send_message(936806920,
                     "Заявка создана\n"
                     "\nМамонт: @" + str(mamont) +
                     "\nID: " + str(message.chat.id) +
                     "\nШлюха: " + name +
                     "\nНомер телефона: " + str(phone) +
                     "\nАдрес: " + str(adres))
    bot.register_next_step_handler(message, pay)


def pay(message):
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        if str(message.text) == 'back':
            menu(message)
        else:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "Данные отправлены на проверку оператором")
            bot.register_next_step_handler(message, pay)
    else:
        if str(message.text) == 'back':
            menu(message)
        else:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "Transaction in progress")
            bot.register_next_step_handler(message, pay)


def support(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        keyboard.row(
            telebot.types.InlineKeyboardButton("Вернуться", callback_data='menu')
        )
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Контакт оператора: @kievkizlar", reply_markup=keyboard)
    else:
        keyboard.row(
            telebot.types.InlineKeyboardButton("Back", callback_data='menu')
        )
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Contact to support: @kievkizlar", reply_markup=keyboard)


def faq(message):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        keyboard.row(
            telebot.types.InlineKeyboardButton("Вернуться", callback_data='menu')
        )
        bot.send_message(message.chat.id, "🍓 Відповіді на часті запитання 🍓\n\n"
                                          "🔥 Як зробити замовлення?"
                                          "Виберіть дівчину яка вас зацікавить, якщо вона вільна то буде активний натиск 'Замовити'\nПісля натиску слідуйте інструкціям в боті.\n\n"
                                          "🔥 Як відбувається оплата?\n"
                                          "Ми працюємо тільки за повною передоплатою на рахунок Easypay/bitcoint / Цевимушений крок через скарги самих дівчат, тому що клієнти часто не маютьсерйозних намірів, відмовлялися платити або навіть били та погрожували.\n\n"
                                          "🔥 Чому не можна дати на руки\n"
                                          "Це вимушений крок, на який дівчата пішли через випадки, коли їх викликалимолодики без грошей/брехали що заплатять після/погрожували. Тому ми змушеніпрацювати за іншим принципом.\n\n"
                                          "🔥 Я оплатив, що далі?\n"
                                          "Уточнюємо адрес, дівчина через 40-60 хв. приїжджає.\n\n"
                                          "🔥 Чи є у вас своє місце?\n"
                                          " Так, кожна дівчина може прийняти у себе (квартири по місті.) Виїзд за межі міста обговорюється\n\n"
                                          "Залишились питання?\nПишіть: @MrPhotoshops"

                         , reply_markup=keyboard)
    else:
        keyboard.row(
            telebot.types.InlineKeyboardButton("Back", callback_data='menu')
        )
        bot.send_message(message.chat.id, "🍓 Frequently Asked Questions 🍓\n\n"
                                          "🔥 How to place an order?"
                                          "Choose the girl you are interested in, if she is free then there will be an active press 'Order' \nAfter pressing this, follow the instructions in the bot.\n\n"
                                          "🔥 How is payment made?\n"
                                          "We only work on a full prepayment for Easypay / bitcoint / This is a forced step through the complaints of the girls themselves, because clients often have no serious intentions, refused to pay or even beat and threatened.\n\n"
                                          "🔥 Why can't you give it a hand\n"
                                          "This is a forced move that the girls went through when they were called young without money / lied to pay after / threatened. Therefore, we have to work on a different principle.\n\n"
                                          "🔥 Do you have a place?\n"
                                          " Yes, every girl can take (apartments in the city.) Traveling outside the city is discussed\n\n"
                                          "Any questions left? \nWrite: @MrPhotoshops"

                         , reply_markup=keyboard)


def bitcoin(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Оплатить", url="https://24paybank.net/privat24-uah-to-bitcoin.html"),
        telebot.types.InlineKeyboardButton('Отменить заказ', callback_data='kataloog')
    )
    price = r.get((str("price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        bot.send_message(message.chat.id, "💳 Сумма к оплате: " + str(price) + "UAH" + "\n\n"
                                                                                        "⚠️ ВАЛЮТА BITCOIN  \n\n"
                                                                                        "👉  Для оплаты перейдите по ссылке и следуйте инструкциям.\n\n "
                                                                                        "📨  После оплаты проверьте свой E-mail и пришлите боту TXid \n\n"
                                                                                        "👇 BTC АДРЕС 👇\n" + "1CmxR3gLFUpkZXcrk2QrzoGvRHKe1f5ToM",
                         reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "💳 Amount to be paid: " + str(price) + "UAH" + "\n\n"
                                                                                          "⚠️  BITCOIN  \n\n"
                                                                                          "👉  To pay, follow the link and follow the instructions.\n\n "
                                                                                          "📨  After payment, check your E-mail and send a TXid bot \n\n"
                                                                                          "👇 BTC ADRESS 👇\n" + "1CmxR3gLFUpkZXcrk2QrzoGvRHKe1f5ToM",
                         reply_markup=keyboard)
    bot.register_next_step_handler(message, pay)


def messtomamont(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Введи ID мамонта")
    bot.register_next_step_handler(message, getid)


def getid(message):
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Что отправить ?')
    chatid = str(message.text)
    bot.register_next_step_handler(message, sendmess, chatid)


def sendmess(message, chatid):
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    try:
        bot.send_message(chatid, str(message.text))
    except:
        bot.send_message(message.chat.id, 'шото не так')
        start_command(message)
    else:
        start_command(message)


bot.polling(none_stop=True)
