import telebot

bot = telebot.TeleBot("7780423838:AAGsnyOpIgqO4OEWcamw1Eg7i5-Kx7f9EAE")

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio'])
def get_forward_id(message):
    if message.forward_from_chat:
        bot.reply_to(message, f"Forwarded Chat ID: {message.forward_from_chat.id}")
    elif message.forward_from:
        bot.reply_to(message, f"Forwarded User ID: {message.forward_from.id}")
    else:
        bot.reply_to(message, f"Current Chat ID: {message.chat.id}")

bot.polling()
