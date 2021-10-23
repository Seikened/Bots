#import the necessary to Create a bot and create it, this bot need obtain the token from BotFather   https://api.telegram.org/bot2001341521:AAF9OlA1_ZykxIR_JgX__T6zy2G18CieFj8/getUpdates
import telebot
import time
import sqlite3
from  time import strftime


# Create a bot
bot = telebot.TeleBot('2001341521:AAF9OlA1_ZykxIR_JgX__T6zy2G18CieFj8')


"""
Import the necessary to work with the database
The database is a file that contains:
-Iduser and name (The name is taken automatically from the user for the bot)
-The user can not be changed
-The user can not be deleted
-The user can not be added manually
-the user don't need personal commands


-Habit name and if is complete (false by defaul when the habit is created), this habit is part of a list of habits of the user


When a new user is added to the database, the bot automatically adds the user to the list of users and take the name from telegram message.


When a new habit is added to the database, the bot make a question to the user for the name of the habit, take this information and add it to the database
and create a status of the habit (false)


When the user send a message to the bot, the bot check if the message is a command or a message, if the message is a command, the bot check if the command is a personal command
this information will be stored in the database bot will be captured by messages 
List of habbits can be: add a habbit (once), modified the items that are contained (habbits) , deleted the items that are contained (habbits) 
and can show all the items that are contained (habbits)


if the user send a message with the text "name of habit" (the neme needs be iqual to the name in database to shearch it) the bot will mark the habit as completed (in the database need be chanche the selected habit and change the status for true) and will send a message to the user with the text "habit completed"
and the bot will send the incomplete habit to the user


if the status in the database of the habit is true change the status in the database "true" for "✅"
if the status in the database of the habit is false change the status in the database "false" for "❌"


Commands:
/start - start the bot 
/add - add a new habit to the list of the user and save it in the database
/modify - modify the items that are contained in the list of habits of the user and save it in the database
/delete - delete the items that are contained in the list of habits of the user and save it in the database
/show - show all the items that are contained in the list of habits of the user and save it in the database; Create a list of the items that are contained in the list of habits of the user and show it in the format of cute list to the user by message
/help - show the list of commands
/stop - stop the bot for dont save the data in the database and dont send the reminders to the user

all the commands can be used in the chat with the bot and those commands modify the data in the database depending his function assigned
this function is not case sensitive
this commands affect the data in the database.
use emoji to show the user that the bot is working and use emojis for each command
"""


# create a database
conn = sqlite3.connect('habits.db')
c = conn.cursor()


# Create a function for the bot
@bot.message_handler(commands=['start'])
def start(message):
    # Send a message to the user
    bot.send_message(message.chat.id, "Hi, I'm the bot that will help you to manage your habits")
    bot.send_message(message.chat.id, "Type /help to see the list of commands")
    # Save the id of the user in the database
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    # create a table users
    c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)")

    c.execute("INSERT INTO users VALUES (:id, :name)",
              {'id': message.chat.id, 'name': message.chat.first_name})
    conn.commit()
    conn.close()


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "List of commands:")
    bot.send_message(message.chat.id, "/start - start the bot")
    bot.send_message(message.chat.id, "/add - add a new habit to the list of the user and save it in the database")
    bot.send_message(message.chat.id, "/modify - modify the items that are contained in the list of habits of the user and save it in the database")
    bot.send_message(message.chat.id, "/delete - delete the items that are contained in the list of habits of the user and save it in the database")
    bot.send_message(message.chat.id, "/show - show all the items that are contained in the list of habits of the user and save it in the database; Create a list of the items that are contained in the list of habits of the user and show it in the format of cute list to the user by message")
    bot.send_message(message.chat.id, "/help - show the list of commands")
    bot.send_message(message.chat.id, "/stop - stop the bot for dont save the data in the database and dont send the reminders to the user")


@bot.message_handler(commands=['add'])
def add(message):
    # Send a message to the user
    bot.send_message(message.chat.id, "Type the name of the habit")
    # Save the id of the user in the database
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    # create a table habits
    c.execute("CREATE TABLE IF NOT EXISTS habits(id INTEGER PRIMARY KEY, name TEXT, complete INTEGER)")

    c.execute("INSERT INTO habits VALUES (:id, :name, :status)",
              {'id': message.chat.id, 'name': message.text, 'status': False})
    conn.commit()
    conn.close()





@bot.message_handler(commands=['delete'])
def delete(message):
    # Send a message to the user
    bot.send_message(message.chat.id, "Type the name of the habit")
    # Save the id of the user in the database
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute("DELETE FROM habits WHERE id = :id AND name = :name",
              {'id': message.chat.id, 'name': message.text})
    conn.commit()
    conn.close()




"""@bot.message_handler(content_types=['text'])
def text(message):
    # Send a message to the user
    bot.send_message(message.chat.id, "Type the name of the habit")
    # Save the id of the user in the database
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute("UPDATE habits SET name = :name WHERE id = :id",
              {'id': message.chat.id, 'name': message.text})
    conn.commit()
    conn.close()"""




bot.infinity_polling()
