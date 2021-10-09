import telebot
import os

bot = telebot.TeleBot("2001341521:AAF9OlA1_ZykxIR_JgX__T6zy2G18CieFj8")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





@bot.message_handler(commands=['lista'])

def cualquiercosa(message):
	bot.send_message(message.chat.id, "Creando lista de comras...")



@bot.message_handler(regexp='someregexp') 
def command_help(message):
    bot.send_message(message.chat.id, 'Did someone call for help?')



bot.infinity_polling()

