from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Initialize Telegram bot
updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)
dispatcher = updater.dispatcher
