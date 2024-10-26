import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random

Token = '7130087451:AAHrO_BSqvfLsDWBbkoTMC_2bhex05o7ZQ8'

bot = telebot.TeleBot(Token, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    javob = 'Assalomu alaykum, '
    javob += 'Iltimos nomeringizni yuboring!'
    
    # Create a ReplyKeyboardMarkup object
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    
    # Add a button that requests the user's phone number
    phone_button = KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)
    markup.add(phone_button)
    
    # Send the message with the custom keyboard
    bot.send_message(message.chat.id, javob, reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    # This function handles the phone number after the user shares it
    contact = message.contact
    # javob = f"Rahmat, sizning raqamingiz: {contact.phone_number}"
    random_number = random.randint(1000, 9999)
    javob = f"\nKodingiz: {random_number}"
    bot.send_message(message.chat.id, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    bot.reply_to(message, msg)

bot.polling()
