import telebot
from telebot import types
import time
import os
import sys
import datetime
import sqlite3
import random
import string
import re
import json
import requests
import urllib.request
import urllib.parse
import urllib.error
import urllib.request



# Create a bot
bot = telebot.TeleBot('2001341521:AAF9OlA1_ZykxIR_JgX__T6zy2G18CieFj8')



"""
create a database of the viernes_taks.
"""




# Create a database
def create_database():
    conn = sqlite3.connect('viernes_taks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS TaskList
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 date TEXT,
                 done TEXT)''')
    conn.commit()
    conn.close()


"""
this bot can create a list of taks for the user,
TaskList: contains the tasks.
Task: contains the name of the task and the date of the task.
Can marque the task as done.
create commnds for the bot to do the following and send the message to the user with each action.
this commands can modify the list of the tasks
this commands can mark the task as done
this commands can delete the task
this commands can show the list of the tasks
this commands can add a new task
"""


# Create a list of tasks
def create_list(name, date):
    conn = sqlite3.connect('viernes_taks.db')
    c = conn.cursor()
    c.execute("INSERT INTO TaskList (name, date) VALUES (?,?)", (name, date))
    conn.commit()
    conn.close()


# Show the list of tasks
def show_list():
    conn = sqlite3.connect('viernes_taks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM TaskList")
    rows = c.fetchall()
    conn.close()
    return rows


# Mark the task as done
def mark_done(id):
    conn = sqlite3.connect('viernes_taks.db')
    c = conn.cursor()
    c.execute("UPDATE TaskList SET done = ? WHERE id = ?", ('True', id))
    conn.commit()
    conn.close()


# Delete the task
def delete_task(id):
    conn = sqlite3.connect('viernes_taks.db')
    c = conn.cursor()
    c.execute("DELETE FROM TaskList WHERE id = ?", (id,))
    conn.commit()
    conn.close()


# Add a new task    
def add_task(name, date):
    conn = sqlite3.connect('viernes_taks.db')
    c = conn.cursor()
    c.execute("INSERT INTO TaskList (name, date) VALUES (?,?)", (name, date))
    conn.commit()
    conn.close()


