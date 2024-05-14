from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Initialize Telegram bot
updater = Updater(token='6434800925:AAGf1wFrvynlxbs_uvrCN0Ezj5rhfkBohi0', use_context=True)
dispatcher = updater.dispatcher

def handle_message(update: Update, context: CallbackContext):
    message_text = update.message.text
    # Check if the message contains a Mega link
    if "mega.nz" in message_text:
        download_and_upload(update.message.chat_id, message_text)
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Please provide a valid Mega download link.")

# Register message handler
message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
dispatcher.add_handler(message_handler)

import requests

def download_and_upload(chat_id, mega_link):
    # Use Mega download API or library to download the file
    # Display real-time status updates during download

    # Example download using requests
    response = requests.get(mega_link, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    bytes_downloaded = 0
    with open('downloaded_file', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                bytes_downloaded += len(chunk)
                # Calculate and send progress updates
                progress_percentage = (bytes_downloaded / total_size) * 100
                context.bot.send_message(chat_id=chat_id, text=f"Download progress: {progress_percentage}%")
    
    # Upload the downloaded file to Telegram
    context.bot.send_document(chat_id=chat_id, document=open('downloaded_file', 'rb'))

def start_bot():
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    start_bot()
