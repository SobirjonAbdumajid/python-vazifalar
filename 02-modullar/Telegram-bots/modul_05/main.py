from translator_kirilLlatin import to_cyrillic,to_latin
import telebot

TOKEN = "7114673209:AAGtVbxPCmA0rkdgQPO4J8PDMZpgfEJs0tI"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    response = 'Assalomu alaykum?'
    response += '\nKirilchani lotinchaga yoki lotinchani kirilchaga o\'tqizib ko\'ring hohlasyz:'
    bot.reply_to(message,response)

@bot.message_handler(func=lambda message : True)
def echo_all(message):
    text = message.text
    result = lambda text1 : to_cyrillic(text1) if text.isascii() else to_latin(text1)
    bot.reply_to(message, result(text))

bot.polling()
