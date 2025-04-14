import telebot
from telebot import types
import requests

# Token va kanal
TOKEN = '7*************************'  # Bot tokenini o'zgartiring
CHANNEL_ID = '@DevSfera'  # Kanal ID sini qo'ying

# Botni yaratish
bot = telebot.TeleBot(TOKEN)

# Obuna tekshirish
def check_subscription(user_id):
    url = f"https://api.telegram.org/bot{TOKEN}/getChatMember?chat_id={CHANNEL_ID}&user_id={user_id}"
    response = requests.get(url).json()
    status = response.get('result', {}).get('status', '')
    return status in ['member', 'administrator', 'creator']

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if check_subscription(user_id):
        bot.send_message(message.chat.id, "Assalomu alaykum! Ismingizni kiriting:")
        bot.register_next_step_handler(message, ask_name)
    else:
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("🔗 Kanalga obuna bo‘lish", url=f"https://t.me/{CHANNEL_ID[1:]}")
        markup.add(button)
        bot.send_message(message.chat.id, "Botdan foydalanish uchun avval kanalga obuna bo‘ling.", reply_markup=markup)

# Ism qabul qilish
def ask_name(message):
    name = message.text
    bot.send_message(message.chat.id, "Familiyangizni kiriting:")
    bot.register_next_step_handler(message, ask_surname, name)

# Familiya qabul qilish
def ask_surname(message, name):
    surname = message.text
    full_name = f"{name} {surname}"

    # "Main Menu" inline buttonlari yaratish
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Markaz haqida ma'lumot", callback_data='about_center'))
    markup.add(types.InlineKeyboardButton("Tanlovlar haqida", callback_data='about_choices'))
    markup.add(types.InlineKeyboardButton("Markazga murojat", callback_data='contact_center'))
    
    bot.send_message(message.chat.id, f"Rahmat, {full_name}! Endi siz botdan foydalanishingiz mumkin. Quyidagi bo'limlardan tanlang:", reply_markup=markup)

# Callback funksiyalari (inline buttonlar uchun)
@bot.callback_query_handler(func=lambda call: True)
def button_handler(call):
    if call.data == 'about_center':
        bot.answer_callback_query(call.id)
        bot.edit_message_text("Markaz haqida ma'lumot: Bu yerda markaz haqida qisqacha ma'lumot keladi.", chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == 'about_choices':
        bot.answer_callback_query(call.id)
        bot.edit_message_text("Tanlovlar haqida: Bu yerda tanlovlar haqida ma'lumot keladi.", chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == 'contact_center':
        bot.answer_callback_query(call.id)
        bot.edit_message_text("Markazga murojat: Bu yerda markazga murojat qilish uchun ma'lumotlar keladi.", chat_id=call.message.chat.id, message_id=call.message.message_id)

# Botni ishga tushurish
bot.polling(none_stop=True, interval=2, timeout=60, long_polling_timeout=60)
