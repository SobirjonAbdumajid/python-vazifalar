from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Replace 'YOUR_TOKEN' with the token you got from BotFather
TOKEN = 'YOUR_TOKEN'

# Function to start the bot and ask for the phone number
def start(update: Update, context: CallbackContext):
    contact_button = KeyboardButton(text="Share Phone Number", request_contact=True)
    reply_markup = ReplyKeyboardMarkup([[contact_button]], resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text("Please share your phone number:", reply_markup=reply_markup)

# Function to handle the contact (phone number) response
def contact_handler(update: Update, context: CallbackContext):
    contact = update.message.contact
    phone_number = contact.phone_number
    update.message.reply_text(f"Thank you! Your phone number is: {phone_number}")

# Main function to set up the bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command to start the bot
    dp.add_handler(CommandHandler("start", start))

    # Handler to catch the phone number response
    dp.add_handler(MessageHandler(filters.CONTACT, contact_handler))

    # Start polling Telegram for updates
    updater.start_polling()

    # Run the bot until you stop it
    updater.idle()

if __name__ == '__main__':
    main()
