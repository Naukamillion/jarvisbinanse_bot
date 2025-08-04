import telebot
import os
import time
from binance.client import Client

# Telegram bot token
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Binance API keys
API_KEY = os.environ.get("BINANCE_API_KEY")
API_SECRET = os.environ.get("BINANCE_API_SECRET")

client = Client(API_KEY, API_SECRET)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Бот для Binance активен.")

@bot.message_handler(commands=['balance'])
def send_balance(message):
    try:
        balance = client.get_asset_balance(asset='USDT')
        bot.reply_to(message, f"Баланс USDT: {balance['free']}")
    except Exception as e:
        bot.reply_to(message, f"Ошибка получения баланса: {e}")

bot.polling()
