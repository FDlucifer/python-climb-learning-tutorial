# pip install python-telegram-bot

import threading
import time
import sqlite3
import telegram.ext

TOKEN = ""

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

current_name = None
current_date = None

def start(update, context):
    update.message.reply_text("hello world! type /new to create new reminder!")

def new_reminder(update, context):
    update.message.reply_text("whose birthday shall i remind you of?")
    return 1

def get_name(update, context):
    global current_name
    current_name = update.message.text
    update.message.reply_text("when is the birthday (year-month-day)?")
    return 2

def get_date(update, context):
    global current_date
    global cursor

    current_date = update.message.text
    user_id = update.message.chat_id

    cursor.execute("SELECT INTO user WHERE id=?", (user_id,))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO user (id) VALUES (?)", (user_id,))
    
    cursor.execute("INSERT INTO birthday_reminder (user_id, name, date, reminded) VALUES (?,?,?,?)", (user_id, current_name, current_date, 0))

    conn.commit()

    update.message.reply_text("i will remind you!")
    return telegram.ext.ConversationHandler.END

def cancel():
    pass

def do_reminders():
    while True:
        # today = dt.date.today().strftime("%Y-%m-%d")
        cursor.execute("SELECT * FROM main.birthday_reminder WHERE strftime('%d', date) = strftime('%d', 'now')"
                        "AND strftime('%m', date) = strftime('%m', 'now') AND reminded = 0")

        rows = cursor.fetchall()
        for row in rows:
            row_id = row[0]
            name = row[2]
            user_id = row[4]
            updater.bot.send_message(chat_id=user_id, text=f"it's {name}'s birthday today!")
            cursor.execute("UPDATE birthday_reminder SET reminded = 1 WHERE id = ?", (row_id,))
            conn.commit()
        
        time.sleep(10)

conv_handler = telegram.ext.ConversationHandler(
    entry_points=[telegram.ext.CommandHandler("new", new_reminder)],
    states={
        1: [telegram.ext.MessageHandler(telegram.ext.Filters.text, get_name)],
        2: [telegram.ext.MessageHandler(telegram.ext.Filters.text, get_date)]
    },
    fallbacks=[telegram.ext.CommandHandler("cancel", cancel)]
)

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(conv_handler)

threading.Thread(target=do_reminders).start()
updater.start_polling()
updater.idle()

