import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8129443607:AAFbDtrj0hmQHjJ2-OdYdhCoUhYizJ6egRM"
bot = telebot.TeleBot(TOKEN)

CHANNEL_URL = "https://t.me/istsahravip"

@bot.message_handler(func=lambda m: True)
def welcome(message):
    chat_id = message.chat.id

    text = (
        "🌆 İstanbul’un en büyük platform botuna **Hoş Geldiniz**!\n\n"
        "Aşağıdan istediğiniz kategoriyi seçebilirsiniz:"
    )

    # Inline butonlar (tıklandığında direkt kanala gider)
    keyboard = InlineKeyboardMarkup()
    buttons = [
        ("💎 İstanbul VIP", CHANNEL_URL),
        ("🏙 İstanbul", CHANNEL_URL),
        ("🔥 En İyiler", CHANNEL_URL),
        ("💃 En Sexy", CHANNEL_URL),
    ]

    for name, url in buttons:
        keyboard.add(InlineKeyboardButton(text=name, url=url))

    bot.send_message(
        chat_id,
        text,
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

bot.polling()
