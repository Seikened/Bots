import telebot
import os

bot = telebot.TeleBot("2001341521:AAF9OlA1_ZykxIR_JgX__T6zy2G18CieFj8")

@bot.message_handler(commands=['start', 'help','diego'])
def send_welcome(message):
	bot.reply_to(message, "QVe el ejemplo xdxdxd!!!!!▲?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)




bot.infinity_polling()

