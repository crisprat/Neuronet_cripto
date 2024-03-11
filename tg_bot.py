import telebot
from telebot import types


bot = telebot.TeleBot("6351723271:AAHwEKnnniEmiyfonIKEhPfQ2quLOcPzxQ8")

@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nЧто исследуем сегодня?"
  markup = types.InlineKeyboardMarkup()
  button_0 = types.InlineKeyboardButton(text = 'val_0', callback_data='yes')
  markup.add(button_0)
  bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "val_0":
        second_mess = "ans_0"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("ans_0"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        bot.answer_callback_query(function_call.id)


bot.infinity_polling()
