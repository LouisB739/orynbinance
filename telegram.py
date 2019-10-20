import telebot
import binance
import json

bot = telebot.TeleBot("927884908:AAEOF5CVBsjdVSNLT8--t09MUYdc88xtyDk")



@bot.message_handler(commands=['price'])
def send_welcome(message):
	bot.reply_to(message, binance.get_price_ticker("ETHBTC"))



@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)



bot.polling()