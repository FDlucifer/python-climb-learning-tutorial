# pip install python-telegram-bot
# pip install pandas-datareader

import telegram.ext
import pandas_datareader as web

with open('token.txt', 'r') as f:
    TOKEN = f.read()

def start(update, context):
    update.message.reply_text("hello, welcome to neuralbot!")

def help(update, context):
    update.message.reply_text("""
    the following commands are available:

    /start -> welcome message
    /help -> this message
    /content -> information about neuralnine content
    /contact -> Information about contact
    """)

def content(update, context):
    update.message.reply_text("we have videos and books! watch and read them!")

def contact(update, context):
    update.message.reply_text("you can contact florian on the discord server.")

def stock(update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['Close']
    update.message.reply_text(f"the current price of {ticker} is {price:.2f}$!")

def handle_message(update, context):
    update.message.reply_text(f"you said {update.message.text}")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("stock", stock))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()